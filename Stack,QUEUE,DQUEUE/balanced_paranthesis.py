def balance_check(s):
    
    # Check is even number of brackets
    if len(s)%2 != 0:
        return False
    
    # Set of opening brackets
    opening = set('([{') 
    
    # Matching Pairs
    matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
    stack = []
    
    for paren in s:
        
        if paren in opening:
            stack.append(paren)
        
        else:
            
            if len(stack) == 0:
                return False
            
            last_open = stack.pop()
            
            if (last_open,paren) not in matches:
                return False
            
    return len(stack) == 0

print(balance_check('((({{{}}})))'))