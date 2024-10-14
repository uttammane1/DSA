def three_min_three_max(N, arr):
    if N == 0:
        print("Not Possible")
        print("Not Possible")
        return

    distinct_elements = sorted(set(arr))

    if len(distinct_elements) < 3:
        print("Not Possible")
    else:
        print(" ".join(map(str, distinct_elements[:3])))

    if len(distinct_elements) < 3:
        print("Not Possible")
    else:
        print(" ".join(map(str, distinct_elements[-3:])))


