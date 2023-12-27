import LineParser as LP
import Tokenizer as TK

with open("tests/test_general.txt", 'r') as fp:
    lp = LP.LineParser(fp.read())
    fp.close()

lp.Parse()