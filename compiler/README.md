# Mini-Compiler

### Intro
* this mini-compiler will work with structured programs.
* the language named **Z**.
* 

### Grammer
* **statement:** letStatement | ifStatement
* **statements:** statement*
* **ifStatement:** `if` `(` expression `)` `{` statements `}`
* **letStatement:** `let` varName `=` expression `;`
* **expression:** term (op term)?
* **term:** varName | constant
* **varName:** a string not beginning with a digit
* **constant:** a decimal number
* **op:** `+` | `-` | `*` | `=` | `>` | `<`
---
* examples:
* `let x = 5;`
* `let y = x + 2`
* `if ( x > y ) { let x = x - 2 ; }`

