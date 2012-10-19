from fabric.api import *  # NOQA
from fabsettings import (PROJECTNAME, APPNAME, REMOTE, USER, HOMEDIR,
                        CODEDIR, VIRTUALENV)

env.projectname = PROJECTNAME
env.appname = APPNAME
env.remote = REMOTE
env.user = USER
env.home = HOMEDIR
env.codedir = CODEDIR
env.venv = VIRTUALENV


def deploy(branch='master'):
    local('git pull %s %s' % (env.remote, branch))
    checkout(branch, 'rsync -auv * %s' % env.codedir)

    with lcd(env.codedir):
        local('pip install -r requirements/production.txt')
        virtualenv('./manage.py collectstatic')
    local('%s/webapps/%s/bin/restart' % (env.home, env.projectname))


def virtualenv(command):
    local('pwd && source %sbin/activate && %s' % (env.venv, command))


def checkout(branch, command):
    local('git checkout %s && %s' % (branch, command))
