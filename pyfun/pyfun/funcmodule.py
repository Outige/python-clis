import os

def my_function(text_to_display):
    print('text from my_function :: {}'.format(text_to_display))

def  gen_gitignore():
    if os.path.isfile('.gitignore'):
        print('.gitignore alread exists. Do you want to overwrite it?(y/n)')
        a = input()
        if a.lower() != 'y' and a.lower() != 'yes':
            print('aborted')
            return

    with open('.gitignore', 'w') as fp:
        ignore = open('static/.gitignore_py', 'r').read()
        fp.write(ignore)
        fp.close()

def print_random0():
    print(open('static/random0.py', 'r').read())