my $str = 'ashish pethkar';
my @arr = split //, $str;
my $len = @arr;
my $rev = '';
while ($len>=0)
{
     $rev.=$arr[$len];
     $len--;
}
print "\n\n$rev\n\n";
