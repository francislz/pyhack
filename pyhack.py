#!/usr/bin/python3
from portscan.portscan import Portscan
from colorama import Fore, Style

def portscan():
    print("")
    address = input("IP/URL: ")
    port_message = "Type your port in one of the following formats: \n\n"
    port_message += "80 \t\t=> Only one port \n"
    port_message += "80 - 100 \t=> Port Range\n"
    port_message += "[80, 443, 22] \t=> List of ports\n\n"
    port_message += "Ports: "

    ports = input(port_message)

    Portscan(address=address, ports=ports).scan()


def main():
    print(f"{Fore.YELLOW}Choose one of the following options: \n")
    print("[1] For Port Scanning")
    print("[2] For DNS Scanning")
    print(f"{Style.RESET_ALL}")
    choice = input("Select a operation: ")

    if choice == "1":
        portscan()


if __name__ == "__main__":
    main()