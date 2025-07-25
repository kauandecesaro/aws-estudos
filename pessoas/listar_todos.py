import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
tabela = dynamodb.Table(os.environ['NOME_TABELA'])

def lambda_handler(event, context):
    try:
        resposta = tabela.scan()
        itens = resposta.get('Items', [])

        return {
            'statusCode': 200,
            'body': json.dumps(itens)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
