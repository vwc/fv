Introduction
============

This is a blueprint buildout to kickstart new Plone CMS projects.

This buildout should not be used directly, but is best downloaded
and cloned to a new and dedicated project repository. When in doubt you can
always return to the blueprint/boilerplate buildout for enhancements and
inspiration concerning the latest "best practice" of ade25 Plone
development and buildout scaffolding in general.


Buildout
--------

This buildout is intended to be used via the development profile to provide
a ready to work on setup:

``` bash
$ virtualenv-2.7 my_project
$ cd ./my_project
$ git clone gitlgithub.com:username/my_project.git buildout.my_project
$ cd ./buildout.my_project
$ python bootstrap.py -c development.cfg
$ bin/buildout -Nc development.cfg
```

Diazo Theme development
=======================

The current version of this buildout already includes a Diazo theme packaged
to be used via *plone.app.theming* located in the '${buildout:directory}/src'
directory and initialized via *mr.developer*. Just rename it and you should
be done.

In order to add a theme resource directory checkout the yeoman diazotheme
generator.
