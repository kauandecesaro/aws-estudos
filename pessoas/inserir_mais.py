import boto3
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Conectar com DynamoDB
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

# Apontar para a tabela
tabela = dynamodb.Table("Pessoas")

# Lista de novos itens
novos_dados = [
    {"pessoa_id": "2", "nome": "Maria Souza", "idade": 30, "email": "maria@example.com"},
    {"pessoa_id": "3", "nome": "João Silva", "idade": 40, "email": "joao@example.com"},
    {"pessoa_id": "4", "nome": "Ana Costa", "idade": 22, "email": "ana@example.com"}
]

# Inserir cada item na tabela
for item in novos_dados:
    try:
        tabela.put_item(Item=item)
        print(f"✅ Inserido: {item['nome']}")
    except Exception as e:
        print(f"❌ Erro ao inserir {item['nome']}: {e}")
