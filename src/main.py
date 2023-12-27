import LineParser as LP

with open("tests/test_general.txt", 'r') as fp:
    lp = LP.LineParser(fp.read(), write_to_file=False)
    fp.close()

lp.Parse()