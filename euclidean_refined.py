## Program to take in 2 integers, calculate the HCF and LCM between them.
import functools, euclidean_tests

def get_primes(num):
    # Calculate primes
    primes = []
    for i in range(2, num+1):
        prime=True
        for x in range(i, 0, -1):
            if (i%x==0) and (x != 1 and x != i):
                # not prime
                prime = False
        if prime:
            primes.append(i)
    return primes

def prime_factors(num):
    # Given integer, find prime factors of it.
    primes = get_primes(num)
    p_factors = []
    for i in range(1, num+1):
        if ((num % i) == 0) and i in primes:
            # is a prime factor
            # now see how many of each factor is present in the product
            # eg keep dividing until it's no longer a whole number
            value = num / i
            while (value == int(value)):
                p_factors.append(i)
                value = value / i
    return p_factors

def hcf_lcm(l1,l2):
    # Calculate the HCF and LCM of two numbers, passed the list of
    # the prime factors of these numbers. HCF can be found by multiplying the 
    # numbers which appeared least. LCM can be found by multiplying those that appeared most.
    elements_dealt_with, hcf_list, lcm_list = [], [], []

    for el in l1:
        if (el in l2) and el not in elements_dealt_with:
            # element appears at least once in the other list.
            appears_in_l2, appears_in_l1 = l2.count(el), l1.count(el)

            # add the element n times to the hcf or lcm list, depending on how many times it appeared
            hcf_list.append(el**appears_in_l2 if appears_in_l2 < appears_in_l1 else el**appears_in_l1)
            lcm_list.append(el**appears_in_l2 if appears_in_l2 > appears_in_l1 else el**appears_in_l1)

        elif (el not in l2):
            # this number is ONLY present in the first list.
            # we know the number is to power 0 then for HCF (as it appears x^0 times in first list) - so 1
            # for lcm we can just use the element value, since we know it only appeared in that list
            hcf_list.append(1)
            lcm_list.append(el)

        # just add the element to (another...) list so as to stop repeats happening
        # due to the way I have stored numbers to nth powers eg 2^3 is [2,2,2]!!!
        elements_dealt_with.append(el)

    # For lcm, Quickly go through the other list and pickup any numbers that weren't in the first list
    lcm_list += [el for el in l2 if el not in elements_dealt_with]

    # multiply all components of each list using reduce function
    hcf_final = functools.reduce(lambda x, y: x * y, hcf_list)
    lcm_final = functools.reduce(lambda x, y: x * y, lcm_list)

    return hcf_final, lcm_final

def euclidean(a,b):
    # First, find prime factors for each number.
    a_pf = prime_factors(a)
    b_pf = prime_factors(b)

    # Calculate the hcf and lcm between a and b (lists of prime factors)
    hcf_num, lcm_num = hcf_lcm(a_pf, b_pf)

    return f'hcf({a},{b}) => {hcf_num}\nlcm({a},{b}) => {lcm_num}'

    # Uncomment line below and comment line above when in testing mode
    #return hcf_num, lcm_num

def search_euclidean():
    print('For hcf(a,b) and lcm(a,b), enter your a, b values:')
    a = input('a: ')
    b = input('b: ')
    return euclidean(int(a),int(b))

print(search_euclidean())

##### TESTS: Uncomment line below to run tests on euclidean function
# and make sure to uncomment required lines in the euclidean function too!
#euclidean_tests.tests(euclidean) 