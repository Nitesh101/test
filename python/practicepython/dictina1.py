d = {0:10, 1:20}
print d
d.update({2:30})
print d
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1,dic2,dic3): dic4.update(d)
print dic4
import os
val2 = os.getcwd()
val=os.listdir(val2)
print val
