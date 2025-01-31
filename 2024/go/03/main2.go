package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	text := ""
	for scanner.Scan() {
		text += scanner.Text()
	}

	re := regexp.MustCompile(`mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\)`)
	expressions := re.FindAllStringSubmatch(text, -1)

	sum := 0
	enabled := true
	for _, x := range expressions {
		switch {
		case x[0] == "don't()":
			enabled = false
		case x[0] == "do()":
			enabled = true
		default:
			if enabled {
				a, _ := strconv.Atoi(x[1])
				b, _ := strconv.Atoi(x[2])
				sum += a * b
			}
		}
	}

	fmt.Println(sum)
}
