#! /usr/bin/env python

import sys

if not getattr(sys, "frozen", False):
    # direct call of __main__.py
    import os.path

    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import nakuyagen

if __name__ == "__main__":
    print(f"Exit with code {nakuyagen.main()}")
