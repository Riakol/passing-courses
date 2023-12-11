def pretty_print(data, side='-', delimiter='|'):
    s2 = delimiter + " "+ f' {delimiter} '.join(map(str, data)) + " " + delimiter
    s = " "+ (len(s2)-2)* side + " "
    print(s)
    print(s2)
    print(s) 

