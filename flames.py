
def flames(s1,s2):
    arr1 = set(list(s1))
    arr2 = set(list(s2))

    tmp = []

    for i in arr1:
        if i in arr2:
            tmp.append(i)

    for i in tmp:
        arr1.remove(i)
        arr2.remove(i)

    k = len(arr1) + len(arr2)

    arr = ['Friends','Lovers','Anger','Married','Enenmy','Sibblings']

    while len(arr) != 1:
        rem = len(arr)%k
        if rem == 0:
            arr.remove(arr[-1])
        else:
            arr.remove(arr[rem-1])

    return arr[0]


def main():
    s1 = str(input('Type the first name:'))
    s2 = str(input('Type the second name:'))
    ret = flames(s1,s2)
    print(f'You are {ret}')


main()
    