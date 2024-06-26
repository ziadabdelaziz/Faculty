# Mini-Compiler

## Intro
* this mini-compiler will work with structured programs.
* the language named **Z**.


## **Grammer**
### Lexical elements:
* **keyword:** `if` | `let` | `int` | `string`
* **symbol:** `{` | `}` | `(` | `)` | `,` | `;`  | `+` | `-` | `*` | `/` | `&` | `|` | `<` | `>` | `=` | `~`
* **integer_constant:** a decimal number
* **string_constant:** `"` sequence of unicode characters not including double quote or newline `"`
* **identifier:** sequence of letters, digits not starting with a digit

### Statements:
* **statement:** dec_statement | let_statement | if_statement
* **statements:** statement*
* **if_statement:** `if` `(` expression `)` `{` statements `}`
* **let_statement:** `let` identifier `=` expression `;`
* **dec_statement:** type identifier `=` expression `;`

### Expressions:
* **expression:** term (op term)?
* **term:** identifier | integer_constant | string_constant
* **op:** `+` | `-` | `*` | `=` | `>` | `<` | `<=` | `>=` | `==` | `!=`
* **type:** `int` | `string`

### Rules
* **Terminals:**: keyword, symbol, integer_constant, string_constant, identifier
* **Non-Terminals:** statements, let_statement, if_statement, dec_statement, expression_list, expression, term

* examples:
* `int x = 5;`
* `int y = x + 2;`
* `if ( x > y ) { let x = x - 2 ; }`
