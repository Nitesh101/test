$str = "my name is ABCD";
print "$str\n";
@str = split //,$str;
$len = @str;
print "string is: @str\n";
$j = 0;
for($i=$len;$i>0;$i--)
{
	$red[$j] = $str[i];
	$j++;
}
$str = join(@res, " ");
print "revesre order is \n",$str
