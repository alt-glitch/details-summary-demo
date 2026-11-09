import argparse


def main():
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--name", default="world", help="who to greet (default: world)")
    parser.add_argument("--shout", action="store_true", help="print the greeting in capitals")
    args = parser.parse_args()
    text = f"Hello, {args.name}"
    print(text.upper() if args.shout else text)


if __name__ == "__main__":
    main()
