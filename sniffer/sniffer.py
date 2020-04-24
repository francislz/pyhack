import socket
from .protocols.ethernet import Ethernet
from .protocols.ipv4 import IPv4
from .protocols.tcp import TCP

def sniffer(args):
    # Make sure is compatible with all machines
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    
    while True:
        raw_data = sniffer.recvfrom(65536)[0]
        eth = Ethernet(raw_data=raw_data)
        # If the protocol is 8 then its a IPv4 packet
        # print(typeof(args['nP']))
        if eth.proto == args['nP']:         
            ip = IPv4(eth)
            # print(ip.dst)
            # TCP packet type
            if ip.proto == args['tP']:
                tcp = TCP(ip)
                if ip.dst == args['nD'] and tcp.flags == args['tF']:
                    print("Packet according to filter was found.....")
                    return tcp
                

def main():
    # Make sure is compatible with all machines
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data = sniffer.recvfrom(65536)[0]

        eth = Ethernet(raw_data=raw_data)
        # print("Ethernet Frame: ")
        # print("\tSource: {} -> Destination: {} = Protocol: {}".format(eth.src_mac, eth.dest_mac, eth.proto))
        
        # If the protocol is 8 then its a IPv4 packet
        if eth.proto == 8:
            
            ip = IPv4(eth.data)
            print("\nIP Segment version: " + str(ip.version))
            print("\tSource: {} -> Destination: {}".format(ip.src, ip.dst))

            # TCP packet type
            if ip.proto == 6:
                tcp = TCP(ip.data)
                print("\tTcp flags: ")
                print("\t\t URG: " + str(tcp.flags['urg']))
                print("\t\t ACK: " + str(tcp.flags['ack']))
                print("\t\t PSH: " + str(tcp.flags['psh']))
                print("\t\t RST: " + str(tcp.flags['rst']))
                print("\t\t SYN: " + str(tcp.flags['syn']))
                print("\t\t FIN: " + str(tcp.flags['fin']))

if __name__ == "__main__":
    main()