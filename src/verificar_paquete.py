from pathlib import Path
from generate_hashes import build_hash_file


def main():
    manifest_path = Path('./files/SHA256SUMS.txt')

    if not manifest_path.exists():
        print('[ERROR] No existe SHA256SUMS.txt')
        return

    correct = 0
    incorrect = 0

    print('\n=== Verificación de integridad ===\n')

    with open(manifest_path, 'r') as manifest:
        for line in manifest:
            expected_hash, filename = line.strip().split()

            file_path = Path('./files') / filename

            if not file_path.exists():
                print(f'[MISSING] {filename}')
                incorrect += 1
                continue

            _, actual_hash = build_hash_file(1, file_path)

            if actual_hash == expected_hash:
                print(f'[OK] {filename}')
                correct += 1
            else:
                print(f'[CORRUPT] {filename}')
                print(f'  esperado: {expected_hash}')
                print(f'  actual:   {actual_hash}')
                incorrect += 1

    print('\n=== Resumen ===')
    print(f'Correctos: {correct}')
    print(f'Incorrectos: {incorrect}')


if __name__ == '__main__':
    main()