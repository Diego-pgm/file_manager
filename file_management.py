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

def insert_to_file(file_name, content=[]):
    path = 'files/' + file_name
    for line in content:
        with open(path, 'a') as file:
            file.write(line)
    return 'Insert done!'

def read_file(file_name):
    path = 'files/' + file_name
    with open(path) as file:
        print(file.read())
    return 'Interesting, right?!'

def get_file_name():
    file_name = input('Insert the file name>> ')
    return file_name


opts = {"1":"create file", "2": "list files", "3":"insert to file", "4":"read file", "5":"delete file", "6":"exit"}
while True:
    message = 'This is the default message'
    os.system('clear')
    menu = cust_menu(opts)
    print(menu)
    select = input("Select>> ")
    if select == "6":
        print('bye bye')
        quit()
    elif select == "1":
        file_name = get_file_name()
        message = manage_files(file_name, 'touch')
    elif select == "2":
        files, message = list_files()
        print(files.decode())
    elif select == "3":
        files = list_files()
        print(files[0].decode())
        file_name = get_file_name()
        print('Insert the content of the file PRESS ENTER WHEN FINISHED')
        content = []
        while True:
            con = input()
            if con == '':
                break
            content.append(con)
            content.append('\n')
        message = insert_to_file(file_name, content)
    elif select == "4":
        files, message = list_files()
        print(files.decode())
        file_name = get_file_name()
        message = read_file(file_name)
    elif select == "5":
        files, message = list_files()
        print(files.decode())
        file_name = get_file_name()
        message = manage_files(file_name, 'rm')
    else:
        print("not an option")
    print(message)
    input()

