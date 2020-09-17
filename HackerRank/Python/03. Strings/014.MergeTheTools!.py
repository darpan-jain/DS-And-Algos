from collections import OrderedDict
def merge_the_tools(string, k):
    to=list()
    for i in range(0,len(string),k):
        to.append(string[i:i+k])

    for w in to:
        print("".join(OrderedDict.fromkeys(w)))

