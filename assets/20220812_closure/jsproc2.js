class Field {
    constructor(name, value) {
        this.name = name
        this.value = value
    }
}

class Calculator {
    constructor(rules) {
        this.rules = rules
        this.fields = {}
        for (let rule of rules) {
            if (!Object.keys(this.fields).some(key => key === rule.name1)) {
                this.fields[rule.name1] = new Field(rule.name1, 1)
            }
            if (!Object.keys(this.fields).some(key => key === rule.name2)) {
                this.fields[rule.name2] = new Field(rule.name2, 1)
            }
            if (!Object.keys(this.fields).some(key => key === rule.name3)) {
                this.fields[rule.name3] = new Field(rule.name3, 1)
            }
        }
        this.funcs = []
        for (let rule of rules) {
            const name1 = rule.name1
            const name2 = rule.name2
            const name3 = rule.name3
            const field1 = this.fields[name1]
            const field2 = this.fields[name2]
            const field3 = this.fields[name3]
            switch (rule.rule) {
                case '*':
                    this.funcs.push(() => {
                        field3.value = field1.value * field2.value
                    })
                    break
                case '+':
                    this.funcs.push(() => {
                        field3.value = field1.value + field2.value
                    })
                    break
                case '-':
                    this.funcs.push(() => {
                        field3.value = field1.value - field2.value
                    })
                    break
                case '|':
                    this.funcs.push(() => {
                        field3.value = field1.value | field2.value
                    })
                    break
                case '^':
                    this.funcs.push(() => {
                        field3.value = field1.value ^ field2.value
                    })
                    break
                case '&':
                    this.funcs.push(() => {
                        field3.value = field1.value & field2.value
                    })
                    break
            }
        }
    }
    cal() {
        for (let func of this.funcs) {
            func()
        }
    }
}

function main() {
    fs = require('fs')
    const rules = JSON.parse(fs.readFileSync('./rules.json', 'utf8'))

    let ct = Date.now()
    const calc = new Calculator(rules)
    console.log((Date.now() - ct) / 1000)
    ct = Date.now()
    calc.cal()
    console.log((Date.now() - ct) / 1000)
    ct = Date.now()
    calc.cal()
    console.log((Date.now() - ct) / 1000)
    ct = Date.now()
    calc.cal()
    console.log((Date.now() - ct) / 1000)

    console.log(calc.fields["validation"].value)
}

main()
