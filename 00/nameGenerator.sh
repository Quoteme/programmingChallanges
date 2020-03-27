#!/usr/bin/env bash
#
# @AUTHOR: Luca Leon Happel
# @DATE  : 2020-03-26 Do 04:43
#
# Return a random name
#

nthline() {
	tail -n+$1 $2 | head -n1
}

randomlinenumber() {
	shuf -i 1-$(wc -l < $1) -n 1
}

randomline() {
	nthline $(randomlinenumber $1) $1
}

FAMILYNAME=$(randomline ./names/NAMES.TXT)
test $((1 + $RANDOM % 2)) -eq 1 \
	&& GENDER='M' \
	|| GENDER='F'

test $GENDER = "M" \
	&& FIRSTNAME=$(randomline ./names/NAMES-M.TXT) \
	|| FIRSTNAME=$(randomline ./names/NAMES-F.TXT)

echo $FIRSTNAME
echo $FAMILYNAME
echo $GENDER
