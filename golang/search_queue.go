package main

import (
	"fmt"
	"strings"
)

var graph = map[string][]string{
	"you":    {"alice", "bob", "claire"},
	"bob":    {"anuj", "peggy"},
	"alice":  {"peggy"},
	"claire": {"thom", "jonny"},
	"anuj":   {},
	"peggy":  {},
	"thom":   {},
	"jonny":  {},
}

func search(name string) bool {
	search_queue := []string{}
	search_queue = append(search_queue, graph[name]...)
	searched := make(map[string]bool, 0)

	for len(search_queue) != 0 {
		var person string
		person, search_queue = search_queue[0], search_queue[1:]

		if searched[person] {
			continue
		}

		if personIsSeller(person) {
			fmt.Println(person + " is a mango seller!")
			return true
		} else {
			search_queue = append(search_queue, graph[person]...)
			searched[person] = true
		}
	}

	return false
}

func personIsSeller(name string) bool {
	return strings.HasSuffix(name, "m")
}

func callSearch() {
	search("you")
}
