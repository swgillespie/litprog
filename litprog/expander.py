#= ## LiterateExpander
#= LiterateExpander is a language-agnostic mechanism
#= by which "literate" comments can be stripped out of
#= and combined with source code into a markdown document.
import os

class LiterateExpander(object):
    #= Initialize some state. The literate expander is a state machine,
    #= so we initialize our state here.
    def __init__(self, literate_comment, source_language):
        self.in_literate_block = False
        self.in_code_block = False
        self.literate_comment = literate_comment
        self.source_language = source_language

    #= Transforms the source_text into a markdown document by splitting
    #= all lines that begin with `literate_comment` into Markdown-formatted
    #= blocks, while leaving all other lines in code blocks annotated by the source
    #= language.
    def source_to_literate(self, source_text):
        markdown_doc = ""
        lines = source_text.splitlines()
        for line in lines:
            markdown_doc += self.convert_line(line)

        if self.in_code_block:
            markdown_doc += '```' + os.linesep
        return markdown_doc

    #= Converts a single line to Markdown, based on the state of the converter.
    def convert_line(self, line):
        output = ""
        if line.strip().startswith(self.literate_comment):
            if self.in_code_block:
                #= if we are in a code block, we have to terminate
                #= it.
                output += '```' + os.linesep
                self.in_code_block = False
                self.in_literate_block = True
            elif not self.in_literate_block:
                #= if we are not in a literate block, this
                #= starts a literate block.
                #= (usually at the start of the program)
                self.in_literate_block = True
            output += line.strip().strip(self.literate_comment).strip() + os.linesep
        else:
            #= if we are in a literate block and are starting a code block, we
            #= need to start a code tag.
            if self.in_literate_block:
                output += '```' + self.source_language + os.linesep
                output += line + os.linesep
                self.in_literate_block = False
                self.in_code_block = True
            elif self.in_code_block:
                output += line + os.linesep
            else:
                #= if we are not in a literate block or a code block,
                #= this is the start of the doc.
                self.in_code_block = True
                output += line + os.linesep
        return output
