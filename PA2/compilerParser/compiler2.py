# Alireza Dehghanpour 98101555
# Rouzbeh pirayadi 98101306

from scanner import *
import scanner
from anytree import Node, RenderTree

action_dict = {(0, 'epsilon'): [], (0, 'int'): [], (0, 'void'): [], (0, '$'): [], (0, 'ID'): [], (0, ';'): [],
               (0, 'NUM'): [], (0, '('): [], (0, '{'): [], (0, '}'): [], (0, 'break'): [], (0, 'if'): [],
               (0, 'repeat'): [], (0, 'return'): [], (1, '$'): [], (3, 'int'): [], (3, 'void'): [], (4, 'epsilon'): [],
               (4, 'int'): [], (4, 'void'): [], (4, '$'): [], (4, 'ID'): [], (4, ';'): [], (4, 'NUM'): [], (4, '('): [],
               (4, '{'): [], (4, '}'): [], (4, 'break'): [], (4, 'if'): [], (4, 'repeat'): [], (4, 'return'): [],
               (3, '$'): [], (3, 'ID'): [], (3, ';'): [], (3, 'NUM'): [], (3, '('): [], (3, '{'): [], (3, '}'): [],
               (3, 'break'): [], (3, 'if'): [], (3, 'repeat'): [], (3, 'return'): [], (6, 'int'): [], (6, 'void'): [],
               (7, ';'): [], (7, '['): [], (7, '('): [], (9, 'int'): ['#ptype'], (9, 'void'): ['#ptype'],
               (10, 'ID'): ['#pid'], (12, '('): ['#declare_fun', '%return_void', '%jump_main', '%dec_scope'],
               (12, ';'): [], (12, '['): [], (14, ';'): ['#declare_var'], (14, '['): [], (16, 'NUM'): ['#psize'],
               (17, ']'): ['#declare_arr'], (18, ';'): [], (19, '('): ['#inc_scope'], (20, 'int'): [], (20, 'void'): [],
               (21, ')'): [], (22, '{'): [], (24, 'int'): [], (24, 'void'): [], (26, 'int'): ['#ptype'],
               (27, 'ID'): ['#pid'], (28, 'epsilon'): [], (28, '['): [], (28, ')'): [], (28, ','): [],
               (29, 'epsilon'): [], (29, ','): [], (29, ')'): [], (26, 'void'): [], (31, ','): [], (32, 'int'): [],
               (32, 'void'): [], (33, 'epsilon'): [], (33, ','): [], (33, ')'): [], (31, ')'): [], (35, 'int'): [],
               (35, 'void'): [], (36, 'epsilon'): [], (36, '['): [], (36, ')'): [], (36, ','): [], (38, '['): [],
               (39, ']'): ['#declare_par_arr'], (38, ')'): ['#declare_par_var'], (38, ','): ['#declare_par_var'],
               (41, '{'): [], (42, 'epsilon'): [], (42, 'int'): [], (42, 'void'): [], (42, '$'): [], (42, 'ID'): [],
               (42, ';'): [], (42, 'NUM'): [], (42, '('): [], (42, '{'): [], (42, '}'): [], (42, 'break'): [],
               (42, 'if'): [], (42, 'repeat'): [], (42, 'return'): [], (43, 'return'): [], (43, 'NUM'): [],
               (43, 'ID'): [], (43, 'epsilon'): [], (43, '('): [], (43, 'break'): [], (43, 'repeat'): [],
               (43, 'if'): [], (43, '{'): [], (43, ';'): [], (43, '}'): [], (44, '}'): [], (46, 'return'): [],
               (46, 'NUM'): [], (46, 'ID'): [], (46, '('): [], (46, 'break'): [], (46, 'repeat'): [], (46, 'if'): [],
               (46, '{'): [], (46, ';'): [], (47, 'return'): [], (47, 'NUM'): [], (47, 'ID'): [], (47, 'epsilon'): [],
               (47, '('): [], (47, 'break'): [], (47, 'repeat'): [], (47, 'if'): [], (47, '{'): [], (47, ';'): [],
               (47, '}'): [], (46, '}'): [], (49, 'NUM'): [], (49, 'ID'): [], (49, '('): [], (49, 'break'): [],
               (49, ';'): [], (49, '{'): [], (49, 'if'): [], (49, 'repeat'): [], (49, 'return'): [], (54, '('): [],
               (54, 'NUM'): [], (54, 'ID'): [], (55, ';'): ['#pop_expression'], (54, 'break'): ['#breakj'],
               (57, ';'): [], (54, ';'): [], (59, 'if'): [], (60, '('): [], (61, '('): [], (61, 'NUM'): [],
               (61, 'ID'): [], (62, ')'): ['#save'], (63, 'return'): [], (63, 'NUM'): [], (63, 'ID'): [], (63, '('): [],
               (63, 'break'): [], (63, 'repeat'): [], (63, 'if'): [], (63, '{'): [], (63, ';'): [], (64, 'endif'): [],
               (64, 'else'): [], (66, 'endif'): ['#jpf'], (66, 'else'): [], (68, 'return'): ['#jpf_save'],
               (68, 'NUM'): ['#jpf_save'], (68, 'ID'): ['#jpf_save'], (68, '('): ['#jpf_save'],
               (68, 'break'): ['#jpf_save'], (68, 'repeat'): ['#jpf_save'], (68, 'if'): ['#jpf_save'],
               (68, '{'): ['#jpf_save'], (68, ';'): ['#jpf_save'], (69, 'endif'): ['#jp'],
               (70, 'repeat'): ['#jump2', '#save_repeat_sym'], (71, 'return'): ['#label'], (71, 'NUM'): ['#label'],
               (71, 'ID'): ['#label'], (71, '('): ['#label'], (71, 'break'): ['#label'], (71, 'repeat'): ['#label'],
               (71, 'if'): ['#label'], (71, '{'): ['#label'], (71, ';'): ['#label'], (72, 'until'): [], (73, '('): [],
               (74, '('): [], (74, 'NUM'): [], (74, 'ID'): [],
               (75, ')'): ['#jpf_repeat', '#fill_break', '#remove_repeat'], (77, 'return'): [], (78, ';'): [],
               (78, 'NUM'): [], (78, '('): [], (78, 'ID'): [], (80, ';'): ['#return_void'], (80, '('): [],
               (80, 'NUM'): [], (80, 'ID'): [], (82, ';'): ['#return_int', '#return_void'], (83, '('): [],
               (83, 'NUM'): [], (83, 'ID'): ['#pid'], (85, '<'): [], (85, '='): [], (85, 'epsilon'): [], (85, '=='): [],
               (85, '('): [], (85, '['): [], (85, '+'): [], (85, '*'): [], (85, '-'): [], (85, ';'): [], (85, ']'): [],
               (85, ')'): [], (85, ','): [], (86, '='): [], (87, '('): ['%get_id_addr_rec', '%assign'],
               (87, 'NUM'): ['%get_id_addr_rec', '%assign'], (87, 'ID'): ['%get_id_addr_rec', '%assign'], (86, '['): [],
               (89, '('): ['#get_id_addr'], (89, 'NUM'): ['#get_id_addr'], (89, 'ID'): ['#get_id_addr'],
               (90, ']'): ['#get_arr_addr'], (91, '<'): [], (91, '='): [], (91, 'epsilon'): [], (91, '=='): [],
               (91, '+'): [], (91, '*'): [], (91, '-'): [], (91, ';'): [], (91, ']'): [], (91, ')'): [], (91, ','): [],
               (86, '<'): ['#get_id_addr'], (86, 'epsilon'): ['#get_id_addr'], (86, '=='): ['#get_id_addr'],
               (86, '('): ['#get_id_addr'], (86, '+'): ['#get_id_addr'], (86, '*'): ['#get_id_addr'],
               (86, '-'): ['#get_id_addr'], (86, ';'): ['#get_id_addr'], (86, ']'): ['#get_id_addr'],
               (86, ')'): ['#get_id_addr'], (86, ','): ['#get_id_addr'], (93, '='): [], (94, '('): ['%assign'],
               (94, 'NUM'): ['%assign'], (94, 'ID'): ['%assign'], (93, 'epsilon'): [], (93, '*'): [], (93, ';'): [],
               (93, ']'): [], (93, ')'): [], (93, ','): [], (93, '<'): [], (93, '=='): [], (93, '+'): [], (93, '-'): [],
               (96, 'epsilon'): [], (96, '+'): [], (96, '-'): [], (96, ';'): [], (96, ']'): [], (96, ')'): [],
               (96, ','): [], (96, '<'): [], (96, '=='): [], (97, '<'): [], (97, 'epsilon'): [], (97, '=='): [],
               (97, ';'): [], (97, ']'): [], (97, ')'): [], (97, ','): [], (98, '('): [], (98, 'NUM'): [],
               (99, '<'): [], (99, 'epsilon'): [], (99, '=='): [], (99, ';'): [], (99, ']'): [], (99, ')'): [],
               (99, ','): [], (101, 'epsilon'): [], (101, '('): [], (101, '+'): [], (101, '*'): [], (101, '-'): [],
               (101, ';'): [], (101, ']'): [], (101, ')'): [], (101, ','): [], (101, '<'): [], (101, '=='): [],
               (102, '<'): [], (102, 'epsilon'): [], (102, '=='): [], (102, ';'): [], (102, ']'): [], (102, ')'): [],
               (102, ','): [], (104, '<'): [], (104, '=='): [], (105, '('): ['%ex_relop'], (105, 'NUM'): ['%ex_relop'],
               (105, 'ID'): ['%ex_relop'], (104, ';'): [], (104, ']'): [], (104, ')'): [], (104, ','): [],
               (107, '<'): ['#p_operation'], (107, '=='): ['#p_operation'], (109, '('): [], (109, 'NUM'): [],
               (109, 'ID'): [], (110, 'epsilon'): [], (110, '+'): [], (110, '-'): [], (110, ';'): [], (110, ']'): [],
               (110, ')'): [], (110, ','): [], (110, '<'): [], (110, '=='): [], (112, 'epsilon'): [], (112, '('): [],
               (112, '*'): [], (112, ';'): [], (112, ']'): [], (112, ')'): [], (112, ','): [], (112, '<'): [],
               (112, '=='): [], (112, '+'): [], (112, '-'): [], (113, 'epsilon'): [], (113, '+'): [], (113, '-'): [],
               (113, ';'): [], (113, ']'): [], (113, ')'): [], (113, ','): [], (113, '<'): [], (113, '=='): [],
               (115, '('): [], (115, 'NUM'): [], (116, 'epsilon'): [], (116, '+'): [], (116, '-'): [], (116, ';'): [],
               (116, ']'): [], (116, ')'): [], (116, ','): [], (116, '<'): [], (116, '=='): [], (118, '+'): [],
               (118, '-'): [], (119, '('): [], (119, 'NUM'): [], (119, 'ID'): [], (120, 'epsilon'): ['#ex_op'],
               (120, '+'): ['#ex_op'], (120, '-'): ['#ex_op'], (120, ';'): ['#ex_op'], (120, ']'): ['#ex_op'],
               (120, ')'): ['#ex_op'], (120, ','): ['#ex_op'], (120, '<'): ['#ex_op'], (120, '=='): ['#ex_op'],
               (118, ';'): [], (118, ']'): [], (118, ')'): [], (118, ','): [], (118, '<'): [], (118, '=='): [],
               (122, '+'): ['#p_operation'], (122, '-'): ['#p_operation'], (124, '('): [], (124, 'NUM'): [],
               (124, 'ID'): [], (125, 'epsilon'): [], (125, '*'): [], (125, ';'): [], (125, ']'): [], (125, ')'): [],
               (125, ','): [], (125, '<'): [], (125, '=='): [], (125, '+'): [], (125, '-'): [], (127, 'epsilon'): [],
               (127, '('): [], (127, ';'): [], (127, ']'): [], (127, ')'): [], (127, ','): [], (127, '<'): [],
               (127, '=='): [], (127, '+'): [], (127, '-'): [], (127, '*'): [], (128, 'epsilon'): [], (128, '*'): [],
               (128, ';'): [], (128, ']'): [], (128, ')'): [], (128, ','): [], (128, '<'): [], (128, '=='): [],
               (128, '+'): [], (128, '-'): [], (130, '('): [], (130, 'NUM'): [], (131, 'epsilon'): [], (131, '*'): [],
               (131, ';'): [], (131, ']'): [], (131, ')'): [], (131, ','): [], (131, '<'): [], (131, '=='): [],
               (131, '+'): [], (131, '-'): [], (133, '*'): ['#p_operation'], (134, '('): [], (134, 'NUM'): [],
               (134, 'ID'): [], (135, 'epsilon'): ['#ex_op'], (135, '*'): ['#ex_op'], (135, ';'): ['#ex_op'],
               (135, ']'): ['#ex_op'], (135, ')'): ['#ex_op'], (135, ','): ['#ex_op'], (135, '<'): ['#ex_op'],
               (135, '=='): ['#ex_op'], (135, '+'): ['#ex_op'], (135, '-'): ['#ex_op'], (133, ';'): [], (133, ']'): [],
               (133, ')'): [], (133, ','): [], (133, '<'): [], (133, '=='): [], (133, '+'): [], (133, '-'): [],
               (137, '('): [], (138, '('): [], (138, 'NUM'): [], (138, 'ID'): [], (139, ')'): [], (137, 'ID'): ['#pid'],
               (141, 'epsilon'): [], (141, '['): [], (141, '('): [], (141, ';'): [], (141, ']'): [], (141, ')'): [],
               (141, ','): [], (141, '<'): [], (141, '=='): [], (141, '+'): [], (141, '-'): [], (141, '*'): [],
               (137, 'NUM'): ['#pnum'], (143, '('): ['#get_id_addr', '#init_func'], (144, 'epsilon'): [],
               (144, '('): [], (144, 'NUM'): [], (144, 'ID'): [], (144, ')'): [], (145, ')'): ['#call_fun'],
               (143, 'epsilon'): ['#get_id_addr'], (143, '['): ['#get_id_addr'], (143, ';'): ['#get_id_addr'],
               (143, ']'): ['#get_id_addr'], (143, ')'): ['#get_id_addr'], (143, ','): ['#get_id_addr'],
               (143, '<'): ['#get_id_addr'], (143, '=='): ['#get_id_addr'], (143, '+'): ['#get_id_addr'],
               (143, '-'): ['#get_id_addr'], (143, '*'): ['#get_id_addr'], (147, '['): [], (148, '('): [],
               (148, 'NUM'): [], (148, 'ID'): [], (149, ']'): ['#get_arr_addr'], (147, ';'): [], (147, ']'): [],
               (147, ')'): [], (147, ','): [], (147, '<'): [], (147, '=='): [], (147, '+'): [], (147, '-'): [],
               (147, '*'): [], (151, '('): ['#init_func'], (152, 'epsilon'): [], (152, '('): [], (152, 'NUM'): [],
               (152, 'ID'): [], (152, ')'): [], (153, ')'): ['#call_fun'], (151, ';'): [], (151, ']'): [],
               (151, ')'): [], (151, ','): [], (151, '<'): [], (151, '=='): [], (151, '+'): [], (151, '-'): [],
               (151, '*'): [], (155, '('): [], (156, '('): [], (156, 'NUM'): [], (156, 'ID'): [], (157, ')'): [],
               (155, 'NUM'): ['#pnum'], (159, '('): [], (159, 'NUM'): [], (159, 'ID'): [], (159, ')'): [],
               (161, '('): [], (161, 'NUM'): [], (161, 'ID'): [], (162, 'epsilon'): ['#pass_arg'],
               (162, ','): ['#pass_arg'], (162, ')'): ['#pass_arg'], (164, ','): [], (165, '('): [], (165, 'NUM'): [],
               (165, 'ID'): [], (166, 'epsilon'): ['#pass_arg'], (166, ','): ['#pass_arg'], (166, ')'): ['#pass_arg'],
               (164, ')'): []}

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
arr_pointer = 30000
globals_pointer = 20000


