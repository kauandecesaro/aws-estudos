import boto3
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Cliente do DynamoDB
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Tabela
tabela = dynamodb.Table("Pessoas")

# Dados a serem inseridos
item = {
    "pessoa_id": "1",               # Chave primária
    "nome": "Kauan de Césaro",
    "idade": 25,
    "email": "kauan@example.com"
}

# Inserção
try:
    tabela.put_item(Item=item)
    print("✅ Item inserido com sucesso!")

except Exception as e:
    print("❌ Erro ao inserir item:", e)
