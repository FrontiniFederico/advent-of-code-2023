"""Script that generates the sum of all the calibration values. """

# let's take the calibration document
with open(file='12-1\\input.txt', encoding='utf-8') as file:
    calibration_document: str = file.read()

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
            i_left += 1
        try:
            ultimo = int(row[i_right])
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
print(sum_of_calibration_values) #the right answer is 56049
