package algs

import (
	"fmt"
	"slices"
)

func BubbleSort(name string, input []int, expect []int) bool {
	for i := 0; i < len(input); i++ {
		for j := 0; j < len(input)-1-i; j++ {
			if input[j] > input[j+1] {
				tmp := input[j]
				input[j] = input[j+1]
				input[j+1] = tmp
			}
		}
	}
	if slices.Equal[[]int](input, expect) {
		fmt.Printf("%s pass\n", name)
		return true
	}
	fmt.Printf("%s fail\n", name)
	return false
}
