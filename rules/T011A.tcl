#!/usr/bin/tclsh
# 大括號同一列，或同一行，或左括號在行尾，內容應縮排

proc acceptPairs {} {
    global file parens index end

    while {$index != $end} {
        set nextToken [lindex $parens $index]
        set tokenValue [lindex $nextToken 0]

        if {$tokenValue == "\{"} {
            incr index
            set leftParenLine [lindex $nextToken 1]
            set leftParenColumn [lindex $nextToken 2]

            acceptPairs

            if {$index == $end} {
                report $file $leftParenLine "程式碼出現未匹配的大括號 \{"
                return
            }

            set nextToken [lindex $parens $index]
            incr index
            set tokenValue [lindex $nextToken 0]
            set rightParenLine [lindex $nextToken 1]
            set rightParenColumn [lindex $nextToken 2]

            if {$leftParenLine != $rightParenLine} {
                set leftParenLineTokens [getTokens $file $leftParenLine 0 [expr $leftParenLine + 1] 0 {}]
                set lplen [llength $leftParenLineTokens]

                set lasttoken "notexist"
                set ignore 0
                foreach tok $leftParenLineTokens {
                    if {$leftParenColumn == [lindex $tok 2]} {
                        set lasttype [lindex $lasttoken 3]
                        if { ($lasttype == "assign") || ($lasttype == "leftbrace") } {
                            set ignore 1
                            break
                        }
                    } else {
                        set lasttoken $tok
                    }
                }

                if {$ignore == 1} {
                    continue
                }

                set leftParenLineLastTokenColumn [lindex [lindex $leftParenLineTokens [expr $lplen - 2]] 2]
                
                # report "DEBUG" $leftParenLine [lindex $]
                # somethings exists after left bracket

                if {$leftParenColumn != $leftParenLineLastTokenColumn} {
                	set afterTokens [getTokens $file $leftParenLine [expr $leftParenColumn + 1] $leftParenLine $leftParenLineLastTokenColumn {}]
		            set others 0
		            foreach tok $afterTokens {
                        set ttype [lindex $tok 3]
	                    # report $file $leftParenLine $ttype
                        if { ($ttype != "space") && ($ttype != "ccomment") } {
                            set others 1
                            break
                        }
                    }
                	if {$others == 1} {
	                    report $file $leftParenLine "多列的區塊，左邊大括號後面應該換列"
                	}
                } else {
                    # make an exception for line continuation
                    set leftLine [getLine $file $leftParenLine]
                    set rightLine [getLine $file $rightParenLine]

                    for {set i [expr $leftParenLine + 1]} {$i < $rightParenLine} {incr i 1} {
                        set lineTokens [getTokens $file $i 0 [expr $i + 1] 0 {}]
                        foreach ltok $lineTokens {
                            set ltoktype [lindex $ltok 3]
                            if {($ltoktype != "space") && ($ltoktype != "newline")} {
                                # report "DEBUG" $i $ltoktype
                                set firstcol [lindex $ltok 2]
                                if {$firstcol <= $rightParenColumn} {
                                    report $file $i "程式碼未正確縮排"
                                    break
                                }
                            }
                        }
                    }
                }
            }
        } else {
            return
        }
    }
}

foreach file [getSourceFileNames] {
    set parens [getTokens $file 1 0 -1 -1 {leftbrace rightbrace}]
    set index 0
    set end [llength $parens]
    acceptPairs
    if {$index != $end} {
        report $file [lindex [lindex $parens $index] 1] "程式碼出現未匹配的大括號 \}"
    }
}
