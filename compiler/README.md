# Mini-Compiler

## Intro
* this mini-compiler will work with structured programs.
* the language named **Z**.


## **Grammer**
### Lexical elements:
* **keyword:** `if` | `let` | `int` | `string` | `true` | `false`
* **symbol:** `{` | `}` | `(` | `)` | `[` | `]` | `,` | `;`  | `+` | `-` | `*` | `/` | `&` | `|` | `<` | `>` | `=` | `~`
* **integer_constant:** a decimal number
* **string_constant:** `"` sequence of unicode characters not including double quote or newline `"`
* **identifier:** sequence of letters, digits, and underscore (`_`) not starting with a digit

### Program Structure
* **condition:** `if` `(` expression+ `)` such that
* **subroutine:** `{` statment* `}`

### Statements:
* **statement:** dec_statement | let_statement | if_statement
* **statements:** statement*
* **if_statement:** `if` `(` expression `)` `{` statements `}`
* **let_statement:** `let` identifier `=` expression `;`
* **dec_statement:** type identifier (`=` expression_list)? `;`

### Expressions:
* **expression_list:** (expression (`,`expresion)*)?
* **expression:** term (op term)?
* **term:** identifier | integer_constant | string_constant | identifier`[`expression`]` | `(`expression`)` | unary_op term
* **op:** `+` | `-` | `*` | `=` | `>` | `<`
* **unary_op:** `~`
* **type:** `bool` | `int` | `char` | `string`
<!-- * **varName:** a string not beginning with a digit
* **constant:** a decimal number | string wraped with double quotes -->

* examples:
* `let x = 5;`
* `let y = x + 2`
* `if ( x > y ) { let x = x - 2 ; }`

### Rules
* **Terminals:**: keyword, symbol, integer_constant, string_constant, identifier
* **Non-Terminals:** statements, let_statement, if_statement, dec_statement, expression_list, expression, term
