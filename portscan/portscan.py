import socket
from colorama import Fore, Style
class Portscan():
    ports = []

    def __init__(self, address: str, ports: str):
        self.address = address
        if '-' in ports:
            start, end = ports.replace(' ', '').split('-')
            self.ports = [port for port in range(int(start), int(end))]
        elif '[' in ports:
            self.ports = eval(ports)
        else:
            self.ports.append(ports)
    
    def scan(self):
        client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_s.settimeout(5)

        for port in self.ports:
            status = client_s.connect_ex((self.address, int(port)))
            if(status == 0):
                print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Port " + str(port) + f" {Fore.GREEN}OPENED{Style.RESET_ALL} in " + self.address)
            else:
                print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Port " + str(port) + f" {Fore.RED}CLOSED{Style.RESET_ALL} in " + self.address)
        client_s.close()
            