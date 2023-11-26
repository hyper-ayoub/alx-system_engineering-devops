#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite while loop
 *
 * Return: No value
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create 5 zombies
 *
 * Return: 0
 */
int main(void)
{
	for (int i = 0; i < 5; ++i)
	{
		if (fork() == 0)
		{
			printf("Child process %d created.\n", getpid());
			exit(0);
		}
	}

	sleep(10);
	printf("Parent process %d exiting.\n", getpid());

	return (0);
}

