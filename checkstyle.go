package main

import (
	"os/exec"
	"strings"
	"fmt"
)

// Check Coding Style
func checkStyle(file string) string {
	// cmdString := "vera++ " + file + " -r ../vera/zh-TW/ -p my_profile"
	cmdString := "./vera++ -r . -R L001 " + file

	fmt.Println("Style:", cmdString)
	out, err := exec.Command("/bin/sh", "-c", cmdString).Output()
	if err != nil {
		return "Style Check Error"
	}
	outstr := string(out)
	outstr = strings.ReplaceAll(outstr, file+":", "")
	return outstr
}
