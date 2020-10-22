Welcome to pyfun (python_functions) cli. This tool is being designed as a shortcut system for all pythony help that I find myself routenly looking for on the internet.

# install - linux based
This is a sumamry of the commands required (assuming you have git, python & virtualenv)
```
$ git clone git@github.com:Outige/tutorial-python.git
$ cd tutorial-python/pyfun
$ virtualenv env
$ source env/bin/active
$ ./install.sh
```

If you didn't understand the above commands here is a more indepth explanation.

Clone the repo(or downlaod the zip):
```
$ git clone git@github.com:Outige/tutorial-python.git
```

Navigate to the `tutorial-python/pyfun` directory. Here you will find `install.sh` containing the follwoing commands: **I would recomend using virtualenv/pipenv to install the module, because I don't know what O'm doing and you don't want to break your python install**
```
uninstall pyfun
pip3 install -e 
```

The first line is to uninstall the module from your python. The second line installs the current directory as a python module. Not the **-e**. I haven't confirmed this but I believe that means you can edit the module without the need to uninstall and reinstall the package (basically for development of the package).

Now all you need to do is set up your virtualenv(optional but recomended) and run the install script (or the commands seperately):
```
$ virtualenv env
$ source env/bin/active
$ ./install.sh
```

# using the cli
To engague the cli all you need to do is type `pyfun` into your terminal. Think of this like any other cli. `git` for example. You would type `git <some cmd> .... <some cmd>`.

To get started type `pyfun` and press enter. This will show the `help page` displaying all the commands.

If this page is too busy you can type a more specific command like `pyfun pycheat`, which will bring up all the options for `pyfun pycheat` - like `pyfun pycheat random`

---

### references
* [python cli article](https://trstringer.com/easy-and-nice-python-cli/)
* [random numbers video](https://www.youtube.com/watch?v=KzqSDvzOFNA)
* [flask session](https://www.youtube.com/watch?v=iIhAfX4iek0&t=533s)