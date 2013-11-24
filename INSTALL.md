INSTALLATION
============

This file contains instructions to setup a development version of the application.


Setting up virtualenv
---------------------

The recommended way to develop Python projects is to use virtual environments for each project.

Install virtualenvwrapper which will install virtualenv as well.

``` bash
$ pip install virtualenvwrapper
```

Add following to the shell's startup file(.zshrc, .bashrc, .profile, etc)

``` bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/directory-you-do-development-in
source /usr/local/bin/virtualenvwrapper.sh
```

Create a new virtual environment with any name.

``` bash
$ mkvirtualenv website
```

This command will create and switch to the virtual environment(the name of the environment will be prepended to the shell).
If not, run the following command to switch.

``` bash
$ workon website
```

Now let's install the required packages within this virtualenv.

``` bash
$ pip install -r requirements.txt
```

Note: drf-any-permissions will be installed from [txel's github](https://github.com/txels/drf-any-permissions) since current version
(0.0.1 as of writing) at PyPI doesn't provide what it advertises. It is good to check if an update has been made available that
fixes the issues before using the github repository. Ensure that git is installed before installing from github.


Specifying website settings
---------------------------

- Copy template local-settings.py to same directory where settings.py resides and rename it to local_settings.py.
- Set values for DATABASES and ADMINS. I recommend sqlite3 for testing but not production: easy to setup(just give path to database file).
- Generate the SECRET_KEY as per instructions in the local_settings.py file.
- You might want to set DEBUG = True for testing else set a value for ALLOWED_HOSTS if deploying in production.


Setting up the database
-----------------------

After specifying the settings, run the following commands to create the database.

``` bash
$ python manage.py syncdb --all
$ python manage.py migrate --fake
```

Create a superuser when prompted to do so. This user will be used to login to admin interface of the site.


Running the development server
---------------------------

If no errors are reported, the development server is ready. Run the server by issuing the command

``` bash
$ python manage.py runserver
```
