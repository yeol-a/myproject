def make_list(string):
    a = []
    for i in range(len(string)):
        a.append(string[i])
    return a

print(make_list("abcd"))