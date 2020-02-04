package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	f, err := os.Open("hello.py")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	fmt.Print("intelisnense!!!")
	r := bufio.NewReader(f)
	for {
		s, err := r.ReadString('\n')
		if err != nil {
			break
		}
		fmt.Println(s)
	}
}
