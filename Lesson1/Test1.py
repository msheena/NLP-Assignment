import random
siri_rules='''
siri=hello question|chat|answer
hello=你好|您好|hola|hi
question=May I help you|What can I do for you|请问有什么需要帮助的吗
chat=今天天气真好呀|您今天气色不错|吃过了没
answer=你说的什么我听不懂|I don't know|这是个好主意
'''

client_rules='''
打招呼=你好|早上好
聊天=你吃早饭了吗|唱个歌吧|今天是几号
'''

def generate(grammar_rule, target):
    if target in grammar_rule:
        candidates = grammar_rule[target]
        candidate = random.choice(candidates)
        return ' '.join(generate(grammar_rule, target=c) for c in candidate.split())
    else:
        return target


def get_generation_by_gram(grammar_str: str, target, stmt_split='=', or_split='|'):
    rules=generate_rules(grammar_str,stmt_split,or_split)
    generated = generate(rules, target)
    return generated

def generate_rules(grammar_str:str, stmt_split='=', or_split='|'):
    rules = {}
    for line in grammar_str.split('\n'):
        if not line: continue
        stmt, expr = line.split(stmt_split)
        rules[stmt] = expr.split(or_split)
    return rules

def generate_n():
    rules_str = [siri_rules, client_rules]
    for i in range(1, 11):
        rule = random.choice(rules_str)
        rules = generate_rules(rule)
        statment = random.choice(list(rules.keys()))
        print(generate(statment, random.choice(rules[statment])))
        if i % 2 == 0:
            print("\n")




generate_n()