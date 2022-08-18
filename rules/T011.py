# -*- coding: utf-8 -*-
# 大括號同一列，或同一行，或左括號在行尾，內容應縮排

def paringBrace(f, tokens):
    pairs, stack, match = {},  [], True
    for i in range(len(tokens)):
        if tokens[i].type == "leftbrace":
            stack.append(tokens[i])
        elif tokens[i].type == "rightbrace":
            if len(stack) == 0:
                match = False
                break
            k = stack.pop()
            if k.type == "rightbrace":
                match = False
                break
            pairs[k] = tokens[i]
    if len(stack) > 0 or not match:
        vera.report(f, tokens[i].line, "程式碼出現未匹配的大括號 }")
        return False, {}
    return True, pairs

for f in vera.getSourceFileNames():
    tokens = vera.getTokens(f, 1, 0, -1, -1, [])
    ok, pdicts = paringBrace(f, tokens)
    if not ok:
        continue
    for i in range(len(tokens)):
        if tokens[i].type != "leftbrace":
            continue
        leftP, rightP = tokens[i], pdicts[tokens[i]]
        if leftP.line == rightP.line: # Both at the same line
            continue
        # Below is the case: left and right are at different lines
        # leftP 前面為 = 或 { 時忽略規則


        print(leftP.line, leftP.column, rightP.line, rightP.column)


