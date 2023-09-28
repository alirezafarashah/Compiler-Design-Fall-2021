SYMBOLS = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-", "*", "=", "==", "<"]
LOWERCASE_LETTERS = [chr(x) for x in range(ord('a'), ord('z') + 1)]
UPPERCASE_LETTERS = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
LETTERS = LOWERCASE_LETTERS + UPPERCASE_LETTERS
DIGITS = [str(x) for x in range(10)]
WHITESPACES = [chr(32), chr(10), chr(13), chr(9), chr(11), chr(12)]
VALID_CHARS = LETTERS + DIGITS + WHITESPACES + SYMBOLS + ["/", "*"]
SYMBOL_TABLE = dict(
    {"if": 1, "else": 2, "void": 3, "int": 4, "repeat": 5, "break": 6, "until": 7, "return": 8, "endif": 9})
ERROR_DICT = dict()


# TODO bug in line number for lexical errors like testcase7
def is_digit(c):
    return c in DIGITS


def is_letter(c):
    return c in LETTERS


def is_symbol_except_equal_and_star(c):
    return c in SYMBOLS and c != "=" and c != '*'


def is_other(c, state):
    if state == 1:
        return (not c in LETTERS) and c in VALID_CHARS + ['']
    elif state == 2:
        return c in VALID_CHARS + ['']
    elif state == 4:
        return c in VALID_CHARS + ['']
    elif state == 7:
        return c in VALID_CHARS
    elif state == 11:
        return c != "*"
    elif state == 12:
        return c != "*"
    elif state == 14:
        return c != "\n" and c != ''
    elif state == 18:
        return c in VALID_CHARS + [''] and c != '/'
    return False


def is_whitespace(c):
    return c in WHITESPACES


def check_id_in_symbol_table(token):
    if not token in SYMBOL_TABLE.keys():
        SYMBOL_TABLE[token] = len(SYMBOL_TABLE) + 1
        return "ID"
    if 1 <= SYMBOL_TABLE[token] <= 8:
        return "KEYWORD"
    return "ID"


def add_to_error(token, string_type, comment_line=0):
    line = LINE_NUMBER
    if string_type == "Unclosed comment":
        line = comment_line
    if line not in ERROR_DICT.keys():
        ERROR_DICT[line] = [(token, string_type)]
    else:
        ERROR_DICT[line].append((token, string_type))


