from colorama import Fore
import os
import sys
from modules import banner
from modules import localhost  # Import the localhost module

import platform

sysname = platform.uname()[0]

while True:
    banner.banner()
    banner.infolist0()

    try:
        input1 = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "STORM-BREAKER" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + """]\n └──╼ """ + Fore.WHITE + "$ ")

        if input1 == "1":
            localhost.webcam()  # Use the correct function name

        elif input1 == "2":
            if sysname == "Windows":
                banner.banner()
                print("\n This feature only works on Linux distributions\n".title())
                input(Fore.RED + " [!]" + Fore.GREEN + " Back To Menu (Press Enter...) ")
            else:
                localhost.micro()  # Use the correct function name

        elif input1 == "3":
            banner.banner()
            localhost.screen()  # Use the correct function name

        elif input1 == "4":
            banner.banner()
            localhost.location()  # Use the correct function name

        elif input1 == "5":
            banner.banner()
            banner.infolist1()

        elif input1 == "6":
            print("\n God Lock :)")
            sys.exit()

    except KeyboardInterrupt:
        print("")
        sys.exit()
