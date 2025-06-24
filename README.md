# Gerenciador de Pessoas com DynamoDB e Python

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Boto3](https://img.shields.io/badge/boto3-aws--sdk-green.svg)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Descrição

Script em Python para gerenciar uma tabela DynamoDB chamada **Pessoas**, utilizando o AWS SDK Boto3. Permite inserir, atualizar, listar e deletar pessoas via menu interativo no terminal.

## Funcionalidades

- Inserção de novos registros
- Atualização de registros existentes
- Listagem completa de registros
- Remoção de registros
- Interface interativa por terminal

## Pré-requisitos

- Python 3.6 ou superior
- AWS CLI configurada ou credenciais AWS em `.env`
- Pacotes Python: `boto3`, `python-dotenv`

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio

Instale as dependências:
pip install boto3 python-dotenv

Configure o arquivo .env com suas credenciais AWS:
AWS_ACCESS_KEY_ID=suachave
AWS_SECRET_ACCESS_KEY=suasecreta
AWS_REGION=sua-regiao

Uso
Execute o script principal:
python menu_pessoas.py

Siga as instruções do menu para gerenciar a tabela.

Contribuição
Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de alterar.

Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para detalhes.

Feito por Kauan de Césaro.
