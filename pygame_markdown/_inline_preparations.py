
def inline_formatting_preparation(self, word, position, code_flag, bold_flag, italic_flag):
    """Recognizes HTML formatting substrings at the start / end of a given word.
    Sets and returns all necessary flags.

    Warning: There can only be one type of format active at the same time.
             Overloading the format of a word with bold and italic is not possible.

    Setting the variable 'position' to 'last' is used to reset the current formatting after the word has been rendered.
    """
    if word[:6] == '<code>':
        code_flag = True
        position = 'first'
        word = word[6:]
    if word[-7:] == '</code>':
        position = 'last'
        word = word[:-7]

    # bold / strong (one-word 'strong' is included)
    if word[:8] == '<strong>':
        bold_flag = True
        position = 'first'
        word = word[8:]
    if word[-9:] == '</strong>':
        position = 'last'
        word = word[:-9]

    # italic (one-word 'italic' is included)
    if word[:4] == '<em>':
        italic_flag = True
        position = 'first'
        word = word[4:]
    if word[-5:] == '</em>':
        position = 'last'
        word = word[:-5]

    return word, position, code_flag, bold_flag, italic_flag