=begin
#$r =12.5;
$r = <STDIN>;

if ($r<0)
{   $A=0;
    print($A);
}else
{
    $A = 2*3.141592654*$r;
}
print($A)
=end
=cut

$a = <STDIN>;
$b = <STDIN>;
#$c= $a*$b;
while($b>0)
{
    print($a);
    $b= $b-1;
}
#print($c);