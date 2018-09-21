#$site = 'JavaTpoint';
#print "Welcome to $site\n";
#$site = 'javaTpoint';
#print 'welcome to $site\n';
@coins = ("quarter","Dime","Nickel");
#print "@coins\n";
#push(@coins, "penny");
#print "@coins\n"
unshift(@coins,"Dollar");
print "@coins\n";
pop(@coins);
print "@coins\n"
