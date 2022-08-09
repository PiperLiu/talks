#include "json/json.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <time.h>

struct Rule {
    std::string name1;
    std::string name2;
    std::string name3;
    std::string rule;
};

class Calculator {
public:
    std::vector<std::shared_ptr<Rule>> rules;
    std::map<std::string, int> values;
    Calculator(Json::Value rules)
    {
        for (auto&& rule: rules)
        {
            auto r = std::make_shared<Rule>();
            r->name1 = rule["name1"].asString();
            r->name2 = rule["name2"].asString();
            r->name3 = rule["name3"].asString();
            r->rule = rule["rule"].asString();
            this->rules.push_back(r);
        }
        for (auto&& rule: this->rules)
        {
            this->values[rule->name1] = 1;
            this->values[rule->name2] = 1;
            this->values[rule->name3] = 1;
        }
    }
    void cal()
    {
        for (auto&& rule: this->rules)
        {
            auto name1 = rule->name1;
            auto name2 = rule->name2;
            auto name3 = rule->name3;
            switch (rule->rule[0]) {
                case '*':
                    this->values[name3] = this->values[name1] * this->values[name2];
                    break;
                case '+':
                    this->values[name3] = this->values[name1] + this->values[name2];
                    break;
                case '-':
                    this->values[name3] = this->values[name1] - this->values[name2];
                    break;
                case '|':
                    this->values[name3] = this->values[name1] | this->values[name2];
                    break;
                case '^':
                    this->values[name3] = this->values[name1] ^ this->values[name2];
                    break;
                case '&':
                    this->values[name3] = this->values[name1] & this->values[name2];
                    break;
            }
        }
    }
    virtual ~Calculator() {}
};

int main()
{
    std::ifstream ifs("../../temp/rules.json");
    Json::Value rules;
    Json::Reader reader;
    if (!reader.parse(ifs, rules))
    {
        std::cout << "parse error" << std::endl;
        return 1;
    }

    clock_t ct = clock();
    auto calculator = new Calculator(rules);
    std::printf("%lf\n", (double)(clock() - ct) / CLOCKS_PER_SEC);
    ct = clock();
    calculator->cal();
    std::printf("%lf\n", (double)(clock() - ct) / CLOCKS_PER_SEC);
    ct = clock();
    calculator->cal();
    std::printf("%lf\n", (double)(clock() - ct) / CLOCKS_PER_SEC);
    ct = clock();
    calculator->cal();
    std::printf("%lf\n", (double)(clock() - ct) / CLOCKS_PER_SEC);

    printf("%d\n", calculator->values["validation"]);
}
