import boto3
import os
from dotenv import load_dotenv

# Carrega .env
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Cliente
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Tabela
tabela = dynamodb.Table("Pessoas")

# ID da pessoa que queremos buscar
pessoa_id = "1"

# Buscar item
try:
    response = tabela.get_item(Key={"pessoa_id": pessoa_id})
    
    if "Item" in response:
        print("✅ Pessoa encontrada:")
        print(response["Item"])
    else:
        print("⚠️ Pessoa não encontrada.")

except Exception as e:
    print("❌ Erro ao buscar item:", e)