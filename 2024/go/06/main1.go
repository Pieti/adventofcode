package main

import (
	"bufio"
	"fmt"
	"os"
)

type Direction int

const (
	Up Direction = iota
	Right
	Down
	Left
)

type Point struct {
	x, y int
}

type Board struct {
	height    int
	width     int
	obstacles map[Point]bool
	guard     Point
	direction Direction
	visited   map[Point]bool
}

func (b *Board) print() {
	for y := 0; y < b.height; y++ {
		for x := 0; x < b.width; x++ {
			p := Point{x, y}
			if b.obstacles[p] {
				fmt.Print("#")
			} else if b.guard == p {
				fmt.Print("^")
			} else if b.visited[p] {
				fmt.Print("X")
			} else {
				fmt.Print(".")
			}
		}
		fmt.Println()
	}
}

func (b *Board) next() Point {
	switch {
	case b.direction == Up:
		return Point{b.guard.x, b.guard.y - 1}
	case b.direction == Right:
		return Point{b.guard.x + 1, b.guard.y}
	case b.direction == Down:
		return Point{b.guard.x, b.guard.y + 1}
	default:
		return Point{b.guard.x - 1, b.guard.y}
	}
}

func (b *Board) run() map[Point]bool {
	for {
		next := b.next()
		if b.guard.x < 0 || b.guard.x >= b.width || b.guard.y < 0 || b.guard.y >= b.height {
			return b.visited
		}

		if _, ok := b.obstacles[next]; ok {
			b.direction = (b.direction + 1) % 4
		} else {
			b.visited[b.guard] = true
			b.guard = next
		}
	}
}

func main() {
	b := parseInput()
	visited := b.run()
	fmt.Println(len(visited))
}

func parseInput() Board {
	scanner := bufio.NewScanner(os.Stdin)

	b := Board{}
	b.obstacles = make(map[Point]bool)
	b.visited = make(map[Point]bool)

	var width, height int
	for scanner.Scan() {
		line := scanner.Text()
		width = len(line)

		for i, c := range line {
			switch {
			case c == '#':
				b.obstacles[Point{i, height}] = true
			case c == '^':
				b.guard = Point{i, height}
			}
		}
		height++
	}
	b.width = width
	b.height = height

	return b
}
