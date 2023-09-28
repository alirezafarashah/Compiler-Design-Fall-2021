terminals = ['$', 'ID', ';', '[', 'NUM', ']', '(', ')', 'int', 'void', ',', '{', '}', 'break', 'if', 'endif', 'else',
             'repeat', 'until', 'return', '=', '<', '==', '+', '-', '*']
first = {'Program': ['$', 'int', 'void'], 'Declaration-list': ['int', 'void', 'epsilon'],
         'Declaration': ['int', 'void'], 'Declaration-initial': ['int', 'void'], 'Declaration-prime': [';', '[', '('],
         'Var-declaration-prime': [';', '['], 'Fun-declaration-prime': ['('], 'Type-specifier': ['int', 'void'],
         'Params': ['int', 'void'], 'Param-list': [',', 'epsilon'], 'Param': ['int', 'void'],
         'Param-prime': ['[', 'epsilon'], 'Compound-stmt': ['{'],
         'Statement-list': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return', 'epsilon'],
         'Statement': ['ID', ';', 'NUM', '(', '{', 'break', 'if', 'repeat', 'return'],
         'Expression-stmt': ['ID', ';', 'NUM', '(', 'break'], 'Selection-stmt': ['if'], 'Else-stmt': ['endif', 'else'],
         'Iteration-stmt': ['repeat'], 'Return-stmt': ['return'], 'Return-stmt-prime': ['ID', ';', 'NUM', '('],
         'Expression': ['ID', 'NUM', '('], 'B': ['[', '(', '=', '<', '==', '+', '-', '*', 'epsilon'],
         'H': ['=', '<', '==', '+', '-', '*', 'epsilon'], 'Simple-expression-zegond': ['NUM', '('],
         'Simple-expression-prime': ['(', '<', '==', '+', '-', '*', 'epsilon'], 'C': ['<', '==', 'epsilon'],
         'Relop': ['<', '=='], 'Additive-expression': ['ID', 'NUM', '('],
         'Additive-expression-prime': ['(', '+', '-', '*', 'epsilon'], 'Additive-expression-zegond': ['NUM', '('],
         'D': ['+', '-', 'epsilon'], 'Addop': ['+', '-'], 'Term': ['ID', 'NUM', '('],
         'Term-prime': ['(', '*', 'epsilon'], 'Term-zegond': ['NUM', '('], 'G': ['*', 'epsilon'],
         'Factor': ['ID', 'NUM', '('], 'Var-call-prime': ['[', '(', 'epsilon'], 'Var-prime': ['[', 'epsilon'],
         'Factor-prime': ['(', 'epsilon'], 'Factor-zegond': ['NUM', '('], 'Args': ['ID', 'NUM', '(', 'epsilon'],
         'Arg-list': ['ID', 'NUM', '('], 'Arg-list-prime': [',', 'epsilon']}

follow = {'Program': [''],
          'Declaration-list': ['$', 'ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'repeat', 'return'],
          'Declaration': ['$', 'ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return'],
          'Declaration-initial': [';', '[', '(', ')', ','],
          'Declaration-prime': ['$', 'ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat', 'return'],
          'Var-declaration-prime': ['$', 'ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat',
                                    'return'],
          'Fun-declaration-prime': ['$', 'ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'repeat',
                                    'return'], 'Type-specifier': ['ID'], 'Params': [')'], 'Param-list': [')'],
          'Param': [')', ','], 'Param-prime': [')', ','],
          'Compound-stmt': ['$', 'ID', ';', 'NUM', '(', 'int', 'void', '{', '}', 'break', 'if', 'endif', 'else',
                            'repeat', 'until', 'return'], 'Statement-list': ['}'],
          'Statement': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'endif', 'else', 'repeat', 'until', 'return'],
          'Expression-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'endif', 'else', 'repeat', 'until',
                              'return'],
          'Selection-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'endif', 'else', 'repeat', 'until',
                             'return'],
          'Else-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'endif', 'else', 'repeat', 'until', 'return'],
          'Iteration-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'endif', 'else', 'repeat', 'until',
                             'return'],
          'Return-stmt': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'endif', 'else', 'repeat', 'until', 'return'],
          'Return-stmt-prime': ['ID', ';', 'NUM', '(', '{', '}', 'break', 'if', 'endif', 'else', 'repeat', 'until',
                                'return'], 'Expression': [';', ']', ')', ','], 'B': [';', ']', ')', ','],
          'H': [';', ']', ')', ','], 'Simple-expression-zegond': [';', ']', ')', ','],
          'Simple-expression-prime': [';', ']', ')', ','], 'C': [';', ']', ')', ','], 'Relop': ['ID', 'NUM', '('],
          'Additive-expression': [';', ']', ')', ','], 'Additive-expression-prime': [';', ']', ')', ',', '<', '=='],
          'Additive-expression-zegond': [';', ']', ')', ',', '<', '=='], 'D': [';', ']', ')', ',', '<', '=='],
          'Addop': ['ID', 'NUM', '('], 'Term': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Term-prime': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Term-zegond': [';', ']', ')', ',', '<', '==', '+', '-'], 'G': [';', ']', ')', ',', '<', '==', '+', '-'],
          'Factor': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Var-call-prime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Var-prime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Factor-prime': [';', ']', ')', ',', '<', '==', '+', '-', '*'],
          'Factor-zegond': [';', ']', ')', ',', '<', '==', '+', '-', '*'], 'Args': [')'], 'Arg-list': [')'],
          'Arg-list-prime': [')']}


def is_terminal(element):
    return element in terminals


f = open("grammer.txt")
dictionary = {}
action_dict = {}
lhs_to_start_state = {}
lhs_to_final_state = {}
state = 0
for line in f.readlines():
    LHS, productions = line.split("->")
    current_start_state = state
    LHS = LHS.strip()
    lhs_to_start_state[LHS] = current_start_state
    final_first_time = True
    all_productions = productions.split("|")
    for production in all_productions:
        first_time = True
        elements = production.strip().split()
        l = []
        for i in range(len(elements)):
            if elements[i].startswith("%") or elements[i].startswith("#"):
                l.append(elements[i])
                continue
            if i == len(elements) - 1 and not final_first_time:
                next_state = last_state
            else:
                next_state = state + 1
            if first_time:
                correct_state = current_start_state
                first_time = False
            else:
                correct_state = state
            if elements[i] == "epsilon":
                for item in follow[LHS]:
                    dictionary[(correct_state, item)] = ("go", next_state)
                    action_dict[(correct_state, item)] = l
                state += 1
            elif is_terminal(elements[i]):
                dictionary[(correct_state, elements[i])] = ("get", next_state)
                action_dict[(correct_state, elements[i])] = l
                state += 1
            else:
                for item in list(set(first[elements[i]]) - set(list("epsilon"))):
                    dictionary[(correct_state, item)] = ("call", (elements[i], next_state))
                    action_dict[(correct_state, item)] = l
                if "epsilon" in first[elements[i]]:
                    for item in follow[elements[i]]:
                        dictionary[(correct_state, item)] = ("call", (elements[i], next_state))
                        action_dict[(correct_state, item)] = l
                else:
                    for item in follow[elements[i]]:
                        if (correct_state, item) not in dictionary.keys():
                            dictionary[(correct_state, item)] = ("missing", (elements[i], next_state))
                state += 1

            if i == len(elements) - 1 and final_first_time:
                last_state = state
                lhs_to_final_state[LHS] = last_state
            l = []
        final_first_time = False
    if len(all_productions) == 1:
        state += 1



