def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mx = a
    if mx > b:
        mx = a
    if b > a:
        mx = b
    if c > b:
        mx =  c
    return mx
print(main(22, 4, 1))