import re
def frequencyCount(istring, substrings):
    match_table = {}
    for substring in substrings:
        match_positions = [position.start() for position in re.finditer(substring, istring)]
        for match_position in match_positions:
            for offset in (match_position, match_position + len(substring) - 1):
                match_table[offset] = match_table.get(offset, 0) + 1
    return match_table
