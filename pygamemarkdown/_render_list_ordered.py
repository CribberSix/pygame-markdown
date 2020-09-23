from typing import List


def prep_ordered_list(self, textlist: List) -> List:
    """
    Prepare the lines of an ordered list by removing all supplied numbers
    and inserting new ones (e.g. also correcting numbers which are out of order).
    Inserts a placeholder for the indentation.
    """
    res = []
    for i, line in enumerate(textlist):
        dot_index = line.find('.') + 2
        if i + 1 < 10:  # further identation at all times if num 1-9
            res.append('___' + str(i+1) + '. ' + line[dot_index:])
        else:
            res.append('__' + str(i+1) + '. ' + line[dot_index:])

    return res
