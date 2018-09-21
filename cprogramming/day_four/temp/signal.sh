#!/bin/bash
trap test_handler USR1
trap int_handler INT
trap usr_handler USR2
test_handler()
{
	echo "find proces id"
}
int_handler()
{
        echo "cought signal"
       
}
usr_handler()
{
	echo "got a signal"
}
while [ true ]
do 
	ps -f
	sleep 5
done


