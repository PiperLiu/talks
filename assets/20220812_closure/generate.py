import random
import json

NAMES = 1500
LENGTH = 100
RULES = 500000

def generate_random_str(length=16):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    for _ in range(length):
        random_str += base_str[random.randint(0, len(base_str) - 1)]
    return random_str

if __name__ == '__main__':
    names = [generate_random_str(LENGTH) for _ in range(NAMES)]
    names.append("validation")
    rules = [] # [{name1: x, name2: x, name3: x, rule: t}]
    for _ in range(RULES):
        name1 = random.choice(names)
        name2 = random.choice(names)
        name3 = random.choice(names)
        rule = random.choice(['+', '-', '|', '^', '&'])
        rules.append({
            'name1': name1,
            'name2': name2,
            'name3': name3,
            'rule': rule
        })
    with open('../../temp/rules.json', 'w') as f:
        json.dump(rules, f)
