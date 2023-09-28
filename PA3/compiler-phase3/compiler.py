# Alireza Dehghanpour 98101555
# Rouzbeh pirayadi 98101306

from scanner import *
import scanner
from anytree import Node, RenderTree
from action_symbol_table import *

semantic_stack = []
PB = [""] * 1000

PB[0] = '(ASSIGN, #512, 100, )'
PB[1] = '(ASSIGN, #0, 10, )'
PB[2] = '(JP, 9, , )'
PB[3] = '(ADD, 100, #8, 3000)'
PB[4] = '(PRINT, @3000, , )'
PB[5] = '(ADD, 100, #4, 3004)'
PB[6] = '(ASSIGN, @100, 100, )'
PB[7] = '(ASSIGN, @3004, 3008, )'
PB[8] = '(JP, @3008, , )'

WORD_SIZE = 4
scope_stack = [0]
symbol_table = [{"lexeme": "output", "type": "void", "fun/var": "fun", "address": 3}]
lexeme_list = []

arg_pass = False
is_not_main = False

local_memory_pointer = 8
last_local_memory_pointers = []

temp_pointer = 3012
arr_pointer = 5000
globals_pointer = 20000


def find_addr(lexeme):
    for i in range(len(symbol_table) - 1, -1, -1):
        if symbol_table[i]["lexeme"] == lexeme:
            return symbol_table[i]["address"]
    return -1


def get_temp():
    global temp_pointer
    temp_pointer += 4
    return temp_pointer - 4


def ptype(token):
    semantic_stack.append(token[1])


def pid(token):
    semantic_stack.append(token[0][1])


def get_id_addr_rec(token):
    global i
    lexeme = semantic_stack[-2]
    for j in range(len(symbol_table) - 1, -1, -1):
        if symbol_table[j]["lexeme"] == lexeme:
            if symbol_table[j]["fun/var"] == "fun":
                semantic_stack[-2] = symbol_table[j]["address"]
            elif symbol_table[j]["fun/var"] == "global" or symbol_table[j]["fun/var"] == "arr_glob":
                t = get_temp()
                addr = symbol_table[j]["address"]
                PB[i] = f"(ASSIGN, #{addr}, {t})"
                i += 1
                semantic_stack[-2] = f"@{t}"
            else:
                t = get_temp()
                addr = symbol_table[j]["address"]
                PB[i] = f"(ADD, 100, #{addr}, {t})"
                i += 1
                semantic_stack[-2] = f"@{t}"
            break


def declare_fun(token):
    global i, local_memory_pointer, is_not_main
    name = semantic_stack.pop()
    fun_type = semantic_stack.pop()
    symbol_table.append(
        {"lexeme": name, "type": fun_type, "fun/var": "fun", "address": i + 1, "scope": len(scope_stack)})
    lexeme_list.append(name)
    if name != "main":
        is_not_main = True
        semantic_stack.append(i)
        i += 1


def jump_main(token):
    global is_not_main
    if is_not_main:
        line_num = semantic_stack.pop()
        PB[line_num] = f"(JP, {i}, , )"
        is_not_main = False


def declare_var(token):
    global i, globals_pointer, local_memory_pointer
    name = semantic_stack.pop()
    var_type = semantic_stack.pop()
    if scope_stack[-1] == 0:
        g = "global"
        addr = globals_pointer
        globals_pointer += 4
    else:
        g = "var"
        addr = local_memory_pointer
        local_memory_pointer += 4
    symbol_table.append({"lexeme": name, "type": var_type, "fun/var": g, "address": addr, "scope": len(scope_stack)})
    lexeme_list.append(name)


def psize(token):
    semantic_stack.append(int(token[0][1]))


def pnum(token):
    global i
    t = get_temp()
    PB[i] = f"(ASSIGN, #{token[0][1]}, {t}, )"
    i += 1
    semantic_stack.append(t)


