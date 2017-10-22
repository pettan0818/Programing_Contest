def read_input():
    l_1 = input()
    day = int(l_1.split(" ")[0])

    num_cake = [int(i) for i in input().split(" ")]

    return day, num_cake


def get_max_index(target_list):
    res = []
    max_target = max(target_list)
    res.append(target_list.index(max_target))
    target_list = target_list.remove(max_target)
    try:
        res.append(target_list.index(max_target))
    except AttributeError:
        return res

    return res
    # return [i for i, j in enumerate(target_list) if j == max(target_list)]


def get_second_max_index(target_list):
    return [i for i, j in enumerate(target_list) if j == list(sorted(set(target_list), reverse=True))[1]]


def mog(day, num_cake):
    """

    >>> mog(7, [3,2,2])
    0
    >>> mog(6, [1,4,1])
    1
    >>> mog(100, [100])
    99
    """
    printed = False
    previous_index = -1

    for i in range(0, day):
        ate_flag = False
        mog_maybe_index = get_max_index(num_cake)

        for n in mog_maybe_index:
            if n == previous_index:
                continue
            else:
                num_cake[n] = num_cake[n] - 1
                ate_flag = True
                previous_index = n
                break

        if ate_flag is False:
            try:
                mog_ext = get_second_max_index(num_cake)
                mogmog = mog_ext[0]
                if num_cake[mogmog] == 0:
                    printed = True
                    print(max(num_cake))

                    break
            except IndexError:
                print(max(num_cake))
                printed = True
                break

            num_cake[mogmog] = num_cake[mogmog] - 1
            previous_index = mogmog

    if printed is False:
        print(0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # day, num_cake = read_input()
    # mog(day, num_cake)
