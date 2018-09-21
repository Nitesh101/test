use feature 'state';
sub printcount{
	state $count = 0;
	print "value of count is $count\n";
	$count++;
}
for(1..5){
	printcount();
}
