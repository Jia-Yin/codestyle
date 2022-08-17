# -*- coding: utf-8 -*-
# Keywords return and throw should be immediately followed by a semicolon or a single space

keywords = ["return", "throw"]

for f in vera.getSourceFileNames():
    allTokens = vera.getTokens(f, 1, 0, -1, -1, [])
    for i in range(len(allTokens)-1):
        t1, t2 = allTokens[i], allTokens[i+1]
        if t1.type in keywords and not t2.value in [",", " "]:
            vera.report(f, t1.line, "關鍵字 "+t1.value+" 後面未跟著分號或單一空格")
