def insertionSort(n, arr):
    # print(n, arr)
    new_arr = [arr[0]]
    i = 1
    # print(new_arr)
    while(i < len(arr)):
        print(arr[i])
        to_replace = arr[i]
        k = 0
        s = len(new_arr)
        while(k < s):
            flag = 'no'
            print('k-->', k, 's-->', s)
            print(new_arr[k], '>', to_replace)
            if new_arr[k] > to_replace:
                new_arr.insert(k, to_replace)
                print(new_arr, 'iffff')
                flag = 'yes'
                break
            else:
                pass
            if len(new_arr) == 1:
                new_arr.append(to_replace)
            print(new_arr, '------->')
            k += 1
        print(flag)
        if flag is not 'yes':
            new_arr.append(to_replace)
        print("-------------------------------------------------")
        i += 1


if __name__ == '__main__':
    n = 6
    arr = [1, 4, 3, 5, 6, 2]
    insertionSort(n, arr)
