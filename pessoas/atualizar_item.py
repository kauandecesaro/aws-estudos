import boto3
import os
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

tabela = dynamodb.Table("Pessoas")

try:
    response = tabela.update_item(
        Key={"pessoa_id": "3"},
        UpdateExpression="SET idade = :idade, email = :email",
        ExpressionAttributeValues={
            ":idade": 32,
            ":email": "joaovitorsilva@atualizado.com"
        },
        ReturnValues="UPDATED_NEW"
    )

    print("✅ Item atualizado com sucesso!")
    print(response["Attributes"])

except Exception as e:
    print("❌ Erro ao atualizar item:", e)
