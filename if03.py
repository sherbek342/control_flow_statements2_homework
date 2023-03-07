def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.123
    """
    bet = c
    if a<=b:
        if b<=c:
            bet=b
        elif a>=c:
            bet=a
    else:
        if a<=c:
            bet=a
        elif b>=c:
            bet=b


    return bet  


print(main(2,3,-4))