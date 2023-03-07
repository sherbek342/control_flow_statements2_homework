def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mn = a
    if mn < b:
        mn = a
    if b < a:
        mn = b
    if c < b:
        mn =  c
    return mn
print(main(22, 44, 1))