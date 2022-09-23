'''def print_keys(dic):
    return dic[:]

print(print_keys({"이름": "김말똥", "나이": 30, "성별":0}))'''

def print_keys(dic):
    for keys in dic.keys():
        print(keys)
        
print_keys({"이름":"김말똥", "나이":30, "성별":0})