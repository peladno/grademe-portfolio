#include <unistd.h>

int	putchar(int c)
{
	(void)c;
	unsigned char chr = c;
	write(1, &chr, 1);
	return chr;
}
