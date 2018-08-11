import sample1 as s

def testsoln25(l):
    return len([x for x in l if x >= 1 and x <= 100]) == len(l)

def testsoln26(l):
    return len([x for x in l if x >= 1 and x <= 20]) == len(l)

def testsoln27(l):
    ls = []
    for x in l:
        if x not in ls and x >= 1 and x <= 20:
            ls.append(x)
    return ls == l

def testsoln28(l):
    ls = []
    for x in l:
        if x >= len(ls)*10 + 1 and x <= 10 * (len(ls)+1):
            ls.append(x)
    return ls == l


assert(s.soln1(10,20) == (20,10))
assert(s.soln2(5))
assert(s.soln3(1,10,2) == [2,4,6,8,10])
assert(s.soln4(2,5) == (0,2))
assert(s.soln5(1,5) == [2,4])
assert(s.soln6(25) == 7)
assert(s.soln7(21) == 3)
assert(s.soln8(2) == 246)
assert(s.soln9(123) == 321)
assert(s.soln10([1,2,3,4,5]) == 3)
assert(s.soln11(12345) == 5)

assert(s.soln12(12321))
assert(not s.soln12(123))

assert(s.soln13('hello','l') == 2)
assert(s.soln14('hello','l') != -1)
assert(s.soln15('hello'))
assert(s.soln16('hello this is sois','s','$') == 'hello thi$ i$ $oi$')
assert(s.soln17('hello') == 2)
assert(s.soln18('Hello this is sois') == 'Hello-this-is-sois')
assert(s.soln19('hello') == 5)

assert(s.soln20('hello','hi') == False)
assert(s.soln20('hello','hi hello') == True)
assert(s.soln21('heLLo') == (2,3))
assert(s.soln22('hello123') == (5,3))
assert(s.soln23('apple app is good','app'))
assert(s.soln24([1,2,3,4,5]) == [1,3,6,10,15])
assert(testsoln25(s.soln25()))
assert(testsoln26(s.soln26()))
assert(testsoln27(s.soln27()))
assert(testsoln28(s.soln28()))