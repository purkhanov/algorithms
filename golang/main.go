package main

import "fmt"

func main() {
	myList := []int{1, 3, 5, 7, 9}

	res, exists := binary_search(myList, 9)
	if !exists {
		fmt.Println("Not found")
	} else {
		fmt.Printf("Result: %d\n", res)
	}

}
