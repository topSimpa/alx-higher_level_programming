#!/usr/bin/python3
def main():
    import hidden_4 as hid
    for method in dir(hid):
        if method[0] != '_' and method[1] != '_':
            print(method)


if __name__ == "__main__":
    main()
