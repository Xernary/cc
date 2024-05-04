/*
 * Authors:
 * + Andrea Fioraldi <andreafioraldi@gmail.com>
 * + Pietro Borrello <pietro.borrello95@gmail.com>
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main()
{
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
	
	char cmd[32];
	
	while(1) {
		printf("Choose one:\n");
		printf(" --> Pepsi\n");
		printf(" --> Coca Cola\n");
		printf(" >> ");
	
		read(STDIN_FILENO, cmd, 0x320);
	
		if(strncmp(cmd, "Coca Cola", 9) == 0) {
			printf("Ahahahahaha Beer >>> Coca Cola\n");
		}
		else if(strncmp(cmd, "Pepsi", 5) == 0) {
			printf("Ahahahahaha Beer >>> Pepsi\n");
		}
		else if(strncmp(cmd, "Beer", 4) == 0) {
			printf("THIS is the answer, simply %s\n", cmd);
		}
		else {
			printf("Are u drunk?\n");
			return 1;
		}
	}
}
