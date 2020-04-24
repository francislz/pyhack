import struct
import socket
from sniffer.tools.mac import convert_to_mac

class Ethernet:

    def __init__(self, raw_data, src_mac=None, dst_mac=None):
        dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

        self.dest_mac = convert_to_mac(dest)
        self.src_mac = convert_to_mac(src)
        self.proto = socket.htons(prototype)
        self.data = raw_data[14:]