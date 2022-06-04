package main

import (
	"fmt"
	"net/http"
)

var (
	cookieOne   = "cookie-one"
	cookieTwo   = "cookie-two"
	cookieThree = "cookie-three"
)

func handlerWithCookie(w http.ResponseWriter, r *http.Request) {
	c := http.Cookie{
		Name: cookieOne,
	}
	http.SetCookie(w, &c)
	fmt.Fprint(w, "You got cookie-one!")
}

func handlerToCheckCookie(w http.ResponseWriter, r *http.Request) {
	cookies := r.Cookies()
	for _, c := range cookies {
		if c.Name == cookieOne {
			newCookie := http.Cookie{
				Name: cookieTwo,
			}
			http.SetCookie(w, &newCookie)
			fmt.Fprintf(w, "You got cookie-two")
			return
		}
	}
	http.Error(w, "cookie-one not found", http.StatusBadRequest)
}

func handlerWithoutCookie(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "/cookie", http.StatusTemporaryRedirect)
}

func registerHandlers(mux *http.ServeMux) {
	mux.HandleFunc("/cookie", handlerWithCookie)
	mux.HandleFunc("/check-cookie", handlerToCheckCookie)
	mux.HandleFunc("/no-cookie", handlerWithoutCookie)
}

func main() {
	mux := http.NewServeMux()
	registerHandlers(mux)
	http.ListenAndServe(":8080", mux)
}
