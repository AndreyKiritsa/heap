def sortBranch(x):
    c = True
    for i in x[1::]:
        if x[0] > i:
            c = False
            break
        else:
            c = True
    return c



def get_rock(Data):
    Data = list(map(int, Data))
    boolNum = True
    i = 1
    left = i * 2
    right= i *2 + 1
    l = []
    length = len(Data)
    while left <= length:
        l.append(Data[i-1])
        l.append(Data[left-1])
        if right <= length:
            l.append(Data[right-1])
        i += 1
        left = i * 2
        right = i * 2 + 1
        if not sortBranch(l):
            boolNum = False
            break
        l.clear()
    if boolNum:
        with open('output.txt', 'w', encoding = 'utf8') as file:
            file.write('YES')
    else:
        with open('output.txt', 'w', encoding = 'utf8') as file:
            file.write('NO')




def main():
    with open('input.txt', 'r', encoding = 'utf8') as data:
        count = int(data.readline())
        Data = data.readline().split()
    get_rock(Data)

if __name__ == '__main__':
    main()