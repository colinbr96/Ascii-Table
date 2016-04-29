def tableify(l: list)-> str:
    #Creates an ASCII table out of a 'rectangular' list of lists.
    #Flip the axes to iterate through columns rather than rows.
    rows = len(l)
    flipL = _flip_axes(l)
    
    #Iterate down the columns (not rows) to find the longest element.
    columnLengths = []
    for c in flipL:
        length = 0
        for r in c:
            n = len(str(r))
            if(n > length):
                length = n
        columnLengths.append(length)

    #Construct table string
    stringRow = []
    for r in range(0, 2*rows + 1):
        actualRow = int((r - 1)/2)
        if((r)%2 == 0):
            s = ""
            for c in columnLengths:
                s += "+"
                s += ("-" * (c + 2))
            s += "+"
            stringRow.append(s)
        else:
            s = ""
            for i, c in enumerate(l[actualRow]):
                s += ("| " + str(c) + " " + (" " * (columnLengths[i] - len(str(c)))))
            s += "|"
            stringRow.append(s)

    #Return the table string
    output = ""
    for r in stringRow:
        output += (str(r) + "\n")
    return output


def _flip_axes(l: list)-> list:
    #Changes a list of lists from [rows, columns] to [columns, rows] and vice versa.
    newList = []
    for i in range(0, len(l[0])):
        newSubList = []
        for subList in l:
            newSubList.append(subList[i])
        newList.append(newSubList)
    return newList
