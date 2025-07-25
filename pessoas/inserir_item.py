import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
tabela = dynamodb.Table(os.environ['NOME_TABELA'])

def lambda_handler(event, context):
    try:
        corpo = json.loads(event['body'])
        nome = corpo['nome']
        idade = corpo['idade']

        resposta = tabela.put_item(
            Item={
                'nome': nome,
                'idade': idade,
                'criado_em': datetime.utcnow().isoformat()
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item inserido com sucesso!'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
