sub printhash{
	my (%hash) = @_;
	foreach my $key (values %hash){
		my $value = $hash{$key};
		print "$key\n";
	}
}
%hash = ('name' => 'Tom', 'age'=> 19);
printhash(%hash);
