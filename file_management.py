"""A program to update files"""
import os

def cust_menu(*args, **kwargs):
    hor = '#dr' * 10
    u = '#dr'
    header = '{} file updater {}\n'.format(hor,hor)
    body = ''
    for key, value in opts.items():
        body = body + '{}) {}\n'.format(key, value)
    menu = header + body
    return menu


opts = {"1":"create file", "2":"insert to file", "3":"delete file", "4":"exit"}
while True:
    os.system('clear')
    menu = cust_menu(opts)
    print(menu)
    select = input("Select>> ")
    if select == "4":
        print('bye bye')
        quit()
    elif select == "1":
        print("create file")
        input()
    elif select == "2":
        print("insert to file")
        input()
    elif select == "3":
        print("delete file")
        input()
    else:
        print("not an option")
        input()

