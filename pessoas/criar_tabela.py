import boto3
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Credenciais e região
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Cliente do DynamoDB
dynamodb = boto3.client(
    "dynamodb",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Criação da tabela
try:
    response = dynamodb.create_table(
        TableName='Pessoas',
        KeySchema=[
            {
                'AttributeName': 'pessoa_id',
                'KeyType': 'HASH'  # Chave primária
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'pessoa_id',
                'AttributeType': 'S'  # Tipo String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("✅ Tabela criada com sucesso!")
    print("Status:", response['TableDescription']['TableStatus'])

except dynamodb.exceptions.ResourceInUseException:
    print("⚠️ A tabela 'Pessoas' já existe.")

except Exception as e:
    print("❌ Erro ao criar a tabela:", e)
