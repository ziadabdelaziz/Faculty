# Mini-Compiler

## Intro
* this mini-compiler will work with structured programs.
* the language named **Z**.
* 

## **Grammer**
### Lexical elements:
* **keyword:** `if` | `let` | `int` | `string` | `true` | `false`
* **symbol:** `{` | `}` | `(` | `)` | `[` | `]` | `,` | `;`  | `+` | `-` | `*` | `/` | `&` | `|` | `<` | `>` | `=` | `!`
* **integerConstant:** a decimal number
* **StringConstant:** 

### Program Structure

### Statements:
* **statement:** letStatement | ifStatement | declareStatement
* **statements:** statement*
* **ifStatement:** `if` `(` expression `)` `{` statements `}`
* **letStatement:** `let` varName `=` expression `;`
* **letStatement:** type varName (`=` expression)? `;`

### Expressions:
* **op:** `+` | `-` | `*` | `=` | `>` | `<`
* **type:** `bool` | `int` | `char` | `string`
* **expression:** term (op term)?
* **term:** varName | constant
* **varName:** a string not beginning with a digit
* **constant:** a decimal number | string wraped with double quotes

* examples:
* `let x = 5;`
* `let y = x + 2`
* `if ( x > y ) { let x = x - 2 ; }`

### Rules
* **Terminals:**: keyword, symbol, constant
