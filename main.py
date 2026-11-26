# Write one UTF-8 auto-reply and report its character count.
import os
from pathlib import Path


TEXT = "I'm on vacation. A human will respond shortly. It has been typing for three hours."


def main():
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
