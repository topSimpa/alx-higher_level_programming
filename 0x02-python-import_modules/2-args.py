#!/usr/bin/python3
def main():
    import sys
    n = len(sys.argv) - 1
    if n > 1:
        print(f"{n} arguments:")
    elif n == 0:
        print(f"{n} arguments.")
        return
    else:
        print(f"{n} argument:")
    ind = 1
    for arg in range(n):
        print(f"{ind}: {sys.argv[ind]}")
        ind += 1


if __name__ == "__main__":
    main()
