import boto3

s3 = boto3.client('s3')

bucket_name = 'meu-bucket-kauan-123456'
file_name = 'texte.txt'  # arquivo no bucket
download_path = 'downloaded_texte.txt'  # onde vai salvar localmente

try:
    s3.download_file(bucket_name, file_name, download_path)
    print(f'Arquivo {file_name} baixado com sucesso para {download_path}')
except Exception as e:
    print(f'Erro ao baixar arquivo: {e}')
