
def insertionSort1(n, arr):
    rep = arr[n - 1]
    while(n >= 1):
        if (n - 2) < 0:
            arr[0] = rep
            print(' '.join([str(x) for x in arr]))
            break
        if arr[n - 2] > rep:
            arr[n - 1] = arr[n - 2]
            print(' '.join([str(x) for x in arr]))
        elif arr[n - 2] < rep:
            print(n)
            arr[n - 1] = rep
            print(' '.join([str(x) for x in arr]))
            break
        else:
            pass

        n -= 1


if __name__ == '__main__':
    n = 10
    arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    insertionSort1(n, arr)
