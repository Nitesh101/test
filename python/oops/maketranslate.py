from string import maketrans
inpu = "aeiou"
outp = "12345"
tran = maketrans(inpu,outp)
str = "this is string example "
print str.translate(tran)
