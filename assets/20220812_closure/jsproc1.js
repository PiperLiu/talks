class Calculator {
    constructor(rules) {
        this.rules = rules
        this.values = {}
        for (let rule of rules) {
            this.values[rule.name1] = 1
            this.values[rule.name2] = 1
            this.values[rule.name3] = 1
        }
        this.funcs = []
        for (let rule of rules) {
            const name1 = rule.name1
            const name2 = rule.name2
            const name3 = rule.name3
            switch (rule.rule) {
                case '*':
                    this.funcs.push(() => {
                        this.values[name3] = this.values[name1] * this.values[name2]
                    })
                    break
                case '+':
                    this.funcs.push(() => {
                        this.values[name3] = this.values[name1] + this.values[name2]
                    })
                    break
                case '-':
                    this.funcs.push(() => {
                        this.values[name3] = this.values[name1] - this.values[name2]
                    })
                    break
                case '|':
                    this.funcs.push(() => {
                        this.values[name3] = this.values[name1] | this.values[name2]
                    })
                    break
                case '^':
                    this.funcs.push(() => {
                        this.values[name3] = this.values[name1] ^ this.values[name2]
                    })
                    break
                case '&':
                    this.funcs.push(() => {
                        this.values[name3] = this.values[name1] & this.values[name2]
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
    const rules = JSON.parse(fs.readFileSync('./../../temp/rules.json', 'utf8'))

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

    console.log(calc.values["validation"])
}

main()
