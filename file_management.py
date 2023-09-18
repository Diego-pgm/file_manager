"""A program to update files"""
import os
import subprocess

def cust_menu(opts):
    hor = '###' * 10
    header = '{} file updater {}\n'.format(hor,hor)
    body = ''
    for key, value in opts.items():
        body = body + '{}) {}\n'.format(key, value)
    menu = header + body
    return menu


def list_files():
    return subprocess.check_output(['ls','files']), 'let there be files!'

def manage_files(file_name, command):
    path = "files/" + file_name
    subprocess.call([command, path])
    if command == 'touch':
        return 'File created!'
    elif command == 'rm':
        return 'File deleted!'

opts = {"1":"create file", "2": "list files", "3":"insert to file", "4":"delete file", "5":"exit"}
while True:
    message = 'This is the default message'
    os.system('clear')
    menu = cust_menu(opts)
    print(menu)
    select = input("Select>> ")
    if select == "5":
        print('bye bye')
        quit()
    elif select == "1":
        file_name = input('Insert the file name>> ')
        #message = create_file(file_name)
        message = manage_files(file_name, 'touch')
    elif select == "2":
        files, message = list_files()
        print(files.decode().split())
    elif select == "3":
        print("insert to file")
    elif select == "4":
        file_name = input('Insert the file name>> ')
        message = manage_files(file_name, 'rm')
    else:
        print("not an option")
    print(message)
    input()

