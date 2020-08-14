#!/usr/bin/bash
# starting shell scripting today --- this is comments 

<<COMMENT
echo "Hello World"
echo $BASH
echo bash version is  $BASH_VERSION
echo our home directory is $HOME
echo our preent directory is  $PWD
name=Wilander # No space 
echo The name is $name 
echo enter name
read name
echo entered name $name '


read -p 'username :' user_Var
read -sp 'username :' user_pwd
echo "username :" $user_Var 
echo "username :" $user_pwd


echo "Enter names: "
read -a names
echo "Names: " ${names[0]}, ${names[1]}


#pass arguments

echo $0 $1 $2 $3 


args=("$@")  #pass arguments as array
echo ${args[0]} ${args[1]} ${args[2]} # to print array, 0 location is not for script here
echo $@ # to print all elements of array
echo $# # to print the number of elements in an array
COMMENT

 
