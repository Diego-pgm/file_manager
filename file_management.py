"""A program to update files"""
import os
import subprocess

def cust_menu(opts):
    hor = '#dr' * 10
    u = '#dr'
    header = '{} file updater {}\n'.format(hor,hor)
    body = ''
    for key, value in opts.items():
        body = body + '{}) {}\n'.format(key, value)
    menu = header + body
    return menu

def create_file(file_name):
    subprocess.call(['touch', file_name])
    return 'File created!'

opts = {"1":"create file", "2":"insert to file", "3":"delete file", "4":"exit"}
message = 'This is the default message'
while True:
    os.system('clear')
    menu = cust_menu(opts)
    print(menu)
    select = input("Select>> ")
    if select == "4":
        print('bye bye')
        quit()
    elif select == "1":
        file_name = input('Insert the file name>> ')
        message = create_file(file_name)
    elif select == "2":
        print("insert to file")
    elif select == "3":
        print("delete file")
    else:
        print("not an option")
    print(message)
    input()

