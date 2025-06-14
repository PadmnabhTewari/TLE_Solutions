for _ in range(int(input())):
    a = input()
    b = input()
    s=0
    for length in range(len(a), -1, -1):
        for i in range(len(a) - length + 1):
            cur_substring = a[i:i + length]
            if cur_substring in b:
                print(len(a) + len(b) - 2 * length)
                s=s+1
                break
        if(s>0):
            break
    if(s>0):
        continue
    a, b = b, a
    for length in range(len(a), -1, -1):
        for i in range(len(a) - length + 1):
            cur_substring = a[i:i + length]
            if cur_substring in b:
                print(len(a) + len(b) - 2 * length)
