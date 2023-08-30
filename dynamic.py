from pygments.lexer import RegexLexer
from pygments.token import Token


def create_dynamic_lexer(patterns):
    dynamic_tokens = {'root': patterns}
    return type('DynamicLexer', (RegexLexer,), {'tokens': dynamic_tokens})


def main():
    dynamic_pattern = [
        (r'[a-zA-Z]+', Token.Name),
        (r'\d+', Token.Number),
    ]
    dynamic_lexer = create_dynamic_lexer(dynamic_pattern)
    code = "123 abc"
    for result in dynamic_lexer().get_tokens_unprocessed(code):
        print(result)


if __name__ == '__main__':
    main()