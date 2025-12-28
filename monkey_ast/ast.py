from abc import ABC, abstractmethod
from monkey_token.token import Token, TokenType

"""
let x = 10;
let y = 20;
let add = fn(a, b) { return a + b; }

1. `let` statement:
    ```
    let <identifer> = <expression>;
    ```
    - identifer: Node that contains an identifier for the value
    - expression : Node that contains a value
"""

# ---BASE-INTERFACES---
class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass

class Statement(Node):
    @abstractmethod
    def statement_node(self):
        pass

class Expression(Node):
    @abstractmethod
    def expression_node(self):
        pass


## --PROGRAM--
class Program(Node):
    """This Program node is going to be the root node of every AST our parser produces."""
    def __init__(self):
        self.statements: list[Statement] = []
    
    def token_literal() -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        return ""

## ---STATEMENTS---
class LetStatement(Statement):
    def __init__(self, token: Token, name: str, value: str):
        self.token: Token = token       # <TokenType.LET, "Let">
        self.name: Identifier  = name   # Identifier
        self.value: Expression = value  # Expression

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.Literal

    def log(self) -> str:
        # (LET)let (IDENT)x (EQUALS)=
        data = [
            f"<{self.token.Type}> {self.token.Literal}",
            f"<{self.name.token.Type}> {self.name.value}",
            self.value,
        ]
        print(data)


## --IDENTIFIERS--
class Identifier(Expression):
    def __init__(self, token: Token, value: str):
        self.token = token      # TokenType.IDENT
        self.value = value

    def expression_node(self):
        return None

    def token_literal(self) -> str:
        return self.token.Literal

