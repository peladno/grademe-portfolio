#include <unistd.h>

int	main(int argc, char **argv)
{
	(void)argc;
	(void)argv;

	char c = 'a';
	while(c >= 'a' && c <= 'z'){

		char out = c;
		if(out % 2 == 0){
			out = c - 32;
		}
		write(1,&out,1);
		write(1,&out,1);
		c++;
	}
	write(1, "\n", 1);

	return (0);
}
