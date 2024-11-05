import json
import os
import time
import random
import json_functions
import menu_functions
import crud_functions

denuncias = [{
    "categoria": "",
    "data": "",
    "local": "",
    "descricao": "",
    "numero_de_protocolo": "",
    "progresso":""
}]

usuarios_adm = [{
    "username":"",
    "nome": "",
    "idade": "",
    "email": "",
    "telefone": "",
    "senha": ""
}]

categorias_denuncias = [{
    "categorias": ["Roubo", "Furto", "Assédio",
                   "Agressão Física", "Fraude", "Tráfico de Drogas",
                   "Vandalismo", "Violência Doméstica", "Discriminação"]
}]

denuncia_arquivo: str = "denuncias.json"
usuario_arquivo: str = "usuarios.json"
categoria_arquivo: str = "categorias.json"

username_padrao = "admin"
senha_padrao = 123456

def gerar_protocolo():
    protocolo = random.randint(10000, 99999)
    return protocolo

numero_protocolo = gerar_protocolo()


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
                print("\nBem vindo a area ADM!")
                try:
                    nome_usuario = input("\nInforme seu nome de usuário: ")
                    senha=int(input("Insira sua senha: "))
                    if (nome_usuario in usuarios_adm and senha == usuarios_adm[nome_usuario]) or \
                       (nome_usuario == username_padrao and senha == senha_padrao):
                        print("\nAutenticação bem sucedida! ")
                        menu_adm()
                    else:
                        print("\nInfelizmente voce não tem o acesso!")
                except ValueError:
                    print("Entrada inválida, insira um número para a senha,")
            case 2:
                menu_denuncia()
            case 3:
                print("Encerrando...")
                time.sleep(1.5)
                break
            case _:
                print("Escolha uma opção válida!")
                time.sleep(1)

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
                print("exemplo")
            case 7:
                print("exemplo")
            case 8:
                print("exemplo")
            case 9:
                print("Voce esta saindo da area do administrador!")
                time.sleep(1)
                break
            case _ :
                print("Digite uma opção válida!")


def menu_denuncia():
    while True:
        print("="*20, "Denúncia Anônima", "="*20)
        print("[1] Realizar Denúncia Anônima")
        print("[2] Busca por Denúncia")
        print("[3] Sair")
        resposta= int(input("Escolha um para continuar:"))
        match resposta:
            case 1:
                print("exemplo")
            case 2:
                print("exemplo")
            case 3:
                break

def main():
    menu_inicial()
    menu_principal()

if __name__=="__main__":
      main()
