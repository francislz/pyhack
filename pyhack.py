#!/usr/bin/python3
from sniffer.sniffer import sniffer
from portscan.portscan import Portscan
from colorama import Fore, Style

import argparse
import sys

PROTO_CONST = {
    'tcp': 6,
    'ipv4': 8
}

def map_args(options):
    args = {}
    for key in options:
        try:
            args[key] = PROTO_CONST[options[key]]
        except KeyError:
            args[key] = options[key]

    flags = int(args['tF']) if 'b' not in args['tF'] else int(args['tF'], 2)
    args['tF'] = {}
    args['tF']["urg"] = flags >> 5
    args['tF']["ack"] = (flags >> 4) & 0b000001
    args['tF']["psh"] = (flags >> 3) & 0b000001
    args['tF']["rst"] = (flags >> 2) & 0b000001
    args['tF']["syn"] = (flags >> 1) & 0b000001
    args['tF']["fin"] = flags & 0b000001

    return args


def main(options):
    print(options)
    if options['module'] == "pscan":
        Portscan(address=options.addr, ports=options.port).scan()
    elif options['module'] == "psniff":
        packet = sniffer(options)
        print(packet.flags)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Some pentest tools")
    # Main menu choices
    help = f"{Fore.YELLOW}Choose one of the following options: \n"
    help += f"pscan, dscan, psniff{Style.RESET_ALL}"

    port_message = "Type your port in one of the following formats: \n\n"
    port_message += "80 \t\t=> Only one port \n"
    port_message += "80 - 100 \t=> Port Range\n"
    port_message += "[80, 443, 22] \t=> List of ports\n\n"

    parser.add_argument('module', help=help)

    # Port Scan input args
    parser.add_argument('-sS', '--sS', type=bool, const=True, nargs='?', help="Enables [SYN, ACK] scan")
    parser.add_argument('-addr', '--addr', help="Type in the address you would like to scan")
    parser.add_argument('-port', '--port', help=port_message)

    # Application layer filters
    parser.add_argument('-aP', '--aP', help="Filter sniffer by aplication protocol (HTTP, HTTPS, etc)")
    parser.add_argument('-tP', '--tP', help="Filter sniffer by transport protocol (TCP/UDP)")
    parser.add_argument('-nP', '--nP', help="Filter sniffer by network protocol (IPv4, IPv6)")

    # Transport layer filter
    parser.add_argument('-tS', '--tS', type=int, help="Filter TCP by Source Port")
    parser.add_argument('-tD', '--tD', type=int, help="Filter TCP by Destination Port")
    parser.add_argument('-tF', '--tF', help="Filter TCP by protocol Flags. Accepts binary or decimal (0b000000 or 0)")

    # Network Layer filters
    parser.add_argument('-nS', '--nS', help="Filter IP by Source Address")
    parser.add_argument('-nD', '--nD', help="Filter IP by Destination Address")
    
    options = parser.parse_args(sys.argv[1:])
    
    main(map_args(vars(options)))