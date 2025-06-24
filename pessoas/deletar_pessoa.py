import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Conectar com o DynamoDB
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

tabela = dynamodb.Table("Pessoas")

# Entrada do usuário
pessoa_id = input("🧍 Digite o ID da pessoa que deseja deletar: ")

# Confirmação
confirmar = input(f"⚠️ Tem certeza que deseja deletar o ID {pessoa_id}? (s/n): ")

if confirmar.lower() == "s":
    try:
        tabela.delete_item(Key={"pessoa_id": pessoa_id})
        print(f"✅ Pessoa com ID {pessoa_id} deletada com sucesso!")
    except Exception as e:
        print("❌ Erro ao deletar:", e)
else:
    print("🚫 Ação cancelada. Nada foi deletado.")
