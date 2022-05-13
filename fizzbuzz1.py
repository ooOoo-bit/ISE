def fizzbuzz():
    n = int(input())
    lst = [1, 2, 'F', 4, "B", "F", 7, 8 ,"F", "B", 11, "F", 13, 14, "FB"]

    for i in range(0,n):
        #a = i // 15
        if isinstance(lst[i - i // 15], int):
            print(lst[i] + 15 * (i // 15))
        else:
            print(lst[i - i // 15])

if __name__ == "__main__":
     fizzbuzz()

