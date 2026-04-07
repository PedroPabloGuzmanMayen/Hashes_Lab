from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from pathlib import Path


def verify():
    base_dir = Path(__file__).resolve().parent

    manifest_path = base_dir.parent / 'files' / 'SHA256SUMS.txt'
    sig_path = base_dir.parent / 'files' / 'SHA256SUMS.sig'
    pub_key_path = base_dir.parent / 'files' / 'medisoft_pub.pem'

    if not manifest_path.exists() or not sig_path.exists():
        print('[ERROR] Faltan archivos')
        return

    data = manifest_path.read_bytes()
    signature = sig_path.read_bytes()

    h = SHA256.new(data)

    key = RSA.import_key(open(pub_key_path, 'rb').read())

    try:
        pkcs1_15.new(key).verify(h, signature)
        print('[OK] Firma válida')
    except (ValueError, TypeError):
        print('[ERROR] Firma inválida')


if __name__ == '__main__':
    verify()