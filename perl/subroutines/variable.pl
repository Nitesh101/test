$string = "Hello World";
sub printhello{
	my $string;
	$string = "Hello Perl";
	print "Inside the function: $string\n";
}
printhello();
print "Outside the function: $string\n";
