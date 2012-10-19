PROJECTNAME = 'projectfoo'
APPNAME = 'appnamebar'
REMOTE = 'origin'
USER = 'username'
HOMEDIR = '/home/%s' % USER
CODEDIR = '%s/webapps/%s/%s/' % (HOMEDIR, PROJECTNAME, APPNAME)
VIRTUALENV = '%s/webapps/%s/env/' % (HOMEDIR, PROJECTNAME)
