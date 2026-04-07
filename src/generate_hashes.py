from Crypto.Hash import MD5, SHA1, SHA256, SHA3_256
from Crypto.Util.strxor import strxor

def xor_diff_bits(a: bytes, b: bytes):
    x = strxor(a, b)
    return sum(bin(byte).count('1') for byte in x)


def build_hash(mode: int, message: bytes):

    if mode == 0:
        h = SHA1.new()
    elif mode == 1:
        h = SHA256.new()
    elif mode == 2:
        h = SHA3_256.new()
    elif mode == 3:
        h = MD5.new()
    else:
        raise ValueError('Modo inválido')

    h.update(message)
    return h.digest(), h.hexdigest()

def build_hash_file(mode: int, filepath):

    if mode == 0:
        h = SHA1.new()
    elif mode == 1:
        h = SHA256.new()
    elif mode == 2:
        h = SHA3_256.new()
    elif mode == 3:
        h = MD5.new()
    else:
        raise ValueError('Modo inválido')

    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)

    return h.digest(), h.hexdigest()