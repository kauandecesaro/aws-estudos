import boto3
import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

arquivo_local = "arquivos/teste_upload.txt"
nome_bucket = "meu-bucket-kauan-123456"
nome_objeto_s3 = os.path.basename(arquivo_local)  # nome do arquivo que vai no bucket

try:
    with open(arquivo_local, "rb") as data:
        s3.upload_fileobj(data, nome_bucket, nome_objeto_s3)
    print(f"✔️ Upload do arquivo '{nome_objeto_s3}' feito com sucesso no bucket '{nome_bucket}'")
except Exception as e:
    print(f"❌ Erro no upload: {str(e)}")
