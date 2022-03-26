import functools


def handler(f):
    """Handles exceptions"""

    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as ex:
            raise Exception(ex)

    return func


@handler
def read(filename):
    """Read file and return list"""
    with open(filename, 'r') as file:
        return file.readlines()


@handler
def remove_line_break(line):
    """Remove line breaks from list, return list"""
    result = []
    for li in line:
        result.append(li.rstrip(li[-1]))
    return result


@handler
def remove_whitespace(elements):
    """Remove line breaks from list, return list"""
    result = []
    for element in elements:
        replaced = element.replace(' ', '')
        if replaced is not '':
            result.append(replaced)
    return result


@handler
def findall(p, s):
    """Yields all the positions of the pattern p in the string s."""
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i + 1)


@handler
def del_empty(matrix):
    """Delete empty elements in matrix"""
    i = 0
    while i < len(matrix) and len(matrix) > 0:
        if len(matrix[i]) == 0:
            del matrix[i]
        else:
            i += 1


@handler
def count_match(bug, matches):
    """Count the number of matches"""
    bug_str = ' '.join(map(str, bug))
    matches_str = ' '.join(map(str, [g[1] for g in matches]))
    return matches_str.count(bug_str)


@handler
def finder(file_bug, file_landscape):
    """Prepare the data for search"""
    number_bugs = 0
    """Read and clean data"""
    dirt_bug = read(file_bug)
    dirt_landscape = read(file_landscape)
    result = []
    bug = remove_line_break(dirt_bug)
    landscape = remove_line_break(dirt_landscape)
    """Search for matches for each item in the bug"""
    for ls in landscape:
        current = []
        for b in bug:
            current += [(i, ls[i:i + len(b)]) for i in findall(b, ls)]
        result.append(current)
    """Iterate matrix of tuples until empty"""
    while len(result) > 0:
        """Remove empty rows"""
        del_empty(result)
        """Break if matrix is empty after remove rows"""
        if len(result) == 0:
            break
        """Get first element"""
        to_compare_element = result[0][0]
        """Remove it"""
        del result[0][0]
        i = 1
        """Search for items by index matching"""
        matches = [to_compare_element]
        while i < len(result):
            j = 0
            while j < len(result[i]):
                if result[i][j][0] == to_compare_element[0]:
                    matches.append(result[i][j])
                    """Remove appended element"""
                    del result[i][j]
                    """To treat the irregular matrix as a transpose"""
                    break
                j += 1
            if len(result[i]) == 0:
                """Remove empty rows"""
                del_empty(result)
            else:
                i += 1
        """Get number of matches"""
        number_bugs += count_match(bug, matches)
    return number_bugs
