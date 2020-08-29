=begin
@line = <STDIN>;
@lines = reverse @line;
print(@lines)


@names = qw (dino betty matt bob jim);
print "Enter input numbers 1-4 to get @names\n enter ^z to end input";
@number = <STDIN>;
foreach $number (@number)
{
    print($names[$number]);
}
=end
=cut

@names = <STDIN>;

print(sort @names);
