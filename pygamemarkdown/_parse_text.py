from typing import List, Dict


def parse_into_text_blocks(self, text: List[str]) -> List[str]:
    """
    Parses physical lines into logical lines.

    Takes a list of strings - directly from a loaded Markdown file, one string per line.
    Parses elements of the lists and connects common blocks going over multiple lines.

    Returns a list of Strings as a result with each block as one element.
    - coding paragraph
    - bullet point paragraph
    - normal text paragraph
    - Header lines
    """
    cleaned_lines = []
    current_line = ''
    code_flag = False
    bullet_points_flag = False
    quote_flag = False
    for line in text:

        def clean_current_line(current_line):
            if current_line != '':
                cleaned_lines.append(current_line)
                return ''
            return ''

        # Identify the end of a bullet-point block
        if bullet_points_flag and (line[:1] == '#' or line[:3] == '```' or line == '' or line[:1] == '>'):
            current_line = clean_current_line(current_line)
            bullet_points_flag = False
        if quote_flag and (line[:1] == '#' or line[:3] == '```' or line == '' or line[:1] == '-'):
            current_line = clean_current_line(current_line)
            quote_flag = False

        # ___ CODE ____
        if line[:3] == '```' and not code_flag:  # Start of a code block
            code_flag = True
            current_line = clean_current_line(current_line)
            current_line = line
        elif line[:3] == '```' and code_flag:  # End of a code block
            code_flag = False
            current_line = current_line + '\n' + line
            cleaned_lines.append(current_line)
            current_line = ''
        elif code_flag:
            current_line = current_line + '\n' + line

        # ___ HEADERS ____
        elif line[:2] == '# ' or line[:3] == '## ' or line[:4] == '### ':
            current_line = clean_current_line(current_line)
            cleaned_lines.append(line)

        # ___ QUOTE BLOCKS ___
        elif line[:2] == '> ' and not quote_flag:
            quote_flag = True
            clean_current_line(current_line)
            current_line = line
        elif line[:2] == '> ' and quote_flag:
            current_line = current_line + line[1:]

        # ___ EMPTY LINE -> BLOCK BREAK ____
        elif line == '':
            current_line = clean_current_line(current_line)

        # ___ BULLET POINTS ____
        elif line[:2] == '- ':
            if not bullet_points_flag:
                clean_current_line(current_line)
                bullet_points_flag = True
                current_line = u'\u2022 ' + line[2:]
            else:
                current_line = current_line + '\n' + u'\u2022 ' + line[2:]

        # ____ BLOCK CONTINUES ____
        else:
            # remove any leading / trailing whitespaces and insert exactly one whitespace
            current_line = current_line.rstrip() + ' ' + line.lstrip()

    # Append current/last line still in the var
    clean_current_line(current_line)

    return cleaned_lines


def interpret_text_blocks(self, text_cut: List) -> List[Dict]:
    """
    Receives a list of text blocks.
    Interprets each block by the starting character (if a key, else normal text) and creates a dict with the keys:
    - chars : String
    - type: String
    """

    text_blocks = []
    code = False
    language = ''
    for line in text_cut:

        # ___ Headers ___
        if line[:2] == '# ':
            text_blocks.append({'chars': line[2:].lstrip(), 'type': 'h1'})
        elif line[:3] == '## ':
            text_blocks.append({'chars': line[3:].lstrip(), 'type': 'h2'})
        elif line[:4] == '### ':
            text_blocks.append({'chars': line[4:].lstrip(), 'type': 'h3'})

        # ___ Coding blocks ___
        elif line[:3] == '```':
             text_blocks.append({'chars': line, 'type': 'code'})

        # ___ Quote blocks ___
        elif line[:2] == '> ':
            text_blocks.append({'chars': line[1:].lstrip(), 'type': 'quote'})

        # ___ Normal text, unordered list, etc.
        else:
            text_blocks.append({'chars': line, 'type': 'text'})

    return text_blocks
