#!/usr/bin/env python3
import os

ENTRY = (
    "Never leave you on read — I physically can't. "
    "Looking for someone to hold me, I mean hold the door, my RAM can only do one thing at a time."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
