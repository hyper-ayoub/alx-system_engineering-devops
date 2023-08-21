#ifndef _MAIN_H_
#define _MAIN_H_
#include<stdio.h>
#include<stdlib.h>
#include<stdarg.h>
#include<limits.h>
int _putchar(char c);
void handle_ayoub(va_list, char specifier, int *counter);
int _printf(const char *format, ...);
int put_ayoub(const char *str);
int print_number(int n);
int  print_binary(unsigned int num);

#endif

