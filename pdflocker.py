import argparse
import getpass
import os
import sys
from pypdf import PdfReader, PdfWriter

def protect_pdf(input_path, password):
    # 1. Validação básica
    if not os.path.exists(input_path):
        print(f"[ERRO] O arquivo '{input_path}' não foi encontrado.")
        sys.exit(1)

    # 2. Definição do nome de saída (input.pdf -> input_protected.pdf)
    base_name, ext = os.path.splitext(input_path)
    output_path = f"{base_name}_protected{ext}"

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        # 3. Copia todas as páginas
        for page in reader.pages:
            writer.add_page(page)

        # 4. Aplica criptografia AES-256 (Padrão Ouro)
        # Nota: AES-256 é muito superior ao padrão antigo.
        writer.encrypt(user_password=password, algorithm="AES-256")

        # 5. Salva o arquivo
        with open(output_path, "wb") as f:
            writer.write(f)
        
        print(f"[\u2714] Sucesso! Arquivo criptografado gerado: {output_path}")

    except Exception as e:
        print(f"[FALHA] Erro ao processar o PDF: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="OiSecurity PDF Locker - CLI Tool")
    
    # Argumentos
    parser.add_argument("file", help="Caminho do arquivo PDF original")
    parser.add_argument("-p", "--password", help="Senha para criptografar (Opcional. Se omitido, será solicitada de forma segura)", default=None)

    args = parser.parse_args()

    # Lógica de Senha Segura
    pwd = args.password
    if not pwd:
        # Se não passou a flag -p, pede interativamente (Input oculto)
        try:
            pwd = getpass.getpass(prompt="Digite a senha para o PDF (input oculto): ")
            if not pwd:
                print("[ERRO] A senha não pode estar vazia.")
                sys.exit(1)
        except KeyboardInterrupt:
            print("\n[!] Operação cancelada.")
            sys.exit(0)

    protect_pdf(args.file, pwd)

if __name__ == "__main__":
    main()
