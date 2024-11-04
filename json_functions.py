import json
from xml.etree.ElementTree import indent

import crud_functions
import menu_functions
import os

denuncias = [{
    "categoria": "",
    "data": "",
    "local": "",
    "descricao": "",
    "numero_de_protoclo": "",
    "progresso":""
}]

usuarios_adm = [{
    "nome": "",
    "idade": "",
    "email": "",
    "telefone": "",
    "senha": ""
}]

categorias_denuncias = {
    "categorias": ["Roubo", "Furto", "Assédio",
                   "Agressão Física", "Fraude", "Tráfico de Drogas",
                   "Vandalismo", "Violência Doméstica", "Discriminação"]
}


def salvar_denuncias(denuncias):
    with open("denuncias.json", 'a', encoding='utf-8') as file:
        json.dump(denuncias, file, ensure_ascii=False, indent=4)

def salvar_usuarios_adm(usuarios_adm):
    with open("usuarios.json", 'a', encoding='utf-8') as file:
        json.dump(usuarios_adm, file, ensure_ascii=False, indent=4)
    print("Usuário modificado com sucesso!")

def salvar_categorias(categorias_denuncias):
    with open("categorias.json", 'a', encoding='utf-8') as file:
        json.dump(categorias_denuncias, file, ensure_ascii=False, indent=4)


def carregar_denuncias():
    with open("denuncias.json", 'r', encoding="utf-8") as file:
        json.load(file)

def carregar_usuarios_adm():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Erro ao decodificar o JSON. O arquivo pode estar corrompido.")
                return []
    return []

def carregar_categorias():
    with open("categorias.json", 'r', encoding="utf-8") as file:
        json.load(file)
