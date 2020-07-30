def removex(string):
    l=len(string)
    if l==0:
        return string
    
    smalla=removex(string[1:])
    if string[0]=='x':
        return smalla
    else:
        return string[0]+smalla

# Main
string = input()
print(removex(string))