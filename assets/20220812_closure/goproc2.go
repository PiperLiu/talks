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
	Values map[string]*int
	Funcs  []func()
}

func Constuctor(rules []*Rule) *Calculater {
	self := &Calculater{Rules: rules, Values: make(map[string]*int)}
	values := make([]int, len(rules))
	cnt := 0
	for _, rule := range rules {
		if _, ok := self.Values[rule.Name1]; !ok {
			values[cnt] = 1
			self.Values[rule.Name1] = &values[cnt]
			cnt++
		}
		if _, ok := self.Values[rule.Name2]; !ok {
			values[cnt] = 1
			self.Values[rule.Name2] = &values[cnt]
			cnt++
		}
		if _, ok := self.Values[rule.Name3]; !ok {
			values[cnt] = 1
			self.Values[rule.Name3] = &values[cnt]
			cnt++
		}
	}
	// init funcs
	self.Funcs = []func(){}
	for _, rule := range self.Rules {
		name1 := rule.Name1
		name2 := rule.Name2
		name3 := rule.Name3
		pValue1 := self.Values[name1]
		pValue2 := self.Values[name2]
		pValue3 := self.Values[name3]
		switch rule.Rule {
		case "*":
			self.Funcs = append(self.Funcs, func() {
				*pValue3 = *pValue1 * *pValue2
			})
		case "+":
			self.Funcs = append(self.Funcs, func() {
				*pValue3 = *pValue1 + *pValue2
			})
		case "-":
			self.Funcs = append(self.Funcs, func() {
				*pValue3 = *pValue1 - *pValue2
			})
		case "|":
			self.Funcs = append(self.Funcs, func() {
				*pValue3 = *pValue1 | *pValue2
			})
		case "^":
			self.Funcs = append(self.Funcs, func() {
				*pValue3 = *pValue1 ^ *pValue2
			})
		case "&":
			self.Funcs = append(self.Funcs, func() {
				*pValue3 = *pValue1 & *pValue2
			})
		}
	}

	return self
}

func (self *Calculater) Cal() {
	for _, f := range self.Funcs {
		f()
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

	fmt.Println(*calculator.Values["validation"])
}
