"""
import re
s = "2 cats and 3 dogs."
print re.findall("\d",s)

s = raw_input()
u = unicode( s ,"utf-8")
print u

import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print t
print zlib.decompress(t)

from timeit import Timer
t = Timer("for i in range(100):1+1")
print t.timeit()

from random import shuffle
li = [3,6,7,8]
shuffle(li)
print li

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
print sentence
"""
import itertools
print list(itertools.permutations([1,2,3]))
