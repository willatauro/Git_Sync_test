=Begin
$_ ="yabba dabba abba";
#if(/ab ba/)
if(//)
{
    print "it matched";
}
else 
{
    print "not matched";
}


while(<STDIN>)
{
    chomp;
    if(/$ARGV[0]/)
    {
        print "it matched";
    }
    else 
    {
        print "not matched"
    }
}



$_ ="abba";
if(/(.)\1/)
{
    print "it matched"
}


$_ ="yabba dabba doo";
if(/y(.)(.)\2\1/)
{
    print "it matched"
}
=end
=cut

$_ ="yabba dabba doo";
if(/y((.)(.)\3\2) d\1/)
{
    print "it matched"
}