def convert(n):
    return (bin(n).replace('0b', '').upper(), oct(n).replace('0o', '').upper(), hex(n).replace('0x', '').upper())
