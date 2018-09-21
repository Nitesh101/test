import zlib
str1 = "hello world!hello world!hello world!hello world!"
#val = zlib.compress(str1)
#print len(val)
val = zlib.decompress(str1)
print len(val)
