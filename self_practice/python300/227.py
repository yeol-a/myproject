def printmxn(string, n):
    chunk_num = int(len(string)/n)
    for i in range(chunk_num+1):
        print(string[i*3:i*3+2])
printmxn("아이엠어보이유알어걸", 3)