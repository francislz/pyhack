import struct
import socket

class IPv4:

    def __init__(self, eth):
        self.eth = eth
        version_and_header = eth.data[0]
        version = (version_and_header >> 4)
        hlen = (version_and_header & 15) * 4

        # x means that the value will be ignored
        self.ttl, self.proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', eth.data[:20])
        
        self.src = self.bytes_2_ipv4(src)
        self.dst = self.bytes_2_ipv4(target)
        self.hlen = hlen
        self.version = version
        self.data = eth.data[hlen:]
    
    def bytes_2_ipv4(self, addr):
        return '.'.join(map(str, addr))