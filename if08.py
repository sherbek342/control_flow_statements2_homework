def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    m = "Monday"
    t = "Tuesday"
    w =  "Wednesday"
    th = "Thursday"
    f = "Friday"
    sa = "Saturday"
    s = "Sunday"
    if number == 1:
        return m
    if number == 2:
        return t
    if number == 3:
        return w
    if number == 4:
        return th
    if number == 5:
        return f
    if number == 6:
        return sa
    if number == 7:
        return s
print(main(5))