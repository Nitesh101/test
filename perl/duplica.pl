my @test_array = qw/ 1 2 3 4 5 6 1 2 3 4 5 6 7/;
my %temp = map{$_, 0}@test_array;
print %temp;
