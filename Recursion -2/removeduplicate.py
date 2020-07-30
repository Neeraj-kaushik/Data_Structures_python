# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here

    if len(string) == 1:
        return string
    
    if string[0] == string[1]:
        smallOutput = removeConsecutiveDuplicates(string[1:])
        return smallOutput   
    
    else:
        nextOutput = removeConsecutiveDuplicates(string[1:])
        return string[0] + nextOutput

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))