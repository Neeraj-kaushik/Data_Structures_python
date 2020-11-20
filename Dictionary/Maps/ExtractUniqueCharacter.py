def uniqueChars(string):
    new_string = ""
    for i in range(len(string)):
        if string[i] not in new_string:
            new_string += string[i]
        
    return new_string  
    
    
string = input()
print(uniqueChars(string))
