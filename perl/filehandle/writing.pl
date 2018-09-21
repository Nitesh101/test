$name = "nitesh";
@value = (2,2,3,4,18);
%hash = ('name',10,'id',100);
open(DATA, ">val2.txt");
print DATA"$name\n";
print DATA @value;
print DATA %hash;
close(DATA);
