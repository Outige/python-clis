import sys
from .classmodule import MyClass
from .funcmodule import gen_gitignore
from .funcmodule import print_random0

def help(cmd='all'):
    if cmd == 'all':
        print('pyfun help:')
        print('\tpyfun help')

        print('\npyfun git:')
        print('\tpyfun git ignore')
    elif cmd == 'pycheat':
        print('$ pyfun pycheat:')
        print('\tpyfun pycheat random')
    else:
        print('help not availible for {}'.format(cmd))



def get_help():
    print('cmd not found\npyfun help')

def handle_git(args):
    if len(args) == 2:
        if args[1] == 'ignore':
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
        get_help()
    elif len(args) >= 1:
        if args[0] == 'git':
            handle_git(args)
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