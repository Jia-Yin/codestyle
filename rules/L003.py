# -*- coding: utf-8 -*-
# No leading and no trailing empty lines

for f in vera.getSourceFileNames():
    lineCount = vera.getLineCount(f)
    lines = vera.getAllLines(f)
    if lineCount > 0:
        firstLine = lines[0].strip()
        if firstLine == "":
            vera.report(f, 1, "檔案最前面出現空白列")
    if lineCount > 1:
        lastLine = lines[lineCount-1].strip()
        lastLine2 = lines[lineCount-2].strip()
        if lastLine == "" and lastLine2 == "":
            vera.report(f, lineCount-1, "檔案最後面出現太多空白列")
