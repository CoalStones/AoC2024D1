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
    
    total = 0
    for i in range (len(l1)):
        print(str(i+1) + ": adding " + str(abs(l2[i] - l1[i])) + " to total " + str(total))
        total += abs(l2[i] - l1[i])
        
    print(total)
        