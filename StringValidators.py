if __name__ == '__main__':
    s = input()
    a = [0 for i in range(5)]
    for i in s:
        if i.isdigit():
            a[0]=1
            a[2]=1
        elif i.isalpha():
            a[0]=1
            a[1]=1
            if i.isupper():
                a[4]=1
            else:
                a[3]=1
    for i in a:
        if i == 1:
            print(True)
        else:
            print(False)
