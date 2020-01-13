import jiagu

jiagu.load_userdict('dict/user.dict')

# load file
contract_file = open("contract.txt", "r")
contract_contents = contract_file.read()
segs = jiagu.seg(contract_contents)
ner = jiagu.ner(segs)
print(segs)
print(ner)
content_arr = list(segs)
for i in range(len(content_arr)):
    if (content_arr[i] != '\n'):
        print('index: ' + str(i) + ':' + content_arr[i] + ' ' + ner[i])
    else:
        print()