def declare_arr(token):
    global i, globals_pointer, arr_pointer, local_memory_pointer
    arr_size = semantic_stack.pop()
    name = semantic_stack.pop()
    var_type = semantic_stack.pop()

    if scope_stack[-1] == 0:
        addr = globals_pointer
        globals_pointer += 4
        lexeme_list.append(name)
        t = get_temp()
        PB[i] = f"(ASSIGN, #{addr}, {t})"
        i += 1
        PB[i] = f"(ASSIGN, #{arr_pointer}, @{t}, )"
        i += 1
        arr_pointer += 4 * arr_size
        symbol_table.append(
            {"lexeme": name, "type": var_type, "fun/var": "arr_glob", "address": addr, "scope": len(scope_stack)})
    else:
        addr = local_memory_pointer
        local_memory_pointer += 4
        lexeme_list.append(name)
        t = get_temp()
        PB[i] = f"(ADD, 100, #{addr}, {t})"
        i += 1
        PB[i] = f"(ASSIGN, #{arr_pointer}, @{t}, )"
        i += 1
        arr_pointer += 4 * arr_size
        symbol_table.append(
            {"lexeme": name, "type": var_type, "fun/var": "arr", "address": addr, "scope": len(scope_stack)})


def inc_scope(token):
    global local_memory_pointer
    local_memory_pointer = 8
    scope_stack.append(len(symbol_table))


def declare_par(token, g):
    global i, globals_pointer, local_memory_pointer
    name = semantic_stack.pop()
    var_type = semantic_stack.pop()
    addr = local_memory_pointer
    local_memory_pointer += 4
    symbol_table.append({"lexeme": name, "type": var_type, "fun/var": g, "address": addr, "scope": len(scope_stack)})
    lexeme_list.append(name)


def declare_par_var(token):
    declare_par(token, "param_var")


def declare_par_arr(token):
    declare_par(token, "param_arr")


def return_void(token):
    global i
    if is_not_main:
        temp1_addr = get_temp()
        PB[i] = f"(ADD, 100, #4, {temp1_addr})"
        i += 1
        PB[i] = f"(ASSIGN, @100, 100, )"
        i += 1
        temp2_addr = get_temp()
        PB[i] = f"(ASSIGN, @{temp1_addr}, {temp2_addr}, )"
        i += 1
        PB[i] = f"(JP, @{temp2_addr}, , )"
        i += 1


def dec_scope(token):
    global lexeme_list, symbol_table
    last_scope_addr = scope_stack.pop()
    lexeme_list = lexeme_list[:last_scope_addr]
    symbol_table = symbol_table[:last_scope_addr]


def pop_expression(token):
    semantic_stack.pop()


def breakj(token):
    global i
    repeat_line = find_addr("repeat")
    PB[i] = f"(JP, {repeat_line}, , )"
    i += 1


def save(token):
    global i
    semantic_stack.append(i)
    i += 1


def jpf(token):
    address = semantic_stack.pop()
    condition = semantic_stack.pop()
    PB[address] = f"(JPF, {condition}, {i}, )"


def jpf_save(token):
    global i
    address = semantic_stack.pop()
    condition = semantic_stack.pop()
    PB[address] = f"(JPF, {condition}, {i + 1}, )"
    semantic_stack.append(i)
    i += 1


def pop(token):
    semantic_stack.pop()


def jp(token):
    address = semantic_stack.pop()
    PB[address] = f"(JP, {i}, , )"


def assign(token):
    global i
    A = semantic_stack.pop()
    R = semantic_stack[-1]
    PB[i] = f"(ASSIGN, {A}, {R}, )"
    i += 1


def jump2(token):
    global i
    PB[i] = f"(JP, {i + 2}, , )"
    semantic_stack.append(i + 1)
    i += 2


def save_repeat_sym(token):
    symbol_table.append({"lexeme": "repeat", "address": semantic_stack[-1], "fun/var": "global"})
    lexeme_list.append("repeat")


def label(token):
    semantic_stack.append(i)


def jpf_repeat(token):
    global i
    condition = semantic_stack.pop()
    jp_label = semantic_stack.pop()
    PB[i] = f"(JPF, {condition}, {jp_label}, )"
    i += 1


def fill_break(token):
    PB[semantic_stack.pop()] = f"(JP, {i}, , )"


def remove_repeat(token):
    for i in range(len(symbol_table) - 1, -1, -1):
        if symbol_table[i]["lexeme"] == "repeat":
            del symbol_table[i]
            break


