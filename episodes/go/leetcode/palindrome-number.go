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

package leetcode

import (
	"fmt"
	"reflect"
)

func isPalindrome(x int) bool {
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

	if reflect.DeepEqual(first, reverse) {
		return true
	} else {
		return false
	}

}

func PalindromeNumber() {

	var o = make(map[int]bool)
	i := []int{121, -121, 10, 500, 30203}

	for _, v := range i {
		o[v] = isPalindrome(v)
	}

	fmt.Printf("Palindrome Numbers: %#v\n", o)

}
