#!/usr/bin/env python3

""" Test program to test CI env """


def print_some_info():
    """print some info"""
    info = "a" + "b" + "c"
    print(info)


def main():
    """Main func"""
    print_some_info()


if __name__ == "__main__":
    main()

    do_something_linter_hates=1
