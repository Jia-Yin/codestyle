# -*- coding: utf-8 -*-
# # no trailing space
for f in vera.getSourceFileNames():
  for lineNumber, line in enumerate(vera.getAllLines(f)):
    if line.endswith(" "):
      vera.report(f, lineNumber+1, "行尾有多餘的空白")
