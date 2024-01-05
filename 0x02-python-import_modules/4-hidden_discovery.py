#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import *

    def_names_pyc = dir()

    for names in range(len(def_names_pyc)):
        if (def_names_pyc[names][:2] != "__"):
            print("{:s}".format(def_names_pyc[names]))
