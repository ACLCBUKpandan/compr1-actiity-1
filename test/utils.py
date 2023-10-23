from colorama import Back, Fore, Style


def reset():
    print(Style.RESET_ALL)



def info(text):
    print(Fore.CYAN + text)

def err(text):
    print(Fore.BLACK + Back.RED + text)
    reset()

def warn(text):
    print(Fore.YELLOW + text)

def success(text):
    print(Back.GREEN + Fore.BLACK + text)
    reset()
