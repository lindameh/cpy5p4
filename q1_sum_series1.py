def sum_series1(n):
    if n==1:
        return 1
    else:
        return sum_series1(n-1) + 1 / n

n = int(input("Enter a positive integer: "))
print("m({0}) = {1}".format(n, sum_series1(n)))
