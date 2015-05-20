package main

import (
	"fmt"
	"strings"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	ip := strings.Split(r.RemoteAddr,":")[0]
	port := strings.Split(r.RemoteAddr,":")[1]
	fmt.Fprintf(w, "Your ip is %s \n", ip)
	fmt.Fprintf(w, "Connection port: %s\n",port)
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
