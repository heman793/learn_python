# -*- coding: utf-8 -*-

from redminelib import Redmine

redmine = Redmine('http://www.redmine.org',username='heman793',password='123456')
project = redmine.project.get('Redmine')

print "project id:",project.id

print "project identifier:",project.identifier

print "project created on:",project.created_on

print "project issues number 202 subject:",project.issues[202].subject



