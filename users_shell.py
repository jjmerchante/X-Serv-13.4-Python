#!/usr/bin/python

fich=open("/etc/passwd","r")
users_lines = fich.readlines()
fich.close()

for user_line in users_lines:
    lista_user = user_line.split(":")
    username = lista_user[0]
    shell = lista_user[-1][:-1]
    print username +" --> "+ shell
print "hay", len(users_lines), "usuarios"
