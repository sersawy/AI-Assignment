from utils import *
from logic2 import *

# Question 3
#----------------------3.1----------------------
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates1 = Symbol(f"hates({x}, {y})")
hates2 = Symbol(f"hates({y}, {x})")
knowledge_for_question1 = And(Implication(enemies, And(hates1, hates2)))
print(knowledge_for_question1.formula())


#----------------------3.2----------------------
p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")
knowledge_for_question2 = And(Implication(p , And(q, r)))
print(knowledge_for_question2.formula())