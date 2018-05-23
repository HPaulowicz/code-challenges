def DNA_strand(dna):
    # code here
    complements = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    string = ''
    for i in dna:
        string += complements[i]
    return string
    
Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")
