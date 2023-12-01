"""Script that generates the sum of all the calibration values. """

# let's take the calibration document
with open(file='12-1\\input.txt', encoding='utf-8') as file:
    calibration_document: str = file.read()

def find_text_number(test: str, index: int, inverted: bool = False) -> int:
    """_summary_

    :param test: _description_
    :type test: str
    :param index: _description_
    :type index: int
    :param inverted: _description_, defaults to False
    :type inverted: bool, optional
    :raises ValueError: _description_
    :return: _description_
    :rtype: int
    """
    if not inverted:
        if test[index] == 'o' and test[index+1] == 'n' and test[index+2] == 'e':
            return 1
        elif test[index] == 't' and test[index+1] == 'w' and test[index+2] == 'o':
            return 2
        elif test[index] == 't' and test[index+1] == 'h' and test[index+2] == 'r' and test[index+3] == 'e' and test[index+4] == 'e':
            return 3
        elif test[index] == 'f' and test[index+1] == 'o' and test[index+2] == 'u' and test[index+3] == 'r':
            return 4
        elif test[index] == 'f' and test[index+1] == 'i' and test[index+2] == 'v' and test[index+3] == 'e':
            return 5
        elif test[index] == 's' and test[index+1] == 'i' and test[index+2] == 'x':
            return 6
        elif test[index] == 's' and test[index+1] == 'e' and test[index+2] == 'v' and test[index+3] == 'e' and test[index+4] == 'n':
            return 7
        elif test[index] == 'e' and test[index+1] == 'i' and test[index+2] == 'g' and test[index+3] == 'h' and test[index+4] == 't':
            return 8
        elif test[index] == 'n' and test[index+1] == 'i' and test[index+2] == 'n' and test[index+3] == 'e':
            return 9
    if test[index] == 'e' and test[index-1] == 'n' and test[index-2] == 'o':
        return 1
    elif test[index] == 'o' and test[index-1] == 'w' and test[index-2] == 't':
        return 2
    elif test[index] == 'e' and test[index-1] == 'e' and test[index-2] == 'r' and test[index-3] == 'h' and test[index-4] == 't':
        return 3
    elif test[index] == 'r' and test[index-1] == 'u' and test[index-2] == 'o' and test[index-3] == 'f':
        return 4
    elif test[index] == 'e' and test[index-1] == 'v' and test[index-2] == 'i' and test[index-3] == 'f':
        return 5
    elif test[index] == 'x' and test[index-1] == 'i' and test[index-2] == 's':
        return 6
    elif test[index] == 'n' and test[index-1] == 'e' and test[index-2] == 'v' and test[index-3] == 'e' and test[index-4] == 's':
        return 7
    elif test[index] == 't' and test[index-1] == 'h' and test[index-2] == 'g' and test[index-3] == 'i' and test[index-4] == 'e':
        return 8
    elif test[index] == 'e' and test[index-1] == 'n' and test[index-2] == 'i' and test[index-3] == 'n':
        return 9
    raise ValueError

def find_calibration_value(row: str) -> int:
    """For each calibration line, return the number to add.

    :param input: the line of the calibration document
    :type input: str
    :return: the number to add to the total by the caller.
    :rtype: int
    """
    i_left: int = 0
    i_right: int = -1
    done: bool = False
    primo: int = -1
    ultimo: int = -1
    while not done:
        try:
            primo = int(row[i_left])
        except ValueError:
            try:
                primo = find_text_number(row, i_left)
            except ValueError:
                i_left += 1
        try:
            ultimo = int(row[i_right])
        except ValueError:
            try:
                ultimo = find_text_number(row, i_right)
            except ValueError:
                i_right -= 1
        if primo>0 and ultimo >0:
            done = True
            aggiungere: str = str(primo) + str(ultimo)
    return int(aggiungere)

lines: list = calibration_document.split()
sum_of_calibration_values: int = 0
for line in lines:
    sum_of_calibration_values += find_calibration_value(line)
print(sum_of_calibration_values)
