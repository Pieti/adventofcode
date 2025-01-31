package main

import (
	"bufio"
	"fmt"
	"os"
)

var text []string

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		text = append(text, scanner.Text())
	}

	count := 0
	for y := 1; y < len(text)-1; y++ {
		for x := 1; x < len(text[y])-1; x++ {
			if isXMAS(x, y) {
				count++
			}
		}
	}

	fmt.Println(count)

}

func isXMAS(x, y int) bool {
	if text[y][x] != 'A' {
		return false
	}

	corners := string([]byte{text[y-1][x-1], text[y+1][x+1], text[y-1][x+1], text[y+1][x-1]})

	return corners == "SMMS" || corners == "MSMS" || corners == "SMSM" || corners == "MSSM"
}
