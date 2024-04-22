def sum_all(*args):
    print(args) # returns tuple
    print(*args) # doesent returns tuple
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))