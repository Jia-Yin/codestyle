package main

import (
    "net/http"
	"fmt"
	"io/ioutil"
    "github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("Start server...")
	// gin.SetMode(gin.ReleaseMode)
    router := gin.Default()
	router.LoadHTMLGlob("template/*")
	router.GET("/", func(c *gin.Context) {
	  c.HTML(http.StatusOK, "upload.html", gin.H{})
	})
	// router.StaticFS("/file", http.Dir("public"))
  
    router.POST("/upload", func(c *gin.Context) {
        file, _ := c.FormFile("file") // get file from form input name 'file'
		filepath := "public/"+file.Filename
        c.SaveUploadedFile(file, filepath) // save file to tmp folder in current directory

		b, err := ioutil.ReadFile(filepath) // just pass the file name
		if err != nil {
			fmt.Print(err)
		}
	
		str := string(b) // convert content to a 'string'
		result := checkStyle(filepath)

        // c.String(http.StatusOK, "file: %s", file.Filename)
        c.String(http.StatusOK, "Result:\n%s", str+result)
    })

    router.Run(":8080")
}

