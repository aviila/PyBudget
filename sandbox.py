### How Bills are going to be Processed ###

tag = True

sampleList = []

while tag == True:
    dict = {}
    key = input("name of bill: ")
    if key == "done":
        tag = False

    value = input("amount: ")
    if value == "done":
        tag = False
    dict.update({str(key):int(value)})

    print("\n")
    sampleList.append(dict)
    print(sampleList)
