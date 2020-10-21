import sys
from .classmodule import MyClass
from .funcmodule import gen_gitignore
from .funcmodule import print_random0

def help(cmd='all'):
    cmd_help = {}
    cmd_help['help'] = '$ pyfun help:'
    cmd_help['help'] += '\n\tpyfun help : show all commands'
    cmd_help['git'] = '$ pyfun git:'
    cmd_help['git'] += '\n\tpyfun git ignore : gen py gitignore'
    cmd_help['pycheat'] = '$ pyfun pycheat:'
    cmd_help['pycheat'] += '\n\tpyfun pycheat random : random num ex'


    if cmd == 'all':
        for command in cmd_help:
            print(cmd_help[command]+'\n')
    elif cmd_help.get(cmd, 0):
        print(cmd_help[cmd])
    else:
        print('help not availible for {}'.format(cmd))



def get_help():
    print('cmd not found\n$ pyfun help')

def handle_git(args):
    if len(args) == 0:
        help('git')
    elif len(args) == 1:
        if args[0] == 'ignore':
            gen_gitignore()
        else:
            get_help()   
    else:
        get_help()

def handle_pycheat(args):
    if len(args) == 0:
        help('pycheat')
    if len(args) == 1:
        if args[0] == 'random':
            print_random0()
        else:
            help('pycheat')

def handle_args(args):
    if len(args) == 0:
        help()
    elif len(args) >= 1:
        if args[0] == 'git':
            handle_git(args[1:])
        elif args[0] == 'pycheat':
            handle_pycheat(args[1:])
        elif args[0] == 'help':
            help()
        else:
            get_help()
    else:
        print('aparenltly there are negative #args')


def main():
    args = sys.argv[1:]
    
    handle_args(args)

if __name__ == '__main__':
    main()