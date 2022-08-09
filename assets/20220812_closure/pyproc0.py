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
    def cal(self):
        for rule in self.rules:
            name1 = rule['name1']
            name2 = rule['name2']
            name3 = rule['name3']
            rule = rule['rule']
            if rule == '*':
                self.values[name3] = self.values[name1] * self.values[name2]
            elif rule == '+':
                self.values[name3] = self.values[name1] + self.values[name2]
            elif rule == '-':
                self.values[name3] = self.values[name1] - self.values[name2]
            elif rule == '|':
                self.values[name3] = self.values[name1] | self.values[name2]
            elif rule == '^':
                self.values[name3] = self.values[name1] ^ self.values[name2]
            elif rule == '&':
                self.values[name3] = self.values[name1] & self.values[name2]

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
