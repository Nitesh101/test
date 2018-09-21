all:appstatic
appstatic: staticmain.o libmylib.a
	gcc -lm -o appstatic staticmain.o -I./static-lheader -L./static -lmylib
staticmain.o:staticmain.c 
	gcc -o -c staticmain.c  header.h 
fact.o:fact.c header.h
	gcc -o -c fact.c
fib.o:fib.c header.h
	gcc -o -c fib.c
prime.o:prime.c header.h
	gcc -o -c prime.c
libmylib.a:fact.o fib.o prime.o
	ar rcs libmylib.a fact.o fib.o prime.o
libs: libmylib.a
clean:
	rm -rf *.o.a*gch

