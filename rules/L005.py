# -*- coding: utf-8 -*-
# There should not be too many consecutive empty lines

max_consecutive_empty_lines = 2

for f in vera.getSourceFileNames():
    lineNumber = 1
    emptyCount = 0
    reported = False
    lines = vera.getAllLines(f)
    for lineNumber, line in enumerate(lines):
        if line.strip() == "":
            emptyCount += 1
            if emptyCount > max_consecutive_empty_lines and not reported:
                vera.report(f, lineNumber+1, "出現太多連續空白列")
                reported = True
        else:
            emptyCount = 0
            reported = False
