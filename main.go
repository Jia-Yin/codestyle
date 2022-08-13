package main

import (
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

type ResultData struct {
	code   string
	result string
}

func main() {
	fmt.Println("Start server...")
	// gin.SetMode(gin.ReleaseMode)
	router := gin.Default()
	router.LoadHTMLGlob("template/*.html")
	router.Static("/lib", "./lib")
	router.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "upload.html", gin.H{})
	})
	// router.StaticFS("/file", http.Dir("public"))

	router.POST("/upload", func(c *gin.Context) {
		file, _ := c.FormFile("file") // get file from form input name 'file'
		filepath := "public/" + file.Filename
		c.SaveUploadedFile(file, filepath) // save file to tmp folder in current directory

		b, err := ioutil.ReadFile(filepath) // just pass the file name
		if err != nil {
			fmt.Print(err)
		}

		code := string(b) // convert content to a 'string'
		result := checkStyle(filepath)

		c.HTML(http.StatusOK, "result.html", gin.H{
			"code":   code,
			"result": result,
		})
	})

	router.Run(":8080")
}
