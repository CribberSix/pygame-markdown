from typing import List, Dict
import re


def interpret_text_blocks(self, text_cut: List) -> List[Dict]:
    """
    Receives a list of text blocks.
    Interprets each block by the starting character (if a key, else normal text) and creates a dict with the keys:
    - chars : String
    - type: String
    """

    text_blocks = []
    for line in text_cut:

        # ___ Headers ___
        if re.search(self.pattern_h3, line) is not None:
            text_blocks.append({'chars': line.lstrip()[3:].lstrip(), 'type': 'h3'})
        elif re.search(self.pattern_h2, line) is not None:
            text_blocks.append({'chars': line.lstrip()[2:].lstrip(), 'type': 'h2'})
        elif re.search(self.pattern_h1, line) is not None:
            text_blocks.append({'chars': line.lstrip()[1:].lstrip(), 'type': 'h1'})

        # ___ Coding blocks ___
        elif re.search(self.pattern_code, line, re.DOTALL) is not None:
            # with newline characters
            text_blocks.append({'chars': line, 'type': 'code'})

        # ___ Quote blocks ___
        elif re.search(self.pattern_quote, line) is not None:
            text_blocks.append({'chars': line[1:].lstrip(), 'type': 'quote'})

        # ___ Unordered List blocks ___
        elif re.search(self.pattern_unorderedList, line) is not None:
            text_blocks.append({'chars': line, 'type': 'unorderdList'})

        # ___ Horizontal rule ___
        elif re.search(self.pattern_hrule, line) is not None:
            text_blocks.append({'chars': line, 'type': 'horizontalRule'})

        # ___ Normal text
        else:
            text_blocks.append({'chars': line, 'type': 'text'})

    return text_blocks
