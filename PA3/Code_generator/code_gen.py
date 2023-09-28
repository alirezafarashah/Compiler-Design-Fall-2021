semantic_stack = []
PB = [""] * 1000
i = 0
WORD_SIZE = 4
scope_stack = [0]
symbol_table = []
lexeme_list = []

runtime_memory = [0] * 40000
runtime_memory_pointer = 500

temp_pointer = 3000
arr_pointer = 30000
globals_pointer = 20000


# var, arr, fun, param_var, param_arr


def find_addr(lexeme):
    for i in range(len(symbol_table) - 1, -1, -1):
        if symbol_table[i]["lexeme"] == lexeme:
            if symbol_table[i]["fun/var"] == "global" or symbol_table[i]["fun/var"] == "fun":
                return symbol_table[i]["address"]
            else:
                return symbol_table[i]["address"] + runtime_memory[100]
    return -1


def get_temp():
    global temp_pointer
    temp_pointer += 4
    return temp_pointer - 4


def ptype(token):
    semantic_stack.append(token[1])


def pid(token):
    semantic_stack.append(token[1])


def declare_fun(token):
    global i
    name = semantic_stack.pop()
    fun_type = semantic_stack.pop()
    symbol_table.append(
        {"lexeme": name, "type": fun_type, "fun/var": "fun", "address": i + 1, "scope": len(scope_stack)})
    lexeme_list.append(name)
    semantic_stack.append(i)
    i = i + 1


def jump_main(token):
    line_num = semantic_stack.pop()
    PB[line_num] = f"(JP, {i}, , )"


def declare_var(token):
    global i, globals_pointer, runtime_memory_pointer
    name = semantic_stack.pop()
    var_type = semantic_stack.pop()
    if scope_stack[-1] == 0:
        g = "global"
        addr = globals_pointer
        globals_pointer += 4
    else:
        g = "var"
        addr = runtime_memory_pointer - runtime_memory[100]
        runtime_memory_pointer += 4
    symbol_table.append({"lexeme": name, "type": var_type, "fun/var": g, "address": addr, "scope": len(scope_stack)})
    lexeme_list.append(name)


def psize(token):
    semantic_stack.append(token[1])


def pnum(token):
    global i
    t = get_temp()
    PB[i] = f"(ASSIGN, #{token[1]}, t, )"
    i += 1
    semantic_stack.append(t)


def declare_arr(token):
    global i, globals_pointer, runtime_memory_pointer, arr_pointer
    arr_size = semantic_stack.pop()
    name = semantic_stack.pop()
    var_type = semantic_stack.pop()

    if scope_stack[-1] == 0:
        addr = globals_pointer
        globals_pointer += 4
    else:
        addr = runtime_memory_pointer - runtime_memory[100]
        runtime_memory_pointer += 4
    arr_pointer += 4 * arr_size
    symbol_table.append(
        {"lexeme": name, "type": var_type, "fun/var": "arr", "address": addr, "scope": len(scope_stack)})
    lexeme_list.append(name)


def inc_scope(token):
    scope_stack.append(len(symbol_table))


def declare_par(token, g):
    global i, globals_pointer, runtime_memory_pointer
    name = semantic_stack.pop()
    var_type = semantic_stack.pop()
    addr = runtime_memory_pointer - runtime_memory[100]
    runtime_memory_pointer += 4
    symbol_table.append({"lexeme": name, "type": var_type, "fun/var": g, "address": addr, "scope": len(scope_stack)})
    lexeme_list.append(name)


def declare_par_var(token):
    declare_par(token, "param_var")


def declare_par_arr(token):
    declare_par(token, "param_arr")


def return_void(token):
    global i
    temp1_addr = get_temp()
    PB[i] = f"(ADD, 100, #4, {temp1_addr}"
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


def save():
    global i
    semantic_stack.append(i)
    i += 1


def jpf():
    address = semantic_stack.pop()
    condition = semantic_stack.pop()
    PB[address] = f"(JPF, {condition}, {i}, )"


def jpf_save():
    global i
    address = semantic_stack.pop()
    condition = semantic_stack.pop()
    PB[address] = f"(JPF, {condition}, {i + 1}, )"
    semantic_stack.append(i)
    i += 1


def jp():
    address = semantic_stack.pop()
    PB[address] = f"(JP, {i}, , )"


def assign():
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
    PB[i] = f"(JPF, {condition}, {label}, )"
    i += 1


# def jpt():
#     condition = semantic_stack.pop()
#     label = semantic_stack.pop()
#     break_address = semantic_stack.pop()
#
#     PB[i] = f"(JPF, {condition}, {i + 2}, )"
#     PB[i + 1] = f"(JP, {condition}, {label}, )"
#     PB[break_address] = f"(JP, {i + 2}, , )"
#     i += 2

def fill_break(token):
    rep_addr = find_addr("repeat")
    PB[rep_addr] = f"(JP, {i}, , )"


def remove_repeat(token):
    for i in range(len(symbol_table), -1, -1):
        if symbol_table[i]["lexeme"] == "repeat":
            del symbol_table[i]
            break


def return_int(token):
    t = semantic_stack.pop()
    PB[i] = f"(ASSIGN, {t}, 10, )"


def get_id_addr(token):
    addr = find_addr(semantic_stack.pop())
    semantic_stack.append(addr)


def get_arr_addr(token):
    global i
    index = semantic_stack.pop()
    temp = get_temp()
    PB[i] = f"(MULT, {index}, {WORD_SIZE}, {temp})"
    PB[i + 1] = f"(ADD, @{semantic_stack.pop()}, {temp}, {temp})"
    i = i + 2
    semantic_stack.append(temp)


# def parr():
#     index = semantic_stack.pop()
#     temp = get_temp()
#     PB[i] = f"(MULT, {index}, {WORD_SIZE}, {temp})"
#     PB[i + 1] = f"(ADD, {semantic_stack.pop()}, {temp}, {temp})"
#     semantic_stack.append(f"@{temp}")


def ex_relop(token):
    temp = get_temp()
    A2 = semantic_stack.pop()
    op = semantic_stack.pop()
    A1 = semantic_stack.pop()
    if op == '==':
        PB[i] = f"(EQ, {A1}, {A2}, {temp})"
    else:
        PB[i] = f"(LT, {A1}, {A2}, {temp})"


def p_operation(token):
    semantic_stack.append(token[1])


def ex_op(token):
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


def pass_arg(token):
    global runtime_memory_pointer, i
    t1 = get_temp()
    PB[i] = f"(ADD, 100, #{runtime_memory_pointer - runtime_memory[100]}, {t1})"
    runtime_memory_pointer += 4
    i += 1
    exp_addr = semantic_stack.pop()
    PB[i] = f"(ASSIGN, {exp_addr}, @{t1}, )"
    i += 1


def call_fun(token):
    global i
    t2 = semantic_stack.pop()
    PB[i] = f"(ASSIGN, {i + 2}, @{t2}, )"
    i += 1
    PB[i] = f"(JP, {semantic_stack.pop()}, , )"


def init_func(token):
    global i, runtime_memory_pointer
    t1 = get_temp()
    PB[i] = f"(ADD, 100, #{runtime_memory_pointer - runtime_memory[100]}, {t1})"
    runtime_memory_pointer += 4
    i += 1
    PB[i] = f"(ASSIGN, 100, @{t1}, )"
    i += 1
    t2 = get_temp()
    PB[i] = f"(ADD, 100, #{runtime_memory_pointer - runtime_memory[100]}, {t2})"
    runtime_memory_pointer += 4
    i += 1
    semantic_stack.append(t2)
