import sys
from colorama import Fore, Style

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
NC = Style.RESET_ALL

def print_fatal(*text):
    str = "[{r}error{nc}] ".format(r=RED, nc=NC)
    for t in text:
        str += t

    print(str) # rest api connection here
    sys.exit(1)
