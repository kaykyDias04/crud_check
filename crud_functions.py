import email
import json
import menu_functions
import json_functions
from json_functions import *

def adicionar_usuario(novo_usuario):
    usuarios_adm = json_functions.carregar_usuarios_adm()
    usuarios_adm.append(novo_usuario)
    json_functions.salvar_usuarios_adm(usuarios_adm)

def cadastro_adm():
    json_functions.carregar_usuarios_adm()
    username = input("Informe o nome de usuário do novo administrador: ")
    nome = input("Informe o nome do novo administrador: ")
    idade = input("Informe a idade do novo administrador: ")
    email = input("Informe o email do novo administrador: ")
    telefone = input("Informe o telefone do novo administrador: ")
    senha = input("Informe a senha do novo administrador: ")
    novo_adm = {
            "username": username,
            "nome": nome,
            "idade": idade,
            "email": email,
            "telefone": telefone,
            "senha": senha
        }
    adicionar_usuario(novo_adm)

def listar_adm():
    usuarios_adm = json_functions.carregar_usuarios_adm()
    if usuarios_adm:
        print("\nADMINISTRADORES CADASTRADOS:")
        for i, user in enumerate(usuarios_adm[1:], start=1):
            print(f"{i}: {user}")
    else:
        print("Nenhum usuário cadastrado!")

def alterar_adm():
    usuarios_adm = json_functions.carregar_usuarios_adm()
    listar_adm()
    json_functions.carregar_usuarios_adm()
    resposta = int(input("\nQual administrador você quer modificar?"))
    try:
        if 0 < resposta <len(usuarios_adm):
            print(f"\nQual informação você gostaria de alterar?")
            print("[1] Username ")
            print("[2] Nome")
            print("[3] Idade")
            print("[4] Email")
            print("[5] Telefone")
            print("[6] Senha")

            opcao = int(input("\n"))
            campos = ["username", "nome", "idade", "email", "telefone", "senha"]

            if 1 <= opcao <= 6:
                novo_valor = input(f"Digite o novo valor para {campos[opcao - 1]}: ")
                usuarios_adm[resposta][campos[opcao - 1]] = novo_valor
                json_functions.salvar_usuarios_adm(usuarios_adm)
                print("Informação alterada com sucesso!")
            else:
                print("Opção inválida! ")
        else:
            print("Administrador não encontrado!")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

def remover_adm():
    listar_adm()
    usuarios_adm = json_functions.carregar_usuarios_adm()
    resposta = int(input("\nQual usuário você quer remover? "))
    if 0 < resposta <= len(usuarios_adm):
     usuarios_adm.pop(resposta)
     print("Usuario removido com sucesso! ")
    else:
        print("Nenhum usuario encontrado")
    json_functions.salvar_usuarios_adm(usuarios_adm)

def listar_denuncias():
    denuncias = json_functions.carregar_denuncias()
    if denuncias:
        print("\nLISTA DE DENÚNCIAS:")
        for i, denuncia in enumerate(denuncias[1:], start=1):
            print(f"{i}: {denuncia}")
    else:
        print("Nenhuma denúncia encontrada!")