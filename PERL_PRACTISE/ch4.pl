=begin
sub total
{
    my $sum=0;
    foreach (@_)
    {
        $sum=$sum + $_ ;

    }$sum 
}
my @fred =qw{1 3 5 7 9};
my $fred_total =&total (@fred);
print($fred_total);


sub total
{
    my $sum=0;
    foreach (@_)
    {
        $sum=$sum + $_ ;

    }$sum 
}
my @fred =(1..1000);
my $fred_total =&total (@fred);
print($fred_total);
=end
=cut