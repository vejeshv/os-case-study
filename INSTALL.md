INSTALLATION
============

This file contains instructions to setup a development version of the application.


Setting up virtualenv
---------------------

The recommended way to develop Python projects is to use virtual environments for each project.

Install virtualenvwrapper which will install virtualenv as well.

$ pip install virtualenvwrapper

Add following to the shell's startup file(.zshrc, .bashrc, .profile, etc)

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/directory-you-do-development-in
source /usr/local/bin/virtualenvwrapper.sh

Create a new virtual environment with any name.

$ mkvirtualenv website

This command will create and switch to the virtual environment(the name of the environment will be prepended to the shell).
If not, run the following command to switch.

$ workon website

Now let's install the required packages within this virtualenv.

$ pip install -r requirements.txt

Note: drf-any-permissions will be installed from [txel's github](https://github.com/txels/drf-any-permissions) since current version
(0.0.1 as of writing) at PyPI doesn't provide what it advertises. It is good to check if an update has been made available that
fixes the issues before using the github repository. Ensure that git is installed before installing from github.


Specifying website settings
---------------------------

Modify the template locate-settings.py file and copy it to the location specified inside the file. In particular, set the
values for SECRET_KEY, DATABASES and ADMINS.


Setting up the database
-----------------------

After specifying the settings, run the following commands to create the database.

$ python manage.py syncdb --all

$ python manage.py migrate --fake

Create a superuser when prompted to do so. This user will be used to login to admin interface of the site.


Running the development server
---------------------------

If no errors are reported, the development server is ready. Run python manage.py runserver to start it.
