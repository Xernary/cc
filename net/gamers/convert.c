#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFF_SIZE 20000
#define COMMANDS 600

const char* const TEMPLATE = "0,1,12,";

char** convert(char* const buff){

  char** res = malloc(sizeof(char*) * COMMANDS);
  int res_count = 0;

  for(int i = 0; i < COMMANDS; i++)
    res[i] = malloc(sizeof(char) * 20);


  for(int i = 0; i < strlen(buff)-10; i++){

    if(buff[i] != '[') continue;

    char tmp[8];
    strncpy(tmp, &buff[i+1], 7);
    if(strcmp(tmp, TEMPLATE) != 0) continue;

    //copy the coordinates until ']' is encountered
    char c = buff[i+8];
    int counter = 0;
    while(c != ']'){
      if(c == ',') c = ' ';
      strncat(res[res_count], &c, 1);
      counter++; 
      c = buff[i+8+counter];
    }
    res[res_count][counter] = '\0';
    res_count++;
  }

  return res;
}

int main(){

  FILE* fd = fopen("commands", "r");
  char* buff = malloc(sizeof(char) * BUFF_SIZE);

  while(fgets(buff, BUFF_SIZE, fd)) {
    //printf("%s", buff);
  }

  // convert text
  char** converted = convert(buff);

  for(int i = 0; i < COMMANDS; i++)
    printf("%s\n", converted[i]);

  for(int i = 0; i < COMMANDS; i++)
    free(converted[i]);
  free(converted);

  free(buff);
  fclose(fd);

  return 0;
}
