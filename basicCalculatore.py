def cal(strings):

    strings = strings.replace(" ", "")   
    stack = []
    oprands = ["+", "-", "*", "/"]
        
    op = "+"
    temp = 0 
        
    for i in range(len(strings)):
        curr = strings[i]
            
        if curr not in oprands:
            temp = temp * 10 + int(curr)
        if curr in oprands or i == len(strings) - 1:
            if op == "+":
                stack.append(temp)
            elif op == "-":
                stack.append(-temp)
            elif op == "*":
                temp = temp * stack.pop()
                stack.append(temp)
            else:
                div = stack.pop()
                    
                if div > 0:
                    stack.append(div // temp)
                else:
                    stack.append(-1 * (-div // temp))
            
            op = curr
            temp = 0
    return sum(stack)
                
             
