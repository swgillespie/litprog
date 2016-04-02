import click
from litprog.expander import LiterateExpander

LANGUAGE_MAP = {
    'c': LiterateExpander('//=', 'c'),
    'python': LiterateExpander('#=', 'python'),
    'ruby': LiterateExpander('#=', 'ruby'),
    'rust': LiterateExpander('//!', 'rust'),
    'c++': LiterateExpander('//=', 'c++'),
    'javascript': LiterateExpander('//=', 'javascript')
}

@click.command()
@click.option('--language',
              default='c',
              help='The language profile to use',
              type=click.Choice(list(LANGUAGE_MAP.keys())))
@click.argument('input_file', type=click.File('r'))
def convert(language, input_file):
    """
    A converter for "literate" programs into a markdown file
    that combines the literate comments with the source code.
    Prints the markdown file to standard out.
    """
    expander = LANGUAGE_MAP[language]
    result = expander.source_to_literate(input_file.read())
    click.echo(result)
