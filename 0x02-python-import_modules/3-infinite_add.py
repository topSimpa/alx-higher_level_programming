#!/usr/bin/python3
def main():
    import sys
    res = 0
    for arg in sys.argv:
        if arg != "./3-infinite_add.py":
            res += int(arg)
    print(res)


if __name__ == "__main__":
    main()
