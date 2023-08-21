#include "main.h"
/**
 * _printf - produces output according to a format
 * @ayoub:
 * @...:
 * Return: i
 */
int _printf(const char *ayoub, ...)
{
	int i = 0;
	va_list arg1;

	va_start(arg1, ayoub);

	if (!ayoub || (ayoub[0] == '%' && !ayoub[1]))
	{
		return (-1);
	}
	if (ayoub[0] == '%' && ayoub[1] == ' ' && !ayoub[2])
	{
		return (-1);
	}
	while (*ayoub)
	{
		if (*ayoub == '%')
		{
			ayoub++;
			handle_ayoub(arg1, *ayoub, &i);
		}
		else
		{
			_putchar(*ayoub);
			i++;
		}
		ayoub++;
	}
	va_end(arg1);
	return (i);
}

