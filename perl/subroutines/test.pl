$string = "Hello World";
sub printhello{
	local $string;
	$string = "Hello Perl";
	printme();
	print "Inside function : $string\n";
}
sub printme{
	print "Inside funcrion: $string\n";
}
printhello();
print "outside function: $string\n";
