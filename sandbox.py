### How Bills are going to be Processed ###

tag = True

sampleList = []

while tag == True:
    dict = {}
    key = input("name of bill: ")
    value = input("amount: ")

    dict.update({key,value})

    if key == "done":
        tag = False
    elif value == "done":
        tag = False
    else:
        print(key)
        print(value)
        sampleList.append(dict)

print(sampleList)
