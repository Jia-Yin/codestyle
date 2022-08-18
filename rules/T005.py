# -*- coding: utf-8 -*-
# Keywords break and continue should be immediately followed by a semicolon

keywords = ["break", "continue"]

for f in vera.getSourceFileNames():
    allTokens = vera.getTokens(f, 1, 0, -1, -1, [])
    for i in range(len(allTokens)-1):
        t1, t2 = allTokens[i], allTokens[i+1]
        if t1.type in keywords and t2.type != "semicolon":
            vera.report(f, t1.line, "關鍵字 "+t1.value+" 後面未緊跟著分號")
