open(DATA,"<reslt.txt");
while(<DATA>){
	print "$_";
}
close(DATA);
