#!/usr/bin/python3
from portscan.portscan import Portscan
from dnsscan.dnsscan import DnsScan

from colorama import Fore, Style


def main():
    print(f"{Fore.YELLOW}Choose one of the following options: \n")
    print("[1] For Port Scanning")
    print("[2] For DNS Scanning")
    print(f"{Style.RESET_ALL}")
    choice = input("Select a operation: ")

    if choice == "1":
        Portscan.menu()
    elif choice == "2":
        DnsScan.menu()


if __name__ == "__main__":
    main()