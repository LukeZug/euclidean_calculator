def tests(fn):
    print('Starting tests...')
    num = 0

    # dictionary of values we need to test
    # key is tuple of number a and b
    # value is expected hcf,lcm (respectively) between these two a and b nums
    values_to_test = {
        # symbolab got these :)
        # add to this dict as needed for more proof of bugfreeness
        (72,56):(8,504),
        (1701,3768):(3,2136456),
        (24,60):(12,120),
        (32,99):(1,3168),
        (32,44):(4,352)
    }

    for key, value in values_to_test.items():
        num+=1
        euclidean = fn(key[0], key[1])
        assert len(euclidean) == 2
        assert type(euclidean) == tuple
        assert type(euclidean[0]) == int and type(euclidean[1]) == int
        assert euclidean[0] == value[0] and euclidean[1] == value[1] # make sure the numbers are correct
        print(f'Passed test {num}')
    print('All tests passed.')