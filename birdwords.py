"""
Created on Tue Apr 11 21:49:56 2017

@author: melissa
"""

from random import randint


adjectives = ['fragile','powerful','subtle','ethereal','ephemeral','piercing']
nouns = ['eternity','universe','flower','soul','child','girl','magic','man',
            'woman','spark','sun']
verbs = ['fights','loves','strikes','dances with','embraces','touches']
pronouns = ['he','she','they','it']

adjpick = adjectives[randint(0,len(adjectives)-1)]
nounpick = nouns[randint(0,len(nouns)-1)]
verbpick = verbs[randint(0,len(verbs)-1)]

def pick(list, a):
    w = list[randint(0,len(list)-1)]
    particle = ''
    if a:
        if w[:1] in ('a','e','i','o','u'):
            particle = 'an'
        else:
            particle = 'a'
    return particle + w

print 'the %s %s %s %s %s' % (pick(nouns), pick(verbs), pick(adjectives,True), pick(nouns))
