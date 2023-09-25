// You are given two non-empty linked lists representing two non-negative integers.
// The digits are stored in reverse order, and each of their nodes contains a single digit.
// Add the two numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.
// Example 1:
//  Input: l1 = [2,4,3], l2 = [5,6,4]
//  Output: [7,0,8]
//  Explanation: 342 + 465 = 807.
// Example 2:
//  Input: l1 = [0], l2 = [0]
//  Output: [0]
// Example 3:
//  Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
//  Output: [8,9,9,9,0,0,0,1]
// 	Constraints:
//The number of nodes in each linked list is in the range [1, 100].
//0 <= Node.val <= 9
//It is guaranteed that the list represents a number that does not have leading zeros.

package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func link(x []int) *ListNode {
	prev := &ListNode{x[0], nil}
	first := prev

	for i := 1; i < len(x); i++ {
		prev.Next = &ListNode{x[i], nil}
		prev = prev.Next
	}

	return first

}

func (ln *ListNode) show() {
	if ln == nil {
		fmt.Printf("ln nil: %v\n", ln)
	}
	for {
		fmt.Printf("ln.Val = %v, ln.Next = %v\n", ln.Val, ln.Next)
		if ln.Next == nil {
			break
		}
		ln = ln.Next
	}
}

func main() {

	s1 := []int{2, 4, 3}
	s2 := []int{5, 6, 4, 6, 2, 1, 4, 6, 5}

	ll1 := link(s1)
	ll2 := link(s2)

	ll1.show()
	ll2.show()
	//  this is how far i got. the question is confusing so i'm skipping

}
