package main

import "fmt"

func bubbleSort(arr []int) {
	n := len(arr)
	for {
		swapped := false
		for i := 0; i < n-1; i++ {
			if arr[i] > arr[i+1] {
				arr[i], arr[i+1] = arr[i+1], arr[i]
				swapped = true
			}
		}
		if !swapped {
			break
		}
		n -= 1
	}
}

func callBubbleSort() {
	list := []int{4, 0, 1, 2, 3}
	bubbleSort(list)

	fmt.Println("Bubble sort:", list)
}
