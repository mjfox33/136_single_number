import code_136_single_number as c

def test_example_1():
    s = c.Solution()
    assert s.singleNumber([2,2,1]) == 1

def test_example_2():
    s = c.Solution()
    assert s.singleNumber([4,1,2,1,2]) == 4

def test_example_3():
    s = c.Solution()
    assert s.singleNumber([1]) == 1