#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

char ror(int c, int counter){
  uint in_EAX;
  
  while (counter = counter + -1, -1 < counter) {
    in_EAX = (c & 1U) << 7 | c >> 1 & 0x7fU;
    c = in_EAX;
  }
  return (char)in_EAX;
}

char reverse_ror(int c, int counter){
  uint in_EAX;
  
  while (counter = counter + -1, -1 < counter) {
    in_EAX = ((c >> 7) & 1U) | ((c & 0x7fU) << 1);
    c = in_EAX;
  }
  return (char)in_EAX;
}

char* encrypt(char * input_file, int output_file){
  int bytes_read;
  int bytes_written;
  char* encrypted_char;
  char* buffer;
  char prev;

  int counter = 0;
  do {
    bytes_read = read((int)input_file,buffer,16);
    if ((int)bytes_read < 1) {
      return 1;
    }
    for (int i = 0; i < (int)bytes_read; i = i + 1) {
      counter = counter + 1;
      encrypted_char = ror((int)buffer[i],counter);
      prev = buffer[i];
      buffer[i] = encrypted_char;
      printf("CALLED EN, %c -> buffer[%i] = %c\n", prev, i, buffer[i]);
    }
    bytes_written = write(output_file,buffer,bytes_read);
  } while (bytes_read == bytes_written);
  return NULL;
}

char* decrypt(char * input_file, int output_file){
  int bytes_read;
  int bytes_written;
  char encrypted_char;
  char* buffer;
  char prev;

  int counter = 0;
  do {
    bytes_read = read((int)input_file,buffer,16);
    if ((int)bytes_read < 1) {
      return 1;
    }
    for (int i = 0; i < (int)bytes_read; i = i + 1) {
      counter = counter + 1;
      prev = buffer[i];
      encrypted_char = reverse_ror((int)buffer[i],counter);
      buffer[i] = encrypted_char;
      printf("%c = %u is %u\n", prev, (uint) prev, (uint) buffer[i]); 
    }
    bytes_written = write(output_file,buffer,bytes_read);
  } while (bytes_read == bytes_written);
  return NULL;
}

int main(int argn, char** args){
  if(argn != 4) exit(1); 

  size_t key_length;
  ushort **ppuVar1;
  char *input_file;
  int output_file;
  char *key;
  char *output_file_name;

  if (argn == 4) {
    key = args[1];
    key_length = strlen(key);
      output_file_name = args[3];
      input_file = (char *)open(args[2],0);
      if ((int)input_file < 0) {
        perror("input file");
      }
      else {
        output_file = open(output_file_name,0xc1,0x180);
        if (-1 < output_file) {
          decrypt(input_file,output_file);
          close((int)input_file);
          close(output_file);
          puts("File successfully decrypted.");
          return 0;
        }
        perror("output file");
      }
  }
  else {
    fprintf(stderr,"Usage: %s key input-file output-file\n",*args);
  }

  return 0;
}
