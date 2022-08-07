package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"time"
)

type Rule struct {
	Name1 string
	Name2 string
	Name3 string
	Rule  string
}

type Calculater struct {
	Rules  []*Rule
	Values map[string]int
}

func Constuctor(rules []*Rule) *Calculater {
	self := &Calculater{Rules: rules, Values: make(map[string]int)}
	for _, rule := range rules {
		self.Values[rule.Name1] = 1
		self.Values[rule.Name2] = 1
		self.Values[rule.Name3] = 1
	}
	return self
}

func (self *Calculater) Cal() {
	for _, rule := range self.Rules {
		name1 := rule.Name1
		name2 := rule.Name2
		name3 := rule.Name3
		switch rule.Rule {
		case "*":
			self.Values[name3] = self.Values[name1] * self.Values[name2]
		case "+":
			self.Values[name3] = self.Values[name1] + self.Values[name2]
		case "-":
			self.Values[name3] = self.Values[name1] - self.Values[name2]
		case "|":
			self.Values[name3] = self.Values[name1] | self.Values[name2]
		case "^":
			self.Values[name3] = self.Values[name1] ^ self.Values[name2]
		case "&":
			self.Values[name3] = self.Values[name1] & self.Values[name2]
		}
	}
}

func main() {
	jsonFile, err := os.Open("rules.json")
	if err != nil {
		panic(err)
	}
	byteValue, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		panic(err)
	}
	rules := []*Rule{}
	if err = json.Unmarshal(byteValue, &rules); err != nil {
		panic(err)
	}

	ct := time.Now()
	calculator := Constuctor(rules)
	fmt.Println(time.Since(ct).Seconds())
	ct = time.Now()
	calculator.Cal()
	fmt.Println(time.Since(ct).Seconds())
	ct = time.Now()
	calculator.Cal()
	fmt.Println(time.Since(ct).Seconds())
	ct = time.Now()
	calculator.Cal()
	fmt.Println(time.Since(ct).Seconds())

	fmt.Println(calculator.Values["validation"])
}
