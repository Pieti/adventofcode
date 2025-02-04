package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Rules map[string][]string

func (rules *Rules) Add(before, after string) {
	rights := (*rules)[before]
	for _, v := range rights {
		if v == after {
			return
		}
	}
	(*rules)[before] = append(rights, after)
}

func (rules Rules) IsValid(update []string) bool {
	for i := 0; i < len(update); i++ {
		toCheck := update[i]
		for j := i + 1; j < len(update); j++ {
			rights := rules[update[j]]
			for _, right := range rights {
				if right == toCheck {
					return false
				}
			}
		}
	}
	return true
}

func main() {
	rules, updates := parseInput()

	sum := 0
	for _, update := range updates {
		if rules.IsValid(update) {
			idx := len(update) / 2
			middle, err := strconv.Atoi(update[idx])
			if err != nil {
				log.Panic()
			}
			sum += middle
		}
	}
	fmt.Println(sum)
}

func parseInput() (Rules, [][]string) {
	scanner := bufio.NewScanner(os.Stdin)

	rules := make(Rules)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}
		split := strings.Split(line, "|")
		rules.Add(split[0], split[1])
	}

	var updates [][]string
	for scanner.Scan() {
		line := scanner.Text()
		update := strings.Split(line, ",")
		updates = append(updates, update)
	}

	return rules, updates
}
