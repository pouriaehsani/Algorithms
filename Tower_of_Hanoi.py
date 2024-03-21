def hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from tower ", source, "to tower ", target)
        return
    hanoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from tower", source, "to tower", target)
    hanoi(n-1, auxiliary, target, source)


n = 3  
hanoi(n, 'a', 'b', 'c')