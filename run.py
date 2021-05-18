import warnings
warnings.filterwarnings('ignore', category=SyntaxWarning, message='"is" with a literal')

from easylang_lex import lexer
from easylang_parser import *

__all__ = ["parse"]
_parse = mk_parser()


def parse(text: str, filename: str = "unknown"):
    tokens = lexer(filename, text)
    status, res_or_err = _parse(None, Tokens(tokens))
    if status:
        return res_or_err

    msgs = []
    lineno = None
    colno = None
    filename = None
    offset = 0
    msg = ""
    for each in res_or_err:
        i, msg = each
        token = tokens[i]
        lineno = token.lineno + 1
        colno = token.colno
        offset = token.offset
        filename = token.filename
        break
    e = SyntaxError(msg)
    e.lineno = lineno
    e.colno = colno
    e.filename = filename
    e.text = text[offset - colno : text.find("\n", offset)]
    e.offset = colno
    raise e


# exp = parse(
#     """
# print(add(1, 2))
# k = fun (x, y, z) =>
#     {
#         if gt(x,  y)
#         then add(z, 1)
#         else add(z, -1)
#     }
#
# print(k(1, 2, 3))
# print(k(2, 1, 3))
# """,
#     "<unknown file>",
# )

import operator

ctx = {"+": operator.add, "print": print, ">": operator.gt}

while True:
    try:
        source_code = input("simple> ")
        filename = "<repl>"
        obj = parse(source_code, filename)
        print(obj(ctx))
    except Exception as e:
        print(type(e), e)
