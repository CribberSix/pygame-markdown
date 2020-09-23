from typing import List
import re
from ast import literal_eval

def prep_unordered_list(self, textlist: List) -> List:
    res = []
    for line in textlist:
        if re.search(self.pattern_uList_first_indent, line) is not None:
            print("FIRST-INDENTATION LEVEL")
            print(line)
            newline = u'\u2022 ' + line[2:]
            res.append(newline)
        elif re.search(self.pattern_uList_second_indent, line) is not None:
            print("SECOND-INDENTATION LEVEL")
            print(line)
            newline = u'____\u25E6 ' + line[6:]
            res.append(newline)

    return res