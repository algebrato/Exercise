//comment2
package main

import (
	"fmt"
	"strings"
	"net/http"
	//"time"
	//"bytes"
)

func handler(w http.ResponseWriter, r *http.Request) {
	ip := strings.Split(r.RemoteAddr,":")[0]
	port := strings.Split(r.RemoteAddr,":")[1]
	fmt.Fprintf(w, "Your ip is %s \n", ip)
	fmt.Fprintf(w, "Connection port: %s\n",port)
}

func destroy(w http.ResponseWriter, r *http.Request) {
}


func create(w http.ResponseWriter, r *http.Request) {
	http.SetCookie(w, &http.Cookie{Name: "cookie-1", Value: "one", Path: "/create"})
	http.SetCookie(w, &http.Cookie{Name: "cookie-2", Value: "two", Path: "/create", MaxAge: 4})
	http.SetCookie(w, &http.Cookie{Name: "cookie-3", Value: "tree", Path: "/create"})

}

func main() {
	http.HandleFunc("/", handler)
	http.HandleFunc("/create", create)
	http.HandleFunc("/delete", destroy)
	http.ListenAndServe(":8080", nil)
}
