import json
import time

class Field:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

class Calculator:
    def __init__(self, rules) -> None:
        self.rules = rules
        self.fields = {}
        for rule in self.rules:
            if rule['name1'] not in self.fields:
                self.fields[rule['name1']] = Field(rule['name1'], 1)
            if rule['name2'] not in self.fields:
                self.fields[rule['name2']] = Field(rule['name2'], 1)
            if rule['name3'] not in self.fields:
                self.fields[rule['name3']] = Field(rule['name3'], 1)
        self.funcs = []
        for rule in rules:
            name1 = rule['name1']
            name2 = rule['name2']
            name3 = rule['name3']
            rule = rule['rule']
            field1 = self.fields[name1]
            field2 = self.fields[name2]
            field3 = self.fields[name3]
            if rule == '*':
                # python 循环没有域的概念
                def makefunc(field1, field2, field3):
                    def func():
                        field3.value = field1.value * field2.value
                    return func
                self.funcs.append(makefunc(field1, field2, field3))
            elif rule == '+':
                def makefunc(field1, field2, field3):
                    def func():
                        field3.value = field1.value + field2.value
                    return func
                self.funcs.append(makefunc(field1, field2, field3))
            elif rule == '-':
                def makefunc(field1, field2, field3):
                    def func():
                        field3.value = field1.value - field2.value
                    return func
                self.funcs.append(makefunc(field1, field2, field3))
            elif rule == '|':
                def makefunc(field1, field2, field3):
                    def func():
                        field3.value = field1.value | field2.value
                    return func
                self.funcs.append(makefunc(field1, field2, field3))
            elif rule == '^':
                def makefunc(field1, field2, field3):
                    def func():
                        field3.value = field1.value ^ field2.value
                    return func
                self.funcs.append(makefunc(field1, field2, field3))
            elif rule == '&':
                def makefunc(field1, field2, field3):
                    def func():
                        field3.value = field1.value & field2.value
                    return func
                self.funcs.append(makefunc(field1, field2, field3))

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

    print(calculator.fields["validation"].value)
