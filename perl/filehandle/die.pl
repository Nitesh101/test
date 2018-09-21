open(DATA, "<te.txt") || die "con't open file ";
while(<DATA>){
	print DATA"$_";
}
close(DATA);
