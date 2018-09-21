use feature ":5.10";
use strict;
use warnings;
my @array = (1,2,1,2,34,3,4,3);
my %hash;
@hash(@array) = ();
@array = keys(%hash);
say "@array";

