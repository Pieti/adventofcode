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

type Visit struct {
	p Point
	d Direction
}

type Board struct {
	height    int
	width     int
	obstacles map[Point]bool
	start     Point
	guard     Point
	direction Direction
	visited   map[Point]bool
}

func (b *Board) reset() {
	b.guard = b.start
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

func (b *Board) simulate(obstruction Point) bool {
	if obstruction == b.guard {
		return false
	}

	if _, ok := b.obstacles[obstruction]; ok {
		return false
	}
	b.obstacles[obstruction] = true
	defer func() {
		delete(b.obstacles, obstruction)
	}()

	visits := make(map[Visit]bool)

	for {
		next := b.next()
		if b.guard.x < 0 || b.guard.x >= b.width || b.guard.y < 0 || b.guard.y >= b.height {
			return false
		}

		if _, ok := b.obstacles[next]; ok {
			b.direction = (b.direction + 1) % 4
		} else {
			b.guard = next
		}

		visit := Visit{b.guard, b.direction}
		if _, ok := visits[visit]; ok {
			return true
		}
		visits[visit] = true
	}
}

func main() {
	b := parseInput()
	start := b.guard
	visited := b.run()
	b.guard = start

	var count int
	for obstruction, _ := range visited {
		if b.simulate(obstruction) {
			count++
		}
		b.guard = b.start
		b.direction = Up
		delete(b.obstacles, obstruction)
	}

	fmt.Println(count)
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
	b.start = b.guard

	return b
}
