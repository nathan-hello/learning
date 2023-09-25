// Given an integer x, return true if x is a
// palindrome, and false otherwise.
// Example 1:
//   Input: x = 121
//   Output: true
//   Explanation: 121 reads as 121 from left to right and from right to left.
// Example 2:
//   Input: x = -121
//   Output: false
//   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:
//   Input: x = 10
//   Output: false
//   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// Constraints:
//     -231 <= x <= 231 - 1
// Follow up: Could you solve it without converting the integer to a string?

package main

import (
	"fmt"
	"reflect"
)

func isPalendrome(x int) bool {
	if x < 0 {
		x = -x
	}
	singles := []int{}
	for i := 10; true; i = i * 10 {
		quotient, remainder := x/i, x%i

		last := remainder * 10 / i
		singles = append(singles, last)
		if quotient < 1 {
			break
		}
	}
	length := len(singles)

	if length%2 != 0 {
		middle := len(singles) / 2
		singles = append(singles[:middle], singles[middle+1:]...)
	}

	first := singles[:length/2]
	second := singles[length/2:]
	reverse := make([]int, len(second))
	for i, v := range second {
		reverse[len(second)-1-i] = v
	}

	fmt.Printf("first: %v, second %v\n", first, second)

	if reflect.DeepEqual(first, reverse) {
		return true
	} else {
		return false
	}

}

func main() {
	ex1 := 121
	ex2 := -121
	ex3 := 10

	p1 := isPalendrome(ex1)
	p2 := isPalendrome(ex2)
	p3 := isPalendrome(ex3)

	fmt.Printf("p1: %v\n", p1)
	fmt.Printf("p2: %v\n", p2)
	fmt.Printf("p3: %v\n", p3)

}
