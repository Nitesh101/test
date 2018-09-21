sub printlist{
	my @list = @_;
	print "given list is @list\n";
}
@a = (10,20,30);
@b = (1,2,3,4);
printlist(@a, @b);
