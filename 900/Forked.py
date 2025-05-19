for i in range(int(input())):
    a,b=map(int, input().split())
    k1,k2=map(int, input().split())
    q1,q2=map(int, input().split())

    s1={
        (k1+a,k2+b),
        (k1+a,k2-b),
        (k1-a,k2+b),
        (k1-a,k2-b),
        (k1+b,k2+a),
        (k1+b,k2-a),
        (k1-b,k2+a),
        (k1-b,k2-a),
    }

    s2 = {(q1+a,q2+b),
(q1+a,q2-b),
(q1-a,q2+b),
(q1-a,q2-b),
(q1+b,q2+a),
(q1+b,q2-a),
(q1-b,q2+a),
(q1-b,q2-a),
    }
    print(len(s1&s2))
