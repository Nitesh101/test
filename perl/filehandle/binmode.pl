open(DATA, ">test.txt");
binmode DATA, :crlf;
print "Hello there, alies from Earth\n";
close(DATA);
