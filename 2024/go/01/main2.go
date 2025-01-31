package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var left []int
	var right = map[int]int{}

	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		lnum, _ := strconv.Atoi(parts[0])
		rnum, _ := strconv.Atoi(parts[1])

		left = append(left, lnum)
		right[rnum]++
	}

	similarity := 0
	for _, n := range left {
		similarity += n * right[n]
	}
	fmt.Println(similarity)
}
