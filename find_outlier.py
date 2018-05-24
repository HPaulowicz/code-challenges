#You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

#Examples
#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)

#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)

def find_outlier(integers):
    if len(integers) > 2:
        e = 0
        o = 0
        for i in integers[0:3]:
            if i % 2 == 0:
                e += 1
            else:
                o += 1
        
        if e > o:
            rest = 0
        else:
            rest = 1
            
        for x in integers:
            if x % 2 <> rest:
                return x
            
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 3, 6, 8, 10, 4]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
test.assert_equals(find_outlier([3, 2, 4, 6, 8, 10]), 3)
