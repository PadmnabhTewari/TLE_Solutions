for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    fa = [0] * (2 * n + 1)
    fb = [0] * (2 * n + 1)
    l = 0
    for j in range(n):
        if j > 0 and a[j] != a[j - 1]:
            l = 0
        l += 1
        fa[a[j]] = max(fa[a[j]],l)

    l = 0
    for j in range(n):
        if j > 0 and b[j] != b[j - 1]:
            l = 0
        l += 1
        fb[b[j]] = max(fb[b[j]], l)

    ans = 0
    for k in range(2 * n + 1):
        ans = max(ans, fa[k] + fb[k])

    print(ans)
