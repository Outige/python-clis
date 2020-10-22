import os
import pyfun

def  gen_gitignore():
    if os.path.isfile('.gitignore'):
        print('.gitignore alread exists. Do you want to overwrite it?(y/n)')
        a = input()
        if a.lower() != 'y' and a.lower() != 'yes':
            print('aborted')
            return

    path = pyfun.__file__.replace('__init__.py', '') + 'static/git/'
    open('.gitignore', 'w').write(open(path+'gitignore_py', 'r').read())

def print_random0():
    path = pyfun.__file__.replace('__init__.py', '')
    print(open(path+'static/pycheat/random0.py', 'r').read())

def gen_flask_hello_world():
    path = pyfun.__file__.replace('__init__.py', '') + 'static/flask/hello_world/'

    open('wsgi.py', 'w').write(open(path+'wsgi.py', 'r').read())
    open('requirements.txt', 'w').write(open(path+'requirements.txt', 'r').read())

    os.mkdir('app')
    open('app/main.py', 'w').write(open(path+'app/main.py', 'r').read())

    os.mkdir('app/templates')
    open('app/templates/base.html', 'w').write(open(path+'app/templates/base.html', 'r').read())
    open('app/templates/index.html', 'w').write(open(path+'app/templates/index.html', 'r').read())

    os.mkdir('app/static')

def gen_flask_hello_world_heroku():
    gen_flask_hello_world()
    path = pyfun.__file__.replace('__init__.py', '') + 'static/flask/hello_world_heroku/'
    
    open('Procfile', 'w').write(open(path+'Procfile', 'r').read())
    open('requirements.txt', 'w').write(open(path+'requirements.txt', 'r').read())

    print('warning this method hasn\'t been proven to work yet')