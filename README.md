# litprog - Quick and dirty "literate" programming
`litprog` is a quick tool that is useful for splitting comments
in a source code file into a markdown document that can be rendered.
The resulting document has all of the "literate comments" (i.e. comments
beginning with a certain prefix) rendered as regular markdown, with the code
rendered in code blocks. 

### Usage
```
Usage: litprog [OPTIONS] INPUT_FILE

  A converter for "literate" programs into a markdown file that combines the
  literate comments with the source code. Prints the markdown file to
  standard out.

Options:
  --language [ruby|c++|c|rust|javascript|python]
                                  The language profile to use
  --help                          Show this message and exit.
```
`litprog` currently writes the generated file to standard out.

### Literate comments
The type of comment that `litprog` recognizes varies from language
to language. Here are the sequences that begin a "literate" comment:

* C/C++/Javascript - `//=`
* Ruby/Python - `#=`
* Rust - `//!`

The Rust comment is identical to the comment that `rustdoc` accepts and renders
in markdown. I'm not sure if that's useful yet.

### Installation
You can install a working copy of `litprog` using
```
pip install --editable .
```

Haven't tried anything else yet.