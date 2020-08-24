#print "hello world \n"


@lines = `perldoc -u -f atan2`;
foreach (@lines){
    s/\w<([^>]+)>/\U$1/g;
    print;
}
print -10%3

#29