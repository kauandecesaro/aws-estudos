import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Conectar ao DynamoDB
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

tabela = dynamodb.Table("Pessoas")

def inserir_pessoa():
    pessoa_id = input("ID: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")

    try:
        tabela.put_item(
            Item={
                "pessoa_id": pessoa_id,
                "nome": nome,
                "idade": idade,
                "email": email
            }
        )
        print(f"✅ Pessoa '{nome}' inserida com sucesso!\n")
    except Exception as e:
        print("❌ Erro ao inserir:", e)

def atualizar_pessoa():
    pessoa_id = input("ID da pessoa que deseja atualizar: ")
    novo_email = input("Novo email: ")
    nova_idade = int(input("Nova idade: "))

    try:
        response = tabela.update_item(
            Key={"pessoa_id": pessoa_id},
            UpdateExpression="SET email = :email, idade = :idade",
            ExpressionAttributeValues={
                ":email": novo_email,
                ":idade": nova_idade
            },
            ReturnValues="UPDATED_NEW"
        )
        print("✅ Atualização feita!")
        print(response["Attributes"], "\n")
    except Exception as e:
        print("❌ Erro ao atualizar:", e)

def listar_pessoas():
    try:
        response = tabela.scan()
        itens = response["Items"]
        print("\n📋 Lista de Pessoas:")
        for pessoa in itens:
            print("-" * 40)
            for k, v in pessoa.items():
                print(f"{k}: {v}")
        print("-" * 40 + "\n")
    except Exception as e:
        print("❌ Erro ao listar:", e)

def deletar_pessoa():
    pessoa_id = input("ID da pessoa que deseja deletar: ")
    confirmar = input(f"⚠️ Tem certeza que deseja deletar {pessoa_id}? (s/n): ")
    if confirmar.lower() == "s":
        try:
            tabela.delete_item(Key={"pessoa_id": pessoa_id})
            print(f"✅ Pessoa com ID {pessoa_id} deletada com sucesso!\n")
        except Exception as e:
            print("❌ Erro ao deletar:", e)
    else:
        print("🚫 Ação cancelada.\n")

def menu():
    while True:
        print("=== Menu - Gerenciamento de Pessoas ===")
        print("1 - Inserir nova pessoa")
        print("2 - Atualizar pessoa existente")
        print("3 - Listar todas as pessoas")
        print("4 - Deletar uma pessoa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_pessoa()
        elif opcao == "2":
            atualizar_pessoa()
        elif opcao == "3":
            listar_pessoas()
        elif opcao == "4":
            deletar_pessoa()
        elif opcao == "0":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.\n")

if __name__ == "__main__":
    menu()
