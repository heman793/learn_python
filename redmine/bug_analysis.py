# -*- coding: utf-8 -*-

from redminelib import Redmine

redmine = Redmine('http://www.redmine.org',username='heman793',password='123456')
project = redmine.project.get('Redmine')

print project.id


