def convert_to_mac(addr):
    return ':'.join(map('{:02x}'.format, addr)).upper()