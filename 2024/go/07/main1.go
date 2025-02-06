package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type equation struct {
	result int
	values []int
}

func isValid(result, left int, right []int) bool {
	if len(right) == 0 {
		return left == result
	}

	if isValid(result, left+right[0], right[1:]) {
		return true
	}

	return isValid(result, left*right[0], right[1:])
}

func main() {
	equations := parseInput()
	var sum int
	for _, e := range equations {
		if isValid(e.result, e.values[0], e.values[1:]) {
			sum += e.result
		}
	}
	fmt.Println(sum)
}

func parseInput() []equation {
	var equations []equation
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, ":")
		result, _ := strconv.Atoi(split[0])
		var values []int
		for _, i := range strings.Fields(split[1]) {
			value, _ := strconv.Atoi(i)
			values = append(values, value)
		}
		equations = append(equations, equation{result: result, values: values})
	}
	return equations
}
