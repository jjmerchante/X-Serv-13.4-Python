#!/usr/bin/python

fich=open("/etc/passwd","r")
users_lines = fich.readlines()
fich.close()

dicc = {}

for user_line in users_lines:
    lista_user = user_line.split(":")
    user = lista_user[0]
    shell = lista_user[-1][:-1] #Principio a final menos el /n
    dicc [username] = shell
    print user +" su shell es "+ shell,
