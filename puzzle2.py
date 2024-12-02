import re


if __name__ == "__main__":
    # gathering input
    with open("input.txt") as file:
        data = file.read()
        
    data = re.split(r'   |\n', data)
        
    l1 = []
    l2 = []
    i = 0
    # splitting it into lists
    for datum in data:
        if i % 2 == 0 and datum.isdigit():
            l1.append(int(datum))
        elif datum.isdigit():
            l2.append(int(datum))
        i += 1
        
    # sorting the list acending
    l1.sort()
    l2.sort()
    oc2 = []
    
    for i in range (len(l1)):
        
        
    # find how many times numbers in l1 occur in l2