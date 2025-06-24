import boto3
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

tabela = dynamodb.Table("Pessoas")

try:
    response = tabela.scan()  # Scan traz todos os itens da tabela
    itens = response.get('Items', [])
    
    if itens:
        print("✅ Itens na tabela Pessoas:")
        for item in itens:
            print(item)
    else:
        print("⚠️ Nenhum item encontrado.")

except Exception as e:
    print("❌ Erro ao listar itens:", e)
