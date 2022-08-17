# -*- coding: utf-8 -*-
# Some keywords should be followed by a single space

keywords = ["case", "class", "delete", "enum", "explicit", 
    "extern", "goto", "new", "struct", "union", "using"]

state = "other"
for f in vera.getSourceFileNames():
    for t in vera.getTokens(f, 1, 0, -1, -1, []):
        if state == "other":
            if t.type in keywords:
                state = "keyword"
                lineno = t.line
                keyvalue = t.value
        elif state == "keyword":
            if t.type == "space" and t.value == " ":
                state = "space"
            else:
                vera.report(f, lineno, "關鍵字 "+keyvalue+" 後面沒有接單一空格")
                state = "other"
        elif state == "space":
            if t.type == "newline":
                vera.report(f, lineno, "關鍵字 "+keyvalue+" 後面沒有接單一空格")
            state = "other"

