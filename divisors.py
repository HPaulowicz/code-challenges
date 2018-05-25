#Create a function named divisors/Divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

#Example:
#divisors(12); #should return [2,3,4,6]
#divisors(25); #should return [5]
#divisors(13); #should return "13 is prime"
#You can assume that you will only get positive integers as inputs.

import math

def divisors(n):
    result = []
    sqr = int(math.sqrt(n)) + 1
    print(sqr)
    for i in range(2, sqr, 1):
        print(i)
        if n % i == 0:
            result.extend([int(i), int(n/i)])
    if len(result) == 0:
        return("{} is prime".format(n))
    result.sort(key=int)
    return result
    
Test.assert_equals(divisors(15), [3, 5]);
Test.assert_equals(divisors(12), [2, 3, 4, 6]);
Test.assert_equals(divisors(13), "13 is prime");
