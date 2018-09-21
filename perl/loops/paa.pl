my($a,$b);
print "Enter a item that is 7 characters\n";
chomp ($a = <>);
my @arr = split //, $a;
my $len = @arr;
print "$len\n";
$b = '';
while($len>=0)
{
  	$b=$b.$arr[$len];
	$len = $len-1;
}
print "reverse string: $b\n";
if ($a eq $b)
{
    print "THIS IS A PALINDROME!!! \n";
}
else
{
    print "THIS IS NOT A PALINDROME \n";
}
