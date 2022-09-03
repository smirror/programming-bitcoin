import hashlib

BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def hash160(s):
    """
    sha256の後にripemd160が続く
    """
    return hashlib.new("ripemd160", hashlib.sha256(s).digest()).digest()


def hash256(s):
    """two rounds of sha256"""
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def encode_base58(s):
    count = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
    num = int.from_bytes(s, "big")
    prefix = "1" * count
    result = ""
    while num > 0:
        num, mod = divmod(num, 58)
        result = BASE58_ALPHABET[mod] + result
    return prefix + result


def encode_base58_checksum(b):
    return encode_base58(b + hash256(b)[:4])


def little_endian_to_int(b):
    """
    little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer
    """
    return int.from_bytes(b, "little")


def int_to_little_endian(n, length):
    """
    little_endian_to_int takes byte sequence as a little-endian number.
    Returns an integer
    """
    return n.to_bytes(length, "little")


def read_varint(s):
    """
    ストリームから可変長の整数を読み取る
    """
    i = s.read(1)[0]
    # 数値はlittle endian
    if i == 0xfd:
        # 0xfdは次の2バイトがデータ長であることを示す
        return little_endian_to_int(s.read(2))
    elif i == 0xfe:
        # 0xfeは次の4バイトがデータ長であることを示す
        return little_endian_to_int(s.read(4))
    elif i == 0xff:
        # 0xffは次の8バイトがデータ長であることを示す
        return little_endian_to_int(s.read(8))
    else:
        # それ以外は単なる数値
        return i


def encode_varint(i):
    """
    整数をvarintとしてエンコードする
    """

    if i < 0xfd:
        return bytes([i])
    elif i < 0x10000:
        return b"\xfd" + int_to_little_endian(i, 2)
    elif i < 0x100000000:
        return b"\xfe" + int_to_little_endian(i, 4)
    elif i < 0x10000000000000000:
        return b"\xff" + int_to_little_endian(i, 8)
    else:
        return ValueError("integer too large: {}".format(i))
