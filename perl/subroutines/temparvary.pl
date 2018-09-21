$string = "Hello World";
sub printhello{
	local $string;
	$string = "Hello Perl";
	printme();
	print "Inside the function: $string\n";
}
sub printme(){
	print "Inside the function: $string\n";
}
printhello();
print "outside the function: $string\n";
