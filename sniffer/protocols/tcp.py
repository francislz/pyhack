import struct
import socket

class TCP:

    def __init__(self, ip):
        self.ip = ip
        src_port, dst_port, seq, ack, offset_flags = struct.unpack('!H H I I H', ip.data[:14])
        offset = (offset_flags >> 12) * 4
        flags = (offset_flags & 63)

        self.src_port = src_port
        self.dst_port = dst_port
        self.offset = offset
        self.seq = seq
        self.ack = ack
        self.flags = {}
        self.data = ip.data[offset:]

        self.flags["urg"] = flags >> 5
        self.flags["ack"] = (flags >> 4) & 0b000001
        self.flags["psh"] = (flags >> 3) & 0b000001
        self.flags["rst"] = (flags >> 2) & 0b000001
        self.flags["syn"] = (flags >> 1) & 0b000001
        self.flags["fin"] = flags & 0b000001
