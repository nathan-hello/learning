package main

import (
	"kata-machine-golang/algs"
)

func main() {
	algs.BubbleSort(
		"bubble sort",
		[]int{9, 3, 7, 4, 69, 420, 42},
		[]int{3, 4, 7, 9, 42, 69, 420},
	)
}
