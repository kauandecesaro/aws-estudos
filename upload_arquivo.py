import boto3
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

# Pega credenciais e região do .env
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Nome do bucket e caminho do arquivo local
bucket_name = "meu-bucket-kauan-123456"
arquivo_local = "aws-estudos/arquivos/teste_upload.txt"
nome_arquivo_s3 = "teste_upload.txt"

# Cria o cliente S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Faz o upload do arquivo
try:
    s3.upload_file(arquivo_local, bucket_name, nome_arquivo_s3)
    print(f"✅ Upload feito com sucesso: {nome_arquivo_s3}")
except Exception as e:
    print(f"❌ Erro no upload: {e}")
