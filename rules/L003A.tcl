#!/usr/bin/tclsh
# No leading and no trailing empty lines

foreach f [getSourceFileNames] {
    set lineCount [getLineCount $f]
    if {$lineCount > 0} {
        set firstLine [getLine $f 1]
        if {[string trim $firstLine] == ""} {
            report $f 1 "檔案最前面出現空白列"
        }

        set lastLine [getLine $f $lineCount]
        if {[string trim $lastLine] == ""} {
	        set lastLine [getLine $f [expr $lineCount - 1]]
	        if {[string trim $lastLine] == ""} {
	            report $f $lineCount "檔案最後面出現太多空白列"
	        }
        }
    }
}
