sub printhash{
	my (%hash) = @_;
	foreach $keys (keys %hash){
		my $value = $hash{$key};
		print "$key\n";
	}
}

