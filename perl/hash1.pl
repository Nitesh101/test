sub printhash{
	my (%hash) = @_;
	foreach my $key ( keys %hash){
		my $value = $hash{$key};
		print "$key";
	}
}
%hash
