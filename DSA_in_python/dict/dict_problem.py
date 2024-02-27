def sort_asc_desc():
    arr = [1, 2, 3, 4, 50, -1, 2, 3, 45]
    occ = {}

    for _, val in enumerate(arr):
        if val in occ:
            occ[val] += 1
        else:
            occ[val] = 1

    # sorting by key
    # Todo: fix this
    asc = dict(sorted(occ.items(), key=lambda x: x[0]))
    desc = dict(sorted(occ.items(), key=lambda x: x[0], reverse=True))
    print(asc)
    print(desc)


sort_asc_desc()
