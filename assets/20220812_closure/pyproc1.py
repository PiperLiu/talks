import json
import time

class Calculator:
    def __init__(self, rules) -> None:
        self.rules = rules
        self.values = {}
        for rule in self.rules:
            self.values[rule['name1']] = 1
            self.values[rule['name2']] = 1
            self.values[rule['name3']] = 1
        self.funcs = []
        for rule in rules:
            name1 = rule['name1']
            name2 = rule['name2']
            name3 = rule['name3']
            rule = rule['rule']
            if rule == '*':
                # python 循环没有域的概念
                def makefunc(self, name1, name2, name3):
                    def func():
                        self.values[name3] = self.values[name1] * self.values[name2]
                    return func
                self.funcs.append(makefunc(self, name1, name2, name3))
            elif rule == '+':
                def makefunc(self, name1, name2, name3):
                    def func():
                        self.values[name3] = self.values[name1] + self.values[name2]
                    return func
                self.funcs.append(makefunc(self, name1, name2, name3))
            elif rule == '-':
                def makefunc(self, name1, name2, name3):
                    def func():
                        self.values[name3] = self.values[name1] - self.values[name2]
                    return func
                self.funcs.append(makefunc(self, name1, name2, name3))
            elif rule == '|':
                def makefunc(self, name1, name2, name3):
                    def func():
                        self.values[name3] = self.values[name1] | self.values[name2]
                    return func
                self.funcs.append(makefunc(self, name1, name2, name3))
            elif rule == '^':
                def makefunc(self, name1, name2, name3):
                    def func():
                        self.values[name3] = self.values[name1] ^ self.values[name2]
                    return func
                self.funcs.append(makefunc(self, name1, name2, name3))
            elif rule == '&':
                def makefunc(self, name1, name2, name3):
                    def func():
                        self.values[name3] = self.values[name1] & self.values[name2]
                    return func
                self.funcs.append(makefunc(self, name1, name2, name3))

    def cal(self):
        for func in self.funcs:
            func()

if __name__ == '__main__':
    rules = json.load(open('../../temp/rules.json'))

    ct = time.time()
    calculator = Calculator(rules)
    print(time.time() - ct)
    ct = time.time()
    calculator.cal()
    print(time.time() - ct)
    ct = time.time()
    calculator.cal()
    print(time.time() - ct)
    ct = time.time()
    calculator.cal()
    print(time.time() - ct)

    print(calculator.values["validation"])
