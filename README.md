webfaction-django-fabric
========================

Fabric deployment script which i use on webfaction.

## Description
Basically consists of:
* pulling the code
* activating branch(just call 'fab deploy' for master)
* installing requirements
* manage.py collectstatic
* restart

## Installation
copy to project root folder, change the variables in fabsettings.py

## Deployment
    fab deploy:<branch>

