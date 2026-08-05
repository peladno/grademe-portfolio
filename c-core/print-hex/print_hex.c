#include <unistd.h>

void prnt_word(char *str){
	while(*str){
		write(1, str, 1);
		str++;
	}
}

void print_hex(unsigned int num){
    char *base = "0123456789abcdef";

    if (num >= 16)
    {
        print_hex(num / 16);
    }
    write(1, &base[num % 16], 1);
    
}

unsigned int    ft_atoi(const char *s)
{
    unsigned int n = 0;

    while (*s >= '0' && *s <= '9')
    {
        n = n * 10 + (*s - '0');
        s++;
    }
    return n;
}



int	main(int argc, char **argv)
{
	if(argc != 2){
		prnt_word("wrong number of arguments");
		write(1,"\n",1);
		return (0);
	}

	unsigned int numb = ft_atoi(argv[1]);

	print_hex(numb);
	write(1,"\n",1);

	return (0);
}
