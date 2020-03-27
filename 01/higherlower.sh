#!/usr/bin/env bash
#
# @AUTHOR: Luca Leon Happel
# @DATE  : 2020-03-27 Fr 12:38
#
# Enter a maximum number as the commandline argument
#

test -z $1 \
	&& RAND=`shuf -i 1-10000 -n 1` \
	|| RAND=`shuf -i 1-$1 -n 1`

echo "A random number has been generated!"
echo "Please enter a guess"

read INPUT

while $( test "$RAND" != "$INPUT" )
do
	test "$INPUT" -le "$RAND" \
		&& echo "Your number was too small." \
		|| echo "Your number was too big."
	echo "Enter a new number"
	read INPUT
done
echo "Congratulations! Your guess was correct:"
echo $RAND
