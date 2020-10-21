import sys
from .classmodule import MyClass
from .funcmodule import gen_gitignore

def help():
    print('pyfun help:')
    print('\tpyfun help')

    print('\npyfun git:')
    print('\tpyfun git ignore')



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

def handle_args(args):
    if len(args) == 0:
        get_help()
    elif len(args) >= 1:
        if args[0] == 'git':
            handle_git(args)
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