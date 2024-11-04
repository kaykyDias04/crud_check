import email
import json
import menu_functions
import json_functions
from main import usuarios_adm, usuario_arquivo


def adicionar_usuario(novo_usuario):
    usuarios_adm = json_functions.carregar_usuarios_adm()
    usuarios_adm.append(novo_usuario)
    json_functions.salvar_usuarios_adm(usuarios_adm)

def cadastro_adm():
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

