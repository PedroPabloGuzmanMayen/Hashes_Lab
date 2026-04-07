import sys
from pathlib import Path
from generate_hashes import build_hash_file


def main():
    if len(sys.argv) < 6:
        print("Uso: python generar_manifiesto.py <file1> ... <file5>")
        sys.exit(1)

    files = sys.argv[1:]

    with open("files/SHA256SUMS.txt", "a") as manifest:
        for file in files:
            path = Path(file)

            if not path.exists():
                print(f"[ERROR] No existe: {file}")
                continue

            _, hash_value = build_hash_file(1, path)  # SHA256

            manifest.write(f"{hash_value}  {path.name}\n")
            print(f"[OK] {path.name} -> {hash_value}")


if __name__ == "__main__":
    main()