#!/usr/bin/python3
def main():
    import calculator_1 as cal
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cal.add(a, b)))
    print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    print("{} / {} = {}".format(a, b, cal.div(a, b)))


if __name__ == "__main__":
    main()
