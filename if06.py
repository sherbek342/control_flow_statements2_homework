def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    
    x1 = n%10  
    
    n = n//10      
    x2 = n%10  
    n = n//10  
    
    x3 = n%10  
    n = n//10 
    
    x4 = n%10 
    
    x5 = n//10
    
    mx = x5
    if x4 > mx:
        mx = x4
        
    if x3 > mx:
        mx = x3
    if x2 > mx:
        mx = x2
    if x1 > mx:
        mx = x1
    return 
    
print(main(19345))