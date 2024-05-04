// gcc -fno-stack-protector -m32 -mpreferred-stack-boundary=2 -no-pie -o challenge main.c
#include <stdio.h>



int main () {
	char buff[64];

	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	

	puts("Hello frienddddddddddddd. How are you?");
	scanf("%s", buff);
	
	return 0;
}
