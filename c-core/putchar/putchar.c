#include <unistd.h>

int	gm_putchar(int c)
{
	(void)c;
	unsigned char chr = c;
	write(1, &chr, 1);
	return chr;
}
