def sum_series2(n):
    if n == 1:
        return 1/3
    else:
        return sum_series2(n-1) + n / (2 * n + 1)

n = int(input("Enter a positive integer: "))
print("m({0}) = {1}".format(n, sum_series2(n)))