# var, arr, fun, param_var, param_arr


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
    if str(A).startswith("!"):
        t = get_temp()
        PB[i] = f"(ADD, 100, #{A[1:]}, {t})"
        i += 1
        A = f"@{t}"
    if str(R).startswith("!"):
        t = get_temp()
        PB[i] = f"(ADD, 100, #{R[1:]}, {t})"
        i += 1
        R = f"@{t}"
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
    if str(A1).startswith("!"):
        t = get_temp()
        PB[i] = f"(ADD, 100, #{A1[1:]}, {t})"
        i += 1
        A1 = f"@{t}"
    if str(A2).startswith("!"):
        t = get_temp()
        PB[i] = f"(ADD, 100, #{A2[1:]}, {t})"
        i += 1
        A2 = f"@{t}"
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
    if str(A1).startswith("!"):
        t = get_temp()
        PB[i] = f"(ADD, 100, #{A1[1:]}, {t})"
        i += 1
        A1 = f"@{t}"
    if str(A2).startswith("!"):
        t = get_temp()
        PB[i] = f"(ADD, 100, #{A2[1:]}, {t})"
        i += 1
        A2 = f"@{t}"
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

    if str(exp_addr).startswith("!"):
        t = get_temp()
        PB[i] = f"(ADD, 100, #{exp_addr[1:]}, {t})"
        i += 1
        exp_addr = f"@{t}"

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
    local_memory_pointer = last_local_memory_pointers.pop()
    PB[i] = f"(ADD, 100, #{local_memory_pointer}, {t})"
    i += 1
    PB[i] = f"(ASSIGN, 10, @{t}, )"
    i += 1
    semantic_stack.append(f"!{local_memory_pointer}")
    local_memory_pointer += 4
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


