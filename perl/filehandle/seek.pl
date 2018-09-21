open(DATA, "<val.txt");
seek DATA, 10,0;
while(<DATA>)
{
	print;
}
close(DATA);
