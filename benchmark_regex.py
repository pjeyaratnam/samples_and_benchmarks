from pygments.lexer import RegexLexer
import os
import random
import re
from pygments.token import Token
import time


def walk(path, exclude_dirs=None, exclude_files=None):
    if exclude_dirs is None:
        exclude_dirs = set()
    if exclude_files is None:
        exclude_files = set()

    for path, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if file not in exclude_files:
                yield os.path.join(path, file)


def gen_random_content(num_lines=5000):
    line = ''
    for _ in range(num_lines):
        line += ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(75))
        line += '\n'
    return line


def gen_random_regexp(num_expr):
    content = []
    for _ in range(num_expr):
        length = random.randint(3, 10)
        regex = r'\b' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length)) + r'\b'
        content.append(regex)
    return content


def build_pattern(expr_list):
    result = []
    for expr in expr_list:
        result.append((expr, Token.NAME))
    return result


def make_regex_lexer(name, patterns):
    tokens = {'root': patterns}
    return type(name, (RegexLexer,), {'tokens': tokens})


def main():
    # let's assume worst case 5000 line code file
    content = gen_random_content(5000)

    # best case
    pattern_best = build_pattern(gen_random_regexp(20))
    # avg case
    pattern_avg = build_pattern(gen_random_regexp(100))
    # worst case
    pattern_worst = build_pattern(gen_random_regexp(5000))

    bestLexer = make_regex_lexer('BestLexer', pattern_best)
    avgLexer = make_regex_lexer('AvgLexer', pattern_avg)
    worstLexer = make_regex_lexer('WorstLexer', pattern_worst)

    st_best = time.time()
    result1 = bestLexer().get_tokens_unprocessed(content)
    end_best = time.time()

    st_avg = time.time()
    result2 = avgLexer().get_tokens_unprocessed(content)
    end_avg = time.time()

    st_worst = time.time()
    result3 = worstLexer().get_tokens_unprocessed(content)
    end_worst = time.time()

    print(end_best - st_best)
    print(end_avg - st_avg)
    print(end_worst - st_worst)


if __name__ == '__main__':
    main()
