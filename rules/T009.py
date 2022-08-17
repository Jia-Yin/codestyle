# -*- coding: utf-8 -*-
# Comma should not be preceded by whitespace, but should be followed by one

permits = ["space", "newline", "operator", "leftparen"]

for f in vera.getSourceFileNames():
    allTokens = vera.getTokens(f, 1, 0, -1, -1, [])
    for i in range(len(allTokens)-1):
        t1, t2 = allTokens[i], allTokens[i+1]
        if t1.type == "space" and t2.type == "comma":
            vera.report(f, t1.line, "逗號前面不要加空格")
        if t1.type == "comma" and not t2.type in permits:
            vera.report(f, t1.line, "逗號後面請加上空格")
