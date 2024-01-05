#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    def_names_pyc = dir(hidden_4)

    for names in def_names_pyc:
        if (names[:2] != "__"):
            print("{:s}".format(names))