def get_next_token(file):
    global LINE_NUMBER
    token = ''
    state = 0
    c = '1'
    comment_line = 0
    while c != '':
        index = file.tell()
        c = file.read(1)
        if c == '\n':
            LINE_NUMBER += 1
        token += c
        if state == 0:
            if is_digit(c):
                state = 1
            elif is_letter(c):
                state = 2
            elif is_symbol_except_equal_and_star(c):
                state = 3
            elif c == "=":
                state = 4
            elif c == "/":
                state = 7
            elif is_whitespace(c):
                state = 8
            elif c == "*":
                state = 18
            elif c != '':
                state = 21
        elif state == 1:
            if is_digit(c):
                state = 1
            elif is_letter(c):
                state = 16
            elif is_other(c, state):
                state = 9
            else:
                state = 21
        elif state == 2:
            if is_letter(c) or is_digit(c):
                state = 2
            elif is_other(c, state):
                state = 10
            else:
                state = 21

        elif state == 4:
            if c == '=':
                state = 5
            elif is_other(c, state):
                state = 6
            else:
                state = 21

        elif state == 7:
            if c == '*':
                state = 11
                comment_line = LINE_NUMBER
            elif c == "/":
                state = 14
            elif is_other(c, state):
                state = 22
            else:
                state = 21

        elif state == 11:
            if c == "*":
                state = 12
            elif c == '':
                state = 17
            elif is_other(c, state):
                state = 11

        elif state == 12:
            if c == "*":
                state = 12
            if c == '':
                state = 17
            elif c == "/":
                state = 13
            elif is_other(c, state):
                state = 11

        elif state == 14:
            if c == "\n" or c == '':
                state = 15
            elif is_other(c, state):
                state = 14

        elif state == 18:
            if c == "/":
                state = 19
            elif is_other(c, state):
                state = 20
            else:
                state = 21

        # final states
        if c == '\n' and (state in [6, 9, 10, 20, 22]):
            LINE_NUMBER -= 1

        if state == 3:
            return 'SYMBOL', token

        if state == 5:
            return "SYMBOL", token
        if state == 6:
            if c == '':
                return "SYMBOL", token
            token = token[:len(token) - 1]
            file.seek(index)
            return "SYMBOL", token

        if state == 8:
            state = 0
            token = ''

        if state == 9:
            if c == '':
                return "NUM", token
            token = token[:len(token) - 1]
            file.seek(index)
            return "NUM", token

        if state == 10:
            if c == '':
                return check_id_in_symbol_table(token), token
            token = token[:len(token) - 1]
            file.seek(index)
            return check_id_in_symbol_table(token), token

        if state == 13:
            state = 0
            token = ''

        if state == 15:
            state = 0
            token = ''

        if state == 16:
            add_to_error(token, "Invalid number")
            # errors.write(str(LINE_NUMBER) + "." + "\t" + "(" + token + ", " + "Invalid number" + ")\n")
            # errors.flush()
            token = ''
            state = 0

        if state == 17:
            temp = token[0:min(7, len(token))]
            # errors.write(
            #   str(comment_line) + "." + "\t" + "(" + token[0:min(7, len(token))])
            if len(token) > 7:
                temp += "..."
            add_to_error(temp, "Unclosed comment", comment_line)
            #   errors.write("...")
            # errors.write(", " + "Unclosed comment" + ")\n")
            # errors.flush()
            token = ''
            state = 0
        if state == 19:
            add_to_error(token, "Unmatched comment")
            # errors.write(str(LINE_NUMBER) + "." + "\t" + "(" + token + ", " + "Unmatched comment" + ")\n")
            # errors.flush()
            token = ''
            state = 0

        if state == 20:
            if c == '':
                return "SYMBOL", token
            token = token[:len(token) - 1]
            file.seek(index)
            return "SYMBOL", token

        if state == 21:
            add_to_error(token, "Invalid input")
            # errors.write(str(LINE_NUMBER) + "." + "\t" + "(" + token + ", " + "Invalid input" + ")\n")
            # errors.flush()
            token = ''
            state = 0
        if state == 22:
            token = token[:len(token) - 1]
            file.seek(index)
            add_to_error(token, "Invalid input")
            # errors.write(str(LINE_NUMBER) + "." + "\t" + "(" + token + ", " + "Invalid input" + ")\n")
            # errors.flush()
            token = ''
            state = 0

    return None


file = open("input.txt", 'r', encoding='utf-8')
error_file = open("lexical_errors.txt", 'w')
tokens_file = open("tokens.txt", 'w')
symbol_table = open("symbol_table.txt", 'w')
LINE_NUMBER = 1
last_line_number = 0
while True:
    res = get_next_token(file)
    if not res is None:
        if last_line_number == 0:
            tokens_file.write(str(LINE_NUMBER) + ".\t")
        elif last_line_number != LINE_NUMBER:
            tokens_file.write("\n" + str(LINE_NUMBER) + ".\t")
        elif last_line_number == LINE_NUMBER:
            tokens_file.write(" ")
        tokens_file.write("(" + res[0] + ", " + res[1] + ")")
        last_line_number = LINE_NUMBER
        tokens_file.flush()
    else:
        break
for key, value in SYMBOL_TABLE.items():
    symbol_table.write(str(value) + ".\t" + key + "\n")

if len(ERROR_DICT) != 0:
    for key, value in ERROR_DICT.items():
        error_file.write(str(key) + ".\t")
        for v in value:
            error_file.write("(" + v[0] + ", " + v[1] + ") ")
        error_file.write("\n")
else:
    error_file.write("There is no lexical error.")
symbol_table.close()
file.close()
tokens_file.close()
error_file.close()
