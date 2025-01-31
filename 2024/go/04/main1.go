package main

import (
	"bufio"
	"fmt"
	"os"
)

var word = "XMAS"
var text []string

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		text = append(text, scanner.Text())
	}

	count := 0
	for y := 0; y < len(text); y++ {
		for x := 0; x < len(text[y]); x++ {
			for dy := -1; dy <= 1; dy++ {
				for dx := -1; dx <= 1; dx++ {
					if isXMAS(x, y, dx, dy) {
						count++
					}
				}
			}
		}
	}

	fmt.Println(count)

}

func isXMAS(x, y, dx, dy int) bool {
	for count := 0; count < len(word); count++ {
		curX := x + count*dx
		curY := y + count*dy

		if curY < 0 || curY >= len(text) {
			return false
		}

		if curX < 0 || curX >= len(text[curY]) {
			return false
		}

		if text[curY][curX] != word[count] {
			return false
		}
	}
	return true
}
