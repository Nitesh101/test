open(DATA, "<reslt.txt");
while(defined($char = getc DATA)){
	print $char;
}
close DATA;
