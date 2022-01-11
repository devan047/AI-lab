Knowledge Base Entailment (Model Checking Algorithm)
Ajay Mittur 1BM18CS006

def processRule(rule):
    rule = rule.replace('~', ' not ')
    rule = rule.replace('^', ' and ')
    rule = rule.replace('v', ' or ')
    return rule

def formatRule(rule, P, Q, R):
    P, Q, R = str(P), str(Q), str(R)
    rule = rule.replace('P', P)
    rule = rule.replace('Q', Q)
    rule = rule.replace('R', R)
    return rule
def checkEntailment(rule, query):
    models = [
        (False, False, False),
        (False, False, True),
        (False, True, False),
        (False, True, True),
        (True, False, False),
        (True, False, True),
        (True, True, False),
        (True, True, True)
    ]
    rule = processRule(rule)
    entails = True

    for P, Q, R in models:
        formattedRule = formatRule(rule, P, Q, R) 
        print(f'Evaluating: {formattedRule}')
        KB = eval(formattedRule)
        _query = R if query == 'R' else P if query == 'P' else Q
        print(f'Knowledge Base: {KB}      Query: {_query}')
        if KB:
            entails &= KB and _query

    if entails:
        print('Knowledge Base entails the query')
    else:
        print("Knowledge Base doesn't entail the query")
rule = input('Enter the rule: ')
# (~Qv~PvR)^(~Q^P)^Q
query = input('Enter the query: ')
# R

checkEntailment(rule, query)
Enter the rule: (~Qv~PvR)^(~Q^P)^Q
Enter the query: R
Evaluating: ( not False or  not False or False) and ( not False and False) and False
Knowledge Base: False      Query: False
Evaluating: ( not False or  not False or True) and ( not False and False) and False
Knowledge Base: False      Query: True
Evaluating: ( not True or  not False or False) and ( not True and False) and True
Knowledge Base: False      Query: False
Evaluating: ( not True or  not False or True) and ( not True and False) and True
Knowledge Base: False      Query: True
Evaluating: ( not False or  not True or False) and ( not False and True) and False
Knowledge Base: False      Query: False
Evaluating: ( not False or  not True or True) and ( not False and True) and False
Knowledge Base: False      Query: True
Evaluating: ( not True or  not True or False) and ( not True and True) and True
Knowledge Base: False      Query: False
Evaluating: ( not True or  not True or True) and ( not True and True) and True
Knowledge Base: False      Query: True
Knowledge Base entails the query
rule = input('Enter the rule: ')
# (P^~Q) => R
# ~(P^~Q)vR
query = input('Enter the query: ')
# R

checkEntailment(rule, query)
Enter the rule: ~(P^~Q)vR
Enter the query: R
Evaluating:  not (False and  not False) or False
Knowledge Base: True      Query: False
Evaluating:  not (False and  not False) or True
Knowledge Base: True      Query: True
Evaluating:  not (False and  not True) or False
Knowledge Base: True      Query: False
Evaluating:  not (False and  not True) or True
Knowledge Base: True      Query: True
Evaluating:  not (True and  not False) or False
Knowledge Base: False      Query: False
Evaluating:  not (True and  not False) or True
Knowledge Base: True      Query: True
Evaluating:  not (True and  not True) or False
Knowledge Base: True      Query: False
Evaluating:  not (True and  not True) or True
Knowledge Base: True      Query: True
Knowledge Base doesn't entail the query
rule = input('Enter the rule: ')
# (PvQ)^(~RvP)
query = input('Enter the query: ')
# R

checkEntailment(rule, query)
Enter the rule: (PvQ)^(~RvP)
Enter the query: R
Evaluating: (False or False) and ( not False or False)
Knowledge Base: False      Query: False
Evaluating: (False or False) and ( not True or False)
Knowledge Base: False      Query: True
Evaluating: (False or True) and ( not False or False)
Knowledge Base: True      Query: False
Evaluating: (False or True) and ( not True or False)
Knowledge Base: False      Query: True
Evaluating: (True or False) and ( not False or True)
Knowledge Base: True      Query: False
Evaluating: (True or False) and ( not True or True)
Knowledge Base: True      Query: True
Evaluating: (True or True) and ( not False or True)
Knowledge Base: True      Query: False
Evaluating: (True or True) and ( not True or True)
Knowledge Base: True      Query: True
Knowledge Base doesn't entail the query
 
