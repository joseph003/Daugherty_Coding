nest = raw_input('Input a string: ')

def nested_sum(nest):
    total = 0  
    if nest == 0:
      return 0 
    for i in nest:
        if isinstance(i, list):  
            total += nested_sum(i)
    return total
