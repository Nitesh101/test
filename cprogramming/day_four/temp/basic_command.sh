#!/bin/bash
a=0
while [ $a -lt 10 ]
do
	echo "hello"
	sleep 1
	a=$(( a+1 ))
done

