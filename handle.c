#include "main.h"
/**
 * handle_ayoub - handles different specifiers
 * @i: the counter
 * @specifier: the specifier
 * @arg: argument
 */
void handle_ayoub(va_list arg1, char specifier, int *i)
{
	switch (specifier)
	{
		case 'c':
				(*i) += _putchar(va_arg(arg1, int));
				break;
		case 's':
				(*i) += put_ayoub(va_arg(arg1, char *));
				break;
		case '%':
				(*i) += _putchar('%');
				break;
		
		
			
		default:
				_putchar('%');
				_putchar(specifier);
				(*i) += 2;
				break;
	}
}




