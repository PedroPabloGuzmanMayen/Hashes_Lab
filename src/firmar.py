from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from pathlib import Path


from Crypto.PublicKey import RSA


def generate_key():
    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open('files/medisoft_priv.pem', 'wb') as f:
        f.write(private_key)

    with open('files/medisoft_pub.pem', 'wb') as f:
        f.write(public_key)

    print('[OK] Claves generadas:')
    print(' - medisoft_priv.pem (privada)')
    print(' - medisoft_pub.pem (pública)')


def create_signature():
    base_dir = Path(__file__).resolve().parent
    manifest_path = base_dir.parent / 'files' / 'SHA256SUMS.txt'
    priv_key_path = base_dir.parent / 'files' / 'medisoft_priv.pem'

    if not manifest_path.exists():
        print('[ERROR] No existe SHA256SUMS.txt')
        return

    if not priv_key_path.exists():
        print('[ERROR] No existe la clave privada')
        return

    data = manifest_path.read_bytes()

    h = SHA256.new(data)

    key = RSA.import_key(open(priv_key_path, 'rb').read())

    signature = pkcs1_15.new(key).sign(h)

    sig_path = base_dir.parent / 'files' / 'SHA256SUMS.sig'
    with open(sig_path, 'wb') as f:
        f.write(signature)

    print('[OK] Firma generada: SHA256SUMS.sig')


if __name__ == '__main__':
    generate_key()
    create_signature()