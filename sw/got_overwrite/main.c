#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

unsigned long long parse_address() {
    unsigned long long address = 0;
    
    unsigned int parsed = scanf("%llu", &address);

    if (parsed != 1) {
        puts("Error");
        exit(-1);
    }

    return address;
}

int main () {
    setvbuf(stdout, NULL, _IONBF, 0);
    
    char reason[32] = {0};

    puts("[ * ] Memory inspector");
    printf("Edit reason: ");
    
    scanf("%31s", reason);

    printf("Input the address to inspect: ");
    unsigned long long address_to_read = parse_address();

    printf("Content of %llu: %llu\n", (unsigned long long)address_to_read, *((unsigned long long*)address_to_read)); 

    printf("Input the address to modify: ");
    unsigned long long address_to_write = parse_address();
    
    printf("Input the value to write: ");

    unsigned int parsed = scanf("%llu", (unsigned long long*)address_to_write);
	
    if (parsed != 1) {
        puts("Error");
        exit(-1);
    }

    puts(reason);
}