def return_int(token):
    global i
    t = semantic_stack.pop()
    PB[i] = f"(ASSIGN, {t}, 10, )"
    i += 1


def get_id_addr(token):
    global i
    lexeme = semantic_stack.pop()
    for j in range(len(symbol_table) - 1, -1, -1):
        if symbol_table[j]["lexeme"] == lexeme:
            if symbol_table[j]["fun/var"] == "fun":
                semantic_stack.append(symbol_table[j]["address"])
            elif symbol_table[j]["fun/var"] == "global" or symbol_table[j]["fun/var"] == "arr_glob":
                t = get_temp()
                addr = symbol_table[j]["address"]
                PB[i] = f"(ASSIGN, #{addr}, {t})"
                i += 1
                semantic_stack.append(f"@{t}")
            else:
                t = get_temp()
                addr = symbol_table[j]["address"]
                PB[i] = f"(ADD, 100, #{addr}, {t})"
                i += 1
                semantic_stack.append(f"@{t}")
            break


def get_arr_addr(token):
    global i
    index = semantic_stack.pop()
    temp = get_temp()
    PB[i] = f"(MULT, {index}, #{WORD_SIZE}, {temp})"
    t2 = get_temp()
    PB[i + 1] = f"(ASSIGN, {semantic_stack.pop()}, {t2}, )"
    PB[i + 2] = f"(ADD, {t2}, {temp}, {temp})"
    i = i + 3
    if arg_pass:
        t3 = get_temp()
        PB[i] = f"(ASSIGN, @{temp}, {t3}, )"
        i += 1
        semantic_stack.append(t3)
    else:
        semantic_stack.append(f"@{temp}")


def ex_relop(token):
    global i
    temp = get_temp()
    A2 = semantic_stack.pop()
    op = semantic_stack.pop()
    A1 = semantic_stack.pop()
    if op == '==':
        PB[i] = f"(EQ, {A1}, {A2}, {temp})"
    else:
        PB[i] = f"(LT, {A1}, {A2}, {temp})"
    semantic_stack.append(temp)
    i += 1


def p_operation(token):
    semantic_stack.append(token[1])


def ex_op(token):
    global i
    temp = get_temp()
    A2 = semantic_stack.pop()
    op = semantic_stack.pop()
    A1 = semantic_stack.pop()
    if op == '+':
        PB[i] = f"(ADD, {A1}, {A2}, {temp})"
    elif op == '-':
        PB[i] = f"(SUB, {A1}, {A2}, {temp})"
    elif op == '*':
        PB[i] = f"(MULT, {A1}, {A2}, {temp})"
    i += 1
    semantic_stack.append(temp)


def pass_arg(token):
    global local_memory_pointer, i
    t1 = get_temp()
    PB[i] = f"(ADD, 100, #{local_memory_pointer}, {t1})"
    local_memory_pointer += 4
    i += 1
    exp_addr = semantic_stack.pop()
    PB[i] = f"(ASSIGN, {exp_addr}, @{t1}, )"
    i += 1


def call_fun(token):
    global i, arg_pass, local_memory_pointer, last_local_memory_pointers
    arg_pass = False
    t1 = semantic_stack.pop()
    PB[i] = f"(ASSIGN, {t1}, 100, )"
    i += 1
    t2 = semantic_stack.pop()
    PB[i] = f"(ASSIGN, #{i + 2}, @{t2}, )"
    i += 1
    PB[i] = f"(JP, {semantic_stack.pop()}, , )"
    i += 1
    t = get_temp()
    PB[i] = f"(ASSIGN, 10, {t}, )"
    i += 1
    semantic_stack.append(t)
    # local_memory_pointer = last_local_memory_pointers.pop()
    local_memory_pointer = last_local_memory_pointers.pop()
    print(local_memory_pointer, "callfun")


def init_func(token):
    global i, local_memory_pointer, last_local_memory_pointers, arg_pass

    arg_pass = True
    t1 = get_temp()
    last_local_memory_pointers.append(local_memory_pointer)
    PB[i] = f"(ADD, 100, #{local_memory_pointer}, {t1})"
    local_memory_pointer += 4
    i += 1
    PB[i] = f"(ASSIGN, 100, @{t1}, )"
    i += 1
    t2 = get_temp()
    PB[i] = f"(ADD, 100, #{local_memory_pointer}, {t2})"
    local_memory_pointer += 4
    i += 1
    semantic_stack.append(t2)
    semantic_stack.append(t1)

    print(last_local_memory_pointers, "init pointers")


