# -*- coding: utf-8 -*-
# No leading and no trailing empty lines

for f in vera.getSourceFileNames():
    lineCount = vera.getLineCount(f)
    if lineCount > 0:
        firstLine = vera.getLine(f, 1).strip()
        if firstLine == "":
            vera.report(f, 1, "檔案最前面出現空白列")
    if lineCount > 1:
        lastLine = vera.getLine(f, lineCount).strip()
        lastLine2 = vera.getLine(f, lineCount-1).strip()
        if lastLine == "" and lastLine2 == "":
            vera.report(f, 1, "檔案最後面出現太多空白列")
