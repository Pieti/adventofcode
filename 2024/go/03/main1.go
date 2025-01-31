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

	re := regexp.MustCompile(`mul\(([0-9]{1,3}),([0-9]{1,3})\)`)
	expressions := re.FindAllStringSubmatch(text, -1)

	sum := 0
	for _, x := range expressions {
		a, _ := strconv.Atoi(x[1])
		b, _ := strconv.Atoi(x[2])
		sum += a * b
	}

	fmt.Println(sum)
}