MY_INPUT_FILE = open("input.txt", 'r')


def get_next_token():
    global MY_INPUT_FILE
    res = get_next_token_from_file(MY_INPUT_FILE)
    if res is None:
        return None, "$"
    if res[0] == 'NUM' or res[0] == 'ID':
        return res, res[0]
    else:
        return res, res[1]


look_ahead = get_next_token()
curr_state = 0


def go(next_state, parent_node=None):
    global curr_state
    curr_state = next_state
    if parent_node is not None:
        Node("epsilon", parent_node)


def get(next_state, parent_node):
    global curr_state
    global look_ahead
    curr_state = next_state
    if look_ahead[0] is None:
        Node("$", parent_node)
    else:
        Node("({}, {})".format(look_ahead[0][0], look_ahead[0][1]), parent_node)
    look_ahead = get_next_token()


def call(string, return_state, parent_node):
    res = 0
    curr_node = Node(string, parent_node)
    global curr_state
    global look_ahead
    curr_state = lhs_to_start_state[string]
    while curr_state != lhs_to_final_state[string]:
        if (curr_state, look_ahead[1]) not in dictionary.keys():
            if look_ahead[1] == "$":
                if res != -1:
                    error_list.append("#{} : syntax error, Unexpected EOF\n".format(scanner.LINE_NUMBER))
                return -1
            else:
                list_of_expected_terminal = []
                for key, value in dictionary.items():
                    if key[0] == curr_state:
                        list_of_expected_terminal.append(key[1])
                if len(list_of_expected_terminal) == 1:
                    error_list.append(
                        "#{} : syntax error, missing {}\n".format(scanner.LINE_NUMBER, list_of_expected_terminal[0]))
                    go(dictionary[(curr_state, list_of_expected_terminal[0])][1])
                else:
                    error_list.append("#{} : syntax error, illegal {}\n".format(scanner.LINE_NUMBER, look_ahead[1]))
                    look_ahead = get_next_token()
                continue

        action, args = dictionary[(curr_state, look_ahead[1])]
        action_list = action_dict[(curr_state, look_ahead[1])]
        if action == "go":
            execute_actions(action_list)
            go(args, curr_node)
        elif action == "get":
            execute_actions(action_list)
            get(args, curr_node)
        elif action == "call":
            pre_actions = []
            post_actions = []
            for a in action_list:
                if a.startswith("#"):
                    pre_actions.append(a)
                else:
                    post_actions.append(a)
            execute_actions(pre_actions)
            res = call(args[0], args[1], curr_node)
            execute_actions(post_actions)
        else:
            error_list.append("#{} : syntax error, missing {}\n".format(scanner.LINE_NUMBER, args[0]))
            go(args[1])

    if return_state == -1:
        return "accept"
    else:
        go(return_state)
        return


i = 9


def execute_action(action_name):
    # print(symbol_table)
    print(look_ahead)
    print(action_name)
    print(semantic_stack)
    print("hello")

    globals()[action_name[1:]](look_ahead)


def execute_actions(action_names):
    for action in action_names:
        execute_action(action)


error_list = []

udo = Node("bikhod")
call("Program", -1, udo)
error_file = open("syntax_errors.txt", 'w')
if len(error_list) == 0:
    error_file.write("There is no syntax error.")
for error in error_list:
    error_file.write(error)
with open("parse_tree.txt", 'w', encoding="utf-8") as tree_file:
    for pre, fill, node in RenderTree(udo.children[0]):
        line_str = "%s%s" % (pre, node.name)
        tree_file.write(line_str + '\n')

output_code = open("output.txt", "w")
pb_line_number = 0
t = PB[0]
while t != "":
    output_code.write(str(pb_line_number) + '\t' + t + '\n')
    pb_line_number += 1
    t = PB[pb_line_number]

output_code.close()
error_file.close()
tree_file.close()
