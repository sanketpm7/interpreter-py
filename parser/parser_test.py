import pytest
from lexer.lexer import Lexer
from monkey_token.token import Token
from monkey_ast.ast import Program, Statement, LetStatement, Identifier
from parser.parser import Parser

def test_let_statements():
    input_text = (
"""
let x = 5;
let y = 10;
let foobar = 838383;
""")

    lexer = Lexer(input_text)
    parser = Parser(lexer)
    program = parser.Parse_Program()

    assert len(program.statements) != 0, "ParseProgram() returned empty Program object"
    assert len(program.statements) == 3, (
        f"program.statements does not contain 3 statements. "
        f"got={len(program.statements)}"
    )

    tests = ["x", "y", "foobar"]

    for i, expected_identifier in enumerate(tests):
        stmt = program.statements[i]
        assert check_let_statement(stmt, expected_identifier)


def check_let_statement(stmt: Statement, name: str) -> bool:
    assert stmt.token_literal() == "let", (
        f"stmt.token_literal() not 'let'. got={stmt.token_literal()}"
    )

    assert isinstance(stmt, LetStatement), (
        f"stmt not LetStatement. got={type(stmt)}"
    )

    assert stmt.name.value == name, (
        f"stmt.name.value not '{name}'. got={stmt.name.value}"
    )

    assert stmt.name.token_literal() == name, (
        f"stmt.name.token_literal() not '{name}'. got={stmt.name.token_literal()}"
    )

    return True

