package main

import "fmt"

type Parent struct {
	Asdf string
	Fdsa string
}

type Child struct {
	Parent
}

type PointerChild struct {
	*Parent
}
 
func (p Parent) PrintFields() {
	fmt.Println("Asdf:", p.Asdf)
	fmt.Println("Fdsa:", p.Fdsa)
}

func (p *Parent) PrintFieldsPointer() {
	fmt.Println("Asdf:", p.Asdf)
	fmt.Println("Fdsa:", p.Fdsa)
}

func main() {
	// Test case for Child (non-pointer embedding)
	fmt.Println("Testing Child (non-pointer embedding):")
	child := Child{
		Parent: Parent{
			Asdf: "parent_asdf",
			Fdsa: "parent_fdsa",
		},
	}

	// Accessing fields
	fmt.Println("Child.Asdf:", child.Asdf) // Output: parent_asdf
	fmt.Println("Child.Fdsa:", child.Fdsa) // Output: parent_fdsa

	// Modifying the embedded struct's field
	child.Asdf = "new_asdf"
	child.Fdsa = "new_fdsa"

	// Verifying changes
	fmt.Println("Child.Asdf after change:", child.Asdf) // Output: new_asdf
	fmt.Println("Child.Fdsa after change:", child.Fdsa) // Output: new_fdsa

	// Using a method from the embedded struct
	child.PrintFields()
	// Output:
	// Asdf: new_asdf
	// Fdsa: new_fdsa

	// Test case for PointerChild (pointer embedding)
	fmt.Println("\nTesting PointerChild (pointer embedding):")
	parent := &Parent{
		Asdf: "parent_asdf",
		Fdsa: "parent_fdsa",
	}

	pointerChild := PointerChild{
		Parent: parent,
	}

	// Accessing fields
	fmt.Println("PointerChild.Asdf:", pointerChild.Asdf) // Output: parent_asdf
	fmt.Println("PointerChild.Fdsa:", pointerChild.Fdsa) // Output: parent_fdsa

	// Modifying the embedded struct's field
	pointerChild.Asdf = "new_asdf"
	pointerChild.Fdsa = "new_fdsa"

	// Verifying changes
	fmt.Println("PointerChild.Asdf after change:", pointerChild.Asdf) // Output: new_asdf
	fmt.Println("PointerChild.Fdsa after change:", pointerChild.Fdsa) // Output: new_fdsa

	// Using a method from the embedded struct
	pointerChild.PrintFieldsPointer()
	// Output:
	// Asdf: new_asdf
	// Fdsa: new_fdsa
}
