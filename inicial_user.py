# -*- coding: utf-8 -*-

import getpass
from settings import FACTORY
from dao.User import User

def menu():
    print "Gerenciamento de usuários"
    print "1 - Inserir usuário"
    print "2 - Listar usuários"
    print "3 - Excluir usuário"
    print "0 - Sair"

    option = int(raw_input("Digite sua opção: "))
    if option == 1:
        insert_user()
        result = True
    elif option == 2:
        list_users()
        result = True
    elif option == 3:
        excluir_user()
        result = True
    else:
        result = False
    return result

def insert_user():
    dao_user = FACTORY.getUserDao()

    password_ok = False
    username_ok = False
    while not username_ok and not password_ok:
        nome = raw_input("Informe o Nome: ")
        username = raw_input("Informe o email: ")
        if dao_user.check_user(username):
            print "Email já existe."
            continue
        password = getpass.getpass("Informe a senha: ")
        password_repeat = getpass.getpass("Informe novamente a senha: ")
        if password == password_repeat:
            password_ok = True
        else:
            print "Senhas não conferem."
    user = User(
        nome,
        username,
        password,
    )

    if dao_user.insert(user):
        print "\nUsuario salvo\n"
    else:
        print "\nErro\n"


def list_users():
    dao_user = FACTORY.getUserDao()
    users = dao_user.get_all()
    if users:
        for user in users:
            print "nome: %s | email: %s\n" % (user.nome, user.email)
    else:
        print "\nNenhum usuario\n"


def excluir_user():
    dao_user = FACTORY.getUserDao()

    username = raw_input("Informe o email: ")
    user = dao_user.check_user(username)
    if user:
        excluido = dao_user.delete_um(user.id)
        if excluido:
            print "\nUsuario excluido\n"
        else:
            print "\nErro\n"
    else:
        print "\nUsuario não existe \n"
            

def main():
    run = True
    while run:
        run = menu()

if __name__ == "__main__":
    main()
