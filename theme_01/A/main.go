package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func SelectionSort(nums []int) {
	n := len(nums)
	for i := 0; i < n-1; i++ {
		maxIndex := i
		for j := i + 1; j < n; j++ {
			if nums[j] > nums[maxIndex] {
				maxIndex = j
			}
		}
		nums[i], nums[maxIndex] = nums[maxIndex], nums[i]
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	if scanner.Scan() {
		text := scanner.Text()
		words := strings.Fields(text)

		var nums []int
		for _, word := range words {
			num, _ := strconv.Atoi(word)
			nums = append(nums, num)
		}

		if len(nums) > 0 {
			SelectionSort(nums)
			for _, num := range nums {
				fmt.Print(num, " ")
			}
			fmt.Println()
		}
	}
}
