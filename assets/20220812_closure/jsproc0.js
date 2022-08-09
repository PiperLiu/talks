class Calculator {
    constructor(rules) {
        this.rules = rules
        this.values = {}
        for (let rule of rules) {
            this.values[rule.name1] = 1
            this.values[rule.name2] = 1
            this.values[rule.name3] = 1
        }
    }
    cal() {
        for (let rule of this.rules) {
            const name1 = rule.name1
            const name2 = rule.name2
            const name3 = rule.name3
            switch (rule.rule) {
                case '*':
                    this.values[name3] = this.values[name1] * this.values[name2]
                    break
                case '+':
                    this.values[name3] = this.values[name1] + this.values[name2]
                    break
                case '-':
                    this.values[name3] = this.values[name1] - this.values[name2]
                    break
                case '|':
                    this.values[name3] = this.values[name1] | this.values[name2]
                    break
                case '^':
                    this.values[name3] = this.values[name1] ^ this.values[name2]
                    break
                case '&':
                    this.values[name3] = this.values[name1] & this.values[name2]
                    break
            }
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

    console.log(calc.values["validation"])
}

main()
