#include "main.h"

/**
 * put_ayoub - it's a function that print a string
 * @str: ayoub
 * Return: i
 */

int put_ayoub(const char *str)
{
    int i = 0;

    if (str == NULL)
    {
        put_ayoub("(null)"); 
        return 6;
    }

    while (str[i] != '\0')
    {
        _putchar(str[i]);
        i++;
    }

    return i;
}
