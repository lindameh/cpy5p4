def reverse_int(n):
    num = len(str(n)) - 1
    if n // 10 == 0:
        return n
    else:
        return n % 10 * (10 ** num) + reverse_int(n // 10)
    
print(reverse_int(12345))
