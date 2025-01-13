def occurencesofSubsting(mainstr,substr):
    start=0
    positions=[]
    while start<len(mainstr):
        pos=mainstr.find(substr,start) # find() searches for a substring within a string and returns the index of its first occurrence
        if pos==-1:
            break
        positions.append(pos)
        start=pos+1
    return positions
mainstr=input('enter mainstr:')
substr=input('enter substr:')
print(occurencesofSubsting(mainstr,substr))