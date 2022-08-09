#include "json/json.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <time.h>
#include <functional>

struct Rule {
    std::string name1;
    std::string name2;
    std::string name3;
    std::string rule;
};

class Calculator {
public:
    std::vector<std::shared_ptr<Rule>> rules;
    std::map<std::string, std::vector<int>::iterator> values;
    std::vector<std::function<void()>> funcs;
    std::vector<int> raw;
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
        raw = std::vector<int>(this->rules.size(), 1);
        std::vector<int>::iterator it = raw.begin();
        for (auto&& rule: this->rules)
        {
            if (!this->values.count(rule->name1))
            {
                this->values[rule->name1] = it;
                it++;
            }
            if (!this->values.count(rule->name2))
            {
                this->values[rule->name2] = it;
                it++;
            }
            if (!this->values.count(rule->name3))
            {
                this->values[rule->name3] = it;
                it++;
            }
        }
        for (auto&& rule: this->rules)
        {
            auto name1 = rule->name1;
            auto name2 = rule->name2;
            auto name3 = rule->name3;
            auto it1 = this->values[name1];
            auto it2 = this->values[name2];
            auto it3 = this->values[name3];
            std::function<void()> f;
            switch (rule->rule[0])
            {
                case '*':
                    f = [=]() {
                        *it3 = *it1 * *it2;
                    };
                    this->funcs.push_back(f);
                    break;
                case '+':
                    f = [=]() {
                        *it3 = *it1 + *it2;
                    };
                    this->funcs.push_back(f);
                    break;
                case '-':
                    f = [=]() {
                        *it3 = *it1 - *it2;
                    };
                    this->funcs.push_back(f);
                    break;
                case '|':
                    f = [=]() {
                        *it3 = *it1 | *it2;
                    };
                    this->funcs.push_back(f);
                    break;
                case '^':
                    f = [=]() {
                        *it3 = *it1 ^ *it2;
                    };
                    this->funcs.push_back(f);
                    break;
                case '&':
                    f = [=]() {
                        *it3 = *it1 & *it2;
                    };
                    this->funcs.push_back(f);
                    break;
            }
        }
    }
    void cal()
    {
        for (auto&& func: funcs)
        {
            func();
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

    printf("%d\n", *(calculator->values["validation"]));
}
