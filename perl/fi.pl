open(FILEHANDEL,"<file.txt");
while(defined($char = getc FILEHANDEL)){
	print "$char\n";
}
close FILEHANDEL;
