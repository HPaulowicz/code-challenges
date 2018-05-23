def Descending_Order(num):
    #Bust a move right here
    result = sorted(str(num), reverse=True)
    return int(''.join(str(i) for i in result))
    
    
test.assert_equals(Descending_Order(0), 0)
test.assert_equals(Descending_Order(15), 51)
test.assert_equals(Descending_Order(123456789), 987654321)