terminals = ['$', 'ID', ';', '[', 'NUM', ']', '(', ')', 'int', 'void', ',', '{', '}', 'break', 'if', 'endif', 'else',
             'repeat', 'until', 'return', '=', '<', '==', '+', '-', '*']


def is_terminal(element):
    return element in terminals


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

f = open("grammar.txt")
dictionary = {}
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
        for i in range(len(elements)):

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
                state += 1
            elif is_terminal(elements[i]):
                dictionary[(correct_state, elements[i])] = ("get", next_state)
                state += 1
            else:
                for item in list(set(first[elements[i]]) - set(list("epsilon"))):
                    dictionary[(correct_state, item)] = ("call", (elements[i], next_state))
                if "epsilon" in first[elements[i]]:
                    for item in follow[elements[i]]:
                        dictionary[(correct_state, item)] = ("call", (elements[i], next_state))
                else:
                    for item in follow[elements[i]]:
                        if (correct_state, item) not in dictionary.keys():
                            dictionary[(correct_state, item)] = ("missing", (elements[i], next_state))
                state += 1

            if i == len(elements) - 1 and final_first_time:
                last_state = state
                lhs_to_final_state[LHS] = last_state
        final_first_time = False
    if len(all_productions) == 1:
        state += 1

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
lllll = 0
t = PB[0]
while t != "":
    output_code.write(str(lllll) + '\t' + t + '\n')
    lllll += 1
    t = PB[lllll]

output_code.close()
error_file.close()
tree_file.close()
