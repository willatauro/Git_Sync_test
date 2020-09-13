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
=end
=cut

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