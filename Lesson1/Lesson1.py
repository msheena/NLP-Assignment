import random

hello_rules = '''
say_hello = names hello tail
names = name names | name
name = Jhon | Mike | 老梁
hello = 您好 | 您来了 | 快请进
tail = 呀 | !
'''

simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => Adj | Adj Adj*
verb_phrase => verb noun_phrase
Article =>  一个 | 这个
noun =>   女人 |  篮球 | 桌子 | 小猫
verb => 看着   |  坐在 |  听着 | 看见
Adj =>   蓝色的 |  好看的 | 小小的"""

# rules={}
# for line in hello_rules.split("\n"):
#     if not line:
#         continue
#     stmt,expr=line.split(" = ")
#     # print(stmt,expr.split(" | "))
#     rules[stmt.strip()]=expr.split(" | ")

# print(rules['name'])

def generate1(grammer_rule,target):
    if target in grammer_rule:
        candidates=grammer_rule[target]
        candidate=random.choice(candidates)
        return ' '.join(generate1(grammer_rule,target=c.strip()) for c in candidate.split())
    else:
        return target

# print(generate(rules,'say_hello'))

def generate_by_grammer(gram_stmt:str,target,stmt_split):
    rules={}
    for line in gram_stmt.split("\n"):
        if not line:
            continue
        stmt, expr = line.split(stmt_split)
        rules[stmt.strip()] = expr.split(" | ")
    return generate1(rules,target=target)


print(generate_by_grammer(simple_grammar,"sentence",'=>'))


