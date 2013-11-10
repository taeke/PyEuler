def reverse_str(s):
    return s[::-1];

def is_a_prime(prime):
    divider = 2;
    while prime % divider != 0 and prime > divider:
        divider = divider + 1;
    if prime == divider:
        return 1
    else:
        return 0;

def solution_1():
    sum = 0;
    for i in range(1000):  
        if (i % 3 == 0) or (i % 5 == 0):
            sum = sum + i;
    return str(sum);

def solution_2():
    item1 = 1;
    item2 = 2;
    sum = 0;
    total = 0;
    while sum < 4000000:
        sum = item1 + item2;
        if item2 % 2 == 0:
            total = total + item2;
        item1 = item2;
        item2 = sum;
    return str(total);

def solution_3():
    count = 1;
    found = 0;
    max = 600851475143;

    while not found == 1:
        count = count + 1;
        if max % count == 0:
            divider = max // count;
            if max % divider == 0:
                found = is_a_prime(divider);
    return str(max // count);
 
def solution_4():
    palindroomHalf = 1000;
    palindroom = 999999;
    divider = 1000;
    found = 0;

    while not found == 1:
        divider = 1000;
        palindroomHalf = palindroomHalf - 1;
        palindroom = int(str(palindroomHalf) + reverse_str(str(palindroomHalf)));
        while not found == 1 and palindroom / divider < 999 :
            divider = divider -1;
            if palindroom % divider == 0:
                found = 1;
    return str(divider) + " en " + str(palindroom / divider) + " en " + str(palindroom);

def solution_5():
    multiplier = 0;
    found = 0;

    while not found == 1:
        multiplier = multiplier + 1;
        divider = 19;
        found = 1;
        while found == 1 and divider > 1 :
            if (multiplier * 20) % divider == 0 :
                found = 1
            else:
                found = 0;
            divider = divider - 1;
    return str(multiplier * 20);

def initialize_problems():
    problems = [];
    problems.append((1, 'Multiples of 3 and 5', solution_1));
    problems.append((2, 'Even Fibonacci numbers', solution_2));
    problems.append((3, 'Largest prime factor', solution_3));
    problems.append((4, 'Largest palindrome product', solution_4));
    problems.append((5, 'Smallest multiple', solution_5));
    problems.append((6, 'Sum square difference', None));
    problems.append((7, '10001st prime', None));
    problems.append((8, 'Largest product in a series', None));
    problems.append((9, 'Special Pythagorean triplet', None));
    problems.append((10, 'Summation of primes', None));
    return problems;

def show_solutions():
    NO_SOLUTION_MSG = 'Found no solution (yet) for problem number ';
    SOLUTION_MSG = 'The solution for problem number ';

    problems = initialize_problems();

    for problem in problems:
        if problem[2] == None:
            print(NO_SOLUTION_MSG + str(problem[0]) + ' : "' + problem[1] + '"')
        else:
            print(SOLUTION_MSG + str(problem[0]) + ' : "' + problem[1] + '" is ' + problem[2]());

show_solutions();
