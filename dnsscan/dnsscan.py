from dns import resolver
from colorama import Fore, Style

import sys
class DnsScan():

    domain: str
    subdomains = []
    
    def __init__(self, domain: str, subdomains = None):
        self.domain = domain
        
        if subdomains is not None:
            if '[' in subdomains:
                self.subdomains = eval(subdomains)
            elif '.txt' in subdomains:
                try:
                    file = open(subdomains)
                    self.subdomains = [line.replace('\n', '') for line in file.readlines()]
                except FileNotFoundError:
                    print("File not Found !")
                    sys.exit()
            else:
                self.subdomains.append(subdomains)

    def scan(self):
        try:
            results = resolver.query(self.domain, 'a')
            print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} " + self.domain + " - " + str(results.__getitem__(0)))

            for subdomain in self.subdomains:
                full_domain = subdomain + '.' + self.domain

                results = resolver.query(full_domain, 'A')
                print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} " + full_domain + " - " + str(results.__getitem__(0)))
        except:
            pass
    
    @staticmethod     
    def menu():
        print("")
        domain = input("Domain: ")
        subdomains = None

        if input("Would you like to scan subdomains as well ? (Y/N)") == "Y":
            subdomain_message = "Inform the subdomains that you wish to scan in the following format: \n\n"
            subdomain_message += "subdomain \t\t=> Only one subdomain \n"
            subdomain_message += "[sub1, sub2, sub3] \t=> Subdomain list\n"
            subdomain_message += "Wordlist.txt \t=> Subdomain wordlist file\n\n"
            subdomain_message += "Type here: "

            subdomains = input(subdomain_message)
            DnsScan(domain=domain, subdomains=subdomains).scan()
        else:
            DnsScan(domain=domain).scan()