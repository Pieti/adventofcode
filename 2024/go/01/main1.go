package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var left, right []int
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		lnum, _ := strconv.Atoi(parts[0])
		rnum, _ := strconv.Atoi(parts[1])

		left = append(left, lnum)
		right = append(right, rnum)
	}

	sort.Ints(left)
	sort.Ints(right)

	dist := 0
	for i := 0; i < len(left); i++ {
		dist += abs(left[i] - right[i])
	}
	fmt.Println(dist)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
