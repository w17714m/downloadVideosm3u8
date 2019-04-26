from colorama import init,Fore,Back,Style
import os

if os.name == "posix":

    init(autoreset=True)
    # primer plano
    fc = "\033[0;96m"
    fg = "\033[0;92m"
    fw = "\033[0;97m"
    fr = "\033[0;91m"
    fb = "\033[0;94m"
    fy = "\033[0;33m"
    fm = "\033[0;35m"

    # segundo plano
    bc = "\033[46m"
    bg = "\033[42m"
    bw = "\033[47m"
    br = "\033[41m"
    bb = "\033[44m"
    by = "\033[43m"
    bm = "\033[45m"

    # colors style text:
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT
else:

    init(autoreset=True)
    # primer plano
    fc = Fore.CYAN
    fg = Fore.GREEN
    fw = Fore.WHITE
    fr = Fore.RED
    fb = Fore.BLUE
    fy = Fore.YELLOW
    fm = Fore.MAGENTA

    # segundo plano
    bc = Back.CYAN
    bg = Back.GREEN
    bw = Back.WHITE
    br = Back.RED
    bb = Back.BLUE
    by = Fore.YELLOW
    bm = Fore.MAGENTA

    # estilo de texto
    sd = Style.DIM
    sn = Style.NORMAL
    sb = Style.BRIGHT


def banner():
    banner = '''


%s%s::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: 

%s%s        ____      ___   ___                   _              _           
%s%s._ _ _ <__ / _ _ < . > | . \ ___  _ _ _ ._ _ | | ___  ___  _| | ___  _ _ 
%s%s| ' ' | <_ \| | |/ . \ | | |/ . \| | | || ' || |/ . \<_> |/ . |/ ._>| '_>
%s%s|_|_|_|<___/`___|\___/ |___/\___/|__/_/ |_|_||_|\___/<___|\___|\___.|_|  
%s%s

%s%s::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ''' % ((fm, sb,
           fm, sn,
           fy, sb,
           fy, sn,
           fy, sb,
           sb, sn,
           fm, sn))
    return banner
