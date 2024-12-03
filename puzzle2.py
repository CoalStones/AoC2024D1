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
    occurances = []
    
    
    for i in range (len(l1)):
        j = 0
        appearance = 0
        if i != 0 and l1[i] == l1[i-1]:
            occurances.append(occurances[i-1])
        else:
            for datum in l2:
                if l1[i] == datum:
                    j += 1
                    appearance += 1
                if datum > l1[i]:
                    break
            occurances.append(appearance)
        # print(occurances[i])
       
    total = 0 
    for i in range (len(occurances)):
        total += l1[i] * occurances[i]
        
    print(total)
        
    # find how many times numbers in l1 occur in l2
        