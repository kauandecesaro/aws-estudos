import boto3
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Define base do projeto para caminhos absolutos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminhos absolutos para arquivos locais
arquivo_local = os.path.join(BASE_DIR, "..", "arquivos", "teste_upload.txt")
arquivo_destino_download = os.path.join(BASE_DIR, "..", "arquivos", "baixado.txt")

# Garante que a pasta 'arquivos' existe
os.makedirs(os.path.join(BASE_DIR, "..", "arquivos"), exist_ok=True)

# Credenciais AWS via .env
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")
bucket_name = "meu-bucket-kauan-123456"  # seu bucket correto

# Cria cliente S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

def fazer_upload():
    try:
        s3.upload_file(arquivo_local, bucket_name, "teste_upload.txt")
        print(f"✅ Upload feito: {arquivo_local} → S3/teste_upload.txt")
    except Exception as e:
        print(f"❌ Erro no upload: {e}")

def listar_arquivos():
    try:
        resposta = s3.list_objects_v2(Bucket=bucket_name)
        print(f"\n📂 Arquivos no bucket '{bucket_name}':")
        if 'Contents' in resposta:
            for obj in resposta['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(" (nenhum arquivo encontrado)")
    except Exception as e:
        print(f"❌ Erro ao listar arquivos: {e}")

def fazer_download():
    try:
        s3.download_file(bucket_name, "teste_upload.txt", arquivo_destino_download)
        print(f"✅ Download concluído: S3/teste_upload.txt → {arquivo_destino_download}")
    except Exception as e:
        print(f"❌ Erro no download: {e}")

if __name__ == "__main__":
    fazer_upload()
    listar_arquivos()
    fazer_download()
