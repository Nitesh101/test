open(DATA1, "<reslt.txt");
open(DATA2, ">file.txt");
while(<DATA1>){
	print "DATA2 $_";
}
close(DATA1);
close(DATA2);
