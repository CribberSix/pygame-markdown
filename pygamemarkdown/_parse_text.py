from typing import List, Dict
import re


def parse_into_text_blocks(self, text: List[str]) -> List[str]:
    """
    Parses physical lines into logical lines.

    Takes a list of strings - directly from a loaded Markdown file, one string per line.
    Parses elements of the lists and connects common blocks going over multiple lines.

    Returns a list of Strings as a result with each block as one element.
    - coding block
    - quote block
    - normal text block
    - unordered List blocks (second level indentation possible)
    - ordered list blocks (no second level indentation possible)
    - header lines
    - normal text blocks
    """
    cleaned_lines = []
    current_line = ''
    code_flag = False
    unordered_List_flag = False
    ordered_List_flag = False
    quote_flag = False

    def clean_current_line(c_line):
        if c_line != '':
            cleaned_lines.append(c_line)
        return ''

    for line in text:
        # Identify the end of a bullet-point block
        if unordered_List_flag and (re.search(self.pattern_header, line) is not None
                                   or re.search(self.pattern_code, line) is not None
                                   or re.search(self.pattern_orderedList, line) is not None
                                   or re.search(self.pattern_hrule, line) is not None
                                   or re.search(self.pattern_quote, line) is not None
                                   or line == ''):
            current_line = clean_current_line(current_line)
            unordered_List_flag = False

        elif ordered_List_flag and (re.search(self.pattern_header, line) is not None
                                   or re.search(self.pattern_code, line) is not None
                                   or re.search(self.pattern_unorderedList, line) is not None
                                   or re.search(self.pattern_hrule, line) is not None
                                   or re.search(self.pattern_quote, line) is not None
                                   or line == ''):
            current_line = clean_current_line(current_line)
            ordered_List_flag = False

        elif quote_flag and (re.search(self.pattern_header, line) is not None
                           or re.search(self.pattern_code, line) is not None
                           or re.search(self.pattern_orderedList, line) is not None
                           or re.search(self.pattern_hrule, line) is not None
                           or re.search(self.pattern_unorderedList, line) is not None
                           or line == ''):
            current_line = clean_current_line(current_line)
            quote_flag = False

        # ___ CODE ____
        if re.search(self.pattern_code, line) is not None and not code_flag:  # Start of a code block
            code_flag = True
            clean_current_line(current_line)
            current_line = line
        elif re.search(self.pattern_code, line) is not None and code_flag:  # End of a code block
            code_flag = False
            current_line = current_line + '\n' + line
            current_line = clean_current_line(current_line)
        elif code_flag:  # middle of a code block
            current_line = current_line + '\n' + line

        # ___ HEADERS ____
        elif re.search(self.pattern_header, line) is not None:
            current_line = clean_current_line(current_line)
            cleaned_lines.append(line)

        # ___ QUOTES ___
        elif re.search(self.pattern_quote, line) is not None:
            if not quote_flag:  # first line of a quote-block
                quote_flag = True
                clean_current_line(current_line)
                current_line = line
            else:  # quote_flag active
                current_line = current_line + line[1:]

        # ___ UNORDERED LIST ____
        elif re.search(self.pattern_unorderedList, line) is not None:
            if not unordered_List_flag:  # first bullet point
                clean_current_line(current_line)
                unordered_List_flag = True
                current_line = line.lstrip()
            else:
                if re.search(self.pattern_uList_first_indent, line):  # (0-3 whitespaces)
                    current_line = current_line + '\n' + line.lstrip()
                elif re.search(self.pattern_uList_second_indent, line) is not None:  # (4 whitespaces)
                    current_line = current_line + '\n    ' + line.lstrip()
                else:  # (5 or more whitespaces -> text continuation)
                    current_line = current_line.rstrip() + ' ' + line.lstrip()

        # ___ ORDERED LIST ____
        elif re.search(self.pattern_orderedList, line) is not None:
            if not ordered_List_flag:
                ordered_List_flag = True
                clean_current_line(current_line)
                current_line = line
            elif ordered_List_flag:
                current_line = current_line + "\n" + line.lstrip()

            # ___ HORIZONTAL RULE ___
        elif re.search(self.pattern_hrule, line) is not None:
            clean_current_line(current_line)
            current_line = clean_current_line(line.lstrip().rstrip())

        # ___ EMPTY LINE -> BLOCK BREAK ____
        elif line == '':
            current_line = clean_current_line(current_line)

        # ____ BLOCK CONTINUES ____
        else:
            # remove any leading / trailing whitespaces
            # and insert exactly one whitespace after first line
            if current_line != '':
                current_line = current_line.rstrip() + ' ' + line.lstrip()
            else:
                current_line = current_line + line

    # Append current/last line still in the var
    clean_current_line(current_line)

    return cleaned_lines
