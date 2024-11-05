import os
import time
import random
import json_functions
import crud_functions

denuncias = [{
}]

usuarios_adm = [{
}]

categorias_denuncias = {
    "categorias": ["Roubo", "Furto", "Assédio",
                   "Agressão Física", "Fraude", "Tráfico de Drogas",
                   "Vandalismo", "Violência Doméstica", "Discriminação"]
}

def gerar_protocolo():
    protocolo = random.randint(100000, 999999)
    return protocolo
numero_protocolo = gerar_protocolo()

def autenticacao_adm():
    usuarios_adm = json_functions.carregar_usuarios_adm()
    nome_usuario = input("\nInforme seu nome de usuário: ")
    senha = input("Informe sua senha: ")

    username_padrao = "admin"
    senha_padrao = "123456"

    autenticado = any(
        nome_usuario == user.get("username") and senha == user.get("senha")
        for user in usuarios_adm) or nome_usuario == username_padrao and senha == senha_padrao

    if autenticado:
        print("\n Autenticação realizada, bem vindo!")
        menu_adm()
    else:
        print("\n Infelizmente você não tem acesso! ")

def menu_inicial():
    print("                                 ")
    print("█▀█ █▀█ █   █ █▀▀ █ ▄▀█   █▀▀ █ █ █ █ █")
    print("█▀▀ █▄█ █▄▄ █ █▄▄ █ █▀█   █▄▄ █ ▀▄▀ █ █▄▄")
    print("Faça sua denúncia com a gente de forma segura!")
    print("                                 ")
    time.sleep(1)
    os.system("cls")

def menu_principal():
    while True:
        print("\n", "="*20, "Menu Principal", "="*20)
        print("[1] Área de Administrador")
        print("[2] Denúncia Anônima")
        print("[3] Sair")
        escolha = int(input("\nEscolha um para continuar: "))
        match escolha:
            case 1:
                autenticacao_adm()
            case 2:
                menu_denuncia()
            case 3:
                print("Encerrando...")
                time.sleep(1.5)
                break
            case _:
                print("Escolha uma opção válida!")
                time.sleep(1)

def menu_denuncia():
    while True:
        print("\n", "="*20, "Denúncia Anônima", "="*20)
        print("[1] Realizar Denúncia Anônima")
        print("[2] Busca por Denúncia")
        print("[3] Sair")
        resposta= int(input("Escolha um para continuar:"))
        match resposta:
            case 1:
                crud_functions.criar_denuncia()
            case 2:
                protocolo = input("\nInforme o número do protocolo da sua denúncia: ")
                crud_functions.buscar_denuncias(protocolo)
            case 3:
                break

def menu_adm():
    while True:
        print("\n", "=" * 20, "Área de Administrador", "=" * 20)
        print("[1] Cadastrar Administrador")
        print("[2] Listar Administradores")
        print("[3] Atualizar Administrador")
        print("[4] Remover Administrador")
        print("[5] Listar Todas as Denúncias")
        print("[6] Atualizar Progresso de Denúncia")
        print("[7] Remover Denúncia")
        print("[8] Edição de Categorias")
        print("[9] Sair")
        resposta = int(input("Escolha um para continuar:"))

        match resposta:
            case 1:
                crud_functions.cadastro_adm()
            case 2:
                crud_functions.listar_adm()
            case 3:
                crud_functions.alterar_adm()
            case 4:
                crud_functions.remover_adm()
            case 5:
                crud_functions.listar_denuncias()
            case 6:
                crud_functions.atualizar_progresso()
            case 7:
                crud_functions.remover_denuncia()
            case 8:
                menu_categorias()
            case 9:
                print("Voce esta saindo da area do administrador!")
                time.sleep(1)
                break
            case _ :
                print("Digite uma opção válida!")

def menu_categorias():
    while True:
        print("=" * 20, "Menu de Edição de Categorias", "=" * 20)
        print("[1] Criar Nova Categoria")
        print("[2] Listar Categorias")
        print("[3] Editar Categoria Existente")
        print("[4] Remover Categoria")
        print("[5] Sair")
        resposta = int(input("Escolha um para continuar:"))
        match resposta:
            case 1:
                crud_functions.criar_categoria()
            case 2:
                crud_functions.listar_categorias()
            case 3:
                crud_functions.editar_categoria()
            case 4:
                crud_functions.remover_categoria()
            case 5:
                break
            case _:
                print("Informe um valor válido! ")

def main():
    menu_inicial()
    menu_principal()

if __name__=="__main__":
      main()