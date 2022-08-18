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
        # skip space
        j = i-1
        while j>=0 and tokens[j].type == "space":
            j -= 1
        # check
        if tokens[j].line == leftP.line and tokens[j].type in ["assign", "leftbrace"]:
            continue

        # left and right at different columns, 左邊大括號後面只能放空白及註解
        if leftP.column != rightP.column:
            ok = True
            j = i+1
            while j<len(tokens) and tokens[j].line == leftP.line:
                if not tokens[j].type in ["space", "ccomment", "cppcomment", "newline"]:
                    ok = False
                    break
                else:
                    j += 1
            if not ok:
                vera.report(f, leftP.line, "多列的區塊，左邊大括號後面應該換列")

        for lineno in range(leftP.line+1, rightP.line):
            lineTokens = vera.getTokens(f, lineno, 0, lineno+1, 0, [])
            for k in range(len(lineTokens)):
                if not lineTokens[k].type in ["space", "newline"]:
                    if lineTokens[k].column <= rightP.column:
                        vera.report(f, lineno, "程式碼未正確縮排")
                    break


