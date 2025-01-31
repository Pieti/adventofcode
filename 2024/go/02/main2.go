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

	score := 0
	for scanner.Scan() {
		var report []int
		parts := strings.Fields(scanner.Text())
		for _, n := range parts {
			level, _ := strconv.Atoi(n)
			report = append(report, level)
		}
		if isSafe(report) {
			score++
		} else {
			for i := 0; i < len(report); i++ {
				newReport := append([]int{}, report[:i]...)
				newReport = append(newReport, report[i+1:]...)
				if isSafe(newReport) {
					score++
					break
				}
			}
		}

	}

	fmt.Println(score)
}

func isSafe(report []int) bool {
	minDiff := 1
	maxDiff := 3

	if report[1]-report[0] < 0 {
		minDiff = -3
		maxDiff = -1
	}

	for i := 1; i < len(report); i++ {
		diff := report[i] - report[i-1]
		if diff < minDiff || diff > maxDiff {
			return false
		}
	}
	return true
}
