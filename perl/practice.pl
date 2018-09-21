my($a,$b);
print "Enter a vlaue: \n";
chomp($val = <>);
$a = 0;
$b = 1;
while($val>0){
	print "$a\n";
	$c = $a;
	$a = $b;
	$b = $c+$b;
	$val--;
}
