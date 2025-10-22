#!/usr/bin/env python3
import sys

VERSION = "0.0.1"

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            print(VERSION)
        else:
            print(f"Unbekannter Befehl: {sys.argv[1]}")
    else:
        print("CatPackManager – deine Toolsammlung\nNutze '--version' für Versionsinfo")

if __name__ == "__main__":
    main()
