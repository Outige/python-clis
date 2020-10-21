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
        # ignore = open('static/.gitignore_py', 'r').read()
        ignore = '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/'''
        fp.write(ignore)
        fp.close()

def print_random0():
    # print(open('random0.py', 'r').read())
    random_str = '''import random

def random_random():
    # returns: float[0, 1)
    val = random.random()
    print(val)

def random_uniform():
    #returns: float[1, 5] - not too sure about inclusivity
    val = random.uniform(1, 5)
    print(val)


def random_choice():
    vals = [3,6,7,8,3]
    value = random.choice(vals)
    print(value)

def random_int():
    # returns: int[0, 9]
    val = random.randint(0, 9)
    print(val)

if __name__ == '__main__':
    random_random()
    random_uniform()
    random_choice()
    random_int()'''
    print(random_str)

def gen_flask_hello_world():
    wsgi_str = '''from app.main import app 

if __name__ == "__main__": 
    app.run(debug=True)'''
    open('wsgi.py', 'w').write(wsgi_str)

    requirements_str = '''appdirs==1.4.3
CacheControl==0.12.6
certifi==2019.11.28
chardet==3.0.4
click==7.1.2
colorama==0.4.3
contextlib2==0.6.0
distlib==0.3.0
distro==1.4.0
Flask==1.1.2
html5lib==1.0.1
idna==2.8
ipaddr==2.2.0
itsdangerous==1.1.0
Jinja2==2.11.2
lockfile==0.12.2
MarkupSafe==1.1.1
msgpack==0.6.2
packaging==20.3
pep517==0.8.2
progress==1.5
pyparsing==2.4.6
pytoml==0.1.21
requests==2.22.0
retrying==1.3.3
six==1.14.0
urllib3==1.25.8
webencodings==0.5.1
Werkzeug==1.0.1'''
    open('requirements.txt', 'w').write(requirements_str)
    open('req_cmd.txt', 'w').write('pip install flask')

    # app level
    os.mkdir('app')
    main_str = '''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return render_template('index.html', title='Home page')

if __name__ == "__main__":
    app.run(debug=True)'''
    open('app/main.py', 'w').write(main_str)

    os.mkdir('app/templates')

    base_str = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% block head %}{% endblock %}
</head>
<body>
    {% block body %}{% endblock %}
</body>
</html>'''
    index_str = '''{% extends 'base.html' %}

{% block head %}
<title>{{ title }}</title>
{% endblock%}

{% block body %}
<h1>Hello world!</h1>
{% endblock%}'''
    open('app/templates/base.html', 'w').write(base_str)
    open('app/templates/index.html', 'w').write(index_str)

    os.mkdir('app/static')