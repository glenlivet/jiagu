import jiagu

jiagu.load_userdict('dict/user.dict')

# load file
contract_file = open("contract.txt", "r")
contract_contents = contract_file.read()
ner = jiagu.ner(contract_contents)
content_arr = list(contract_contents)
for i in range(len(content_arr)):
    if (content_arr[i] != '\n'):
        print(content_arr[i] + ' ' + ner[i])
    else:
        print()
