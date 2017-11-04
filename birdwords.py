#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:49:56 2017

@author: melissa
"""

from random import randint


adjectives = ['fragile','powerful','subtle','ethereal','ephemeral','piercing']
nouns = ['eternity','universe','flower','soul','child','girl','magic']

adjpick = adjectives[randint(0,len(adjectives)-1)]
nounpick = nouns[randint(0,len(nouns)-1)]



if adjpick[:1] in ('a','e','i','o','u'):
    particle = 'an'
else:
    particle = 'a'
print particle + ' ' + adjpick + ' ' + nounpick