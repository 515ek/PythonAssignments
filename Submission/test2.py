import sample2 as s

assert(s.soln01([1,2,3,4,5]) == 5)#max element of list
assert(s.soln02([1,2,3,4,5]) == 4)#max but one element of list
assert(s.soln03([1,2,3,4,5]) == ([1,3,5],[2,4]))# 2 lists with odd and even elements respectively
assert(s.soln04([1,2,3],[1,2,3])) # True if both lists are same
assert(s.soln05([1,2,3,4],[2,3,4,5]) == [1,2,3,4,2,3,4,5]) # union of list with repitition
assert(s.soln06([1,2,3,4],[2,3,4,5]) == [2,3,4]) # intersection of list with repitition
assert(s.soln07([1,2,3,4],[2,3,4,5]) == ([1,2,3,4,5],[2,3,4])) # union and intersection without repitition
# return list with tuples of (x,x*x)
assert(s.soln08([1,2,3]) == [(1,1),(2,4),(3,9)])
# returns list with no repititions
assert(s.soln09([1,2,3,4,2]) == [1,2,3,4])
# returns length of longest word in list
assert(s.soln10(['a','abc','abcd','abcd']) == 4)
# adds key, val to dictionary given
assert(s.soln11(1,2,{}) == {1:2})
# concatenate two dictionaries
assert(s.soln12({1:2},{3:4}) == {1:2,3:4})
# check for key in dictionary returns False if not present
assert(s.soln13(1,{1:2,3:4,5:6}))
# returns dictionary with {x:x*x} 
assert(s.soln14(3) == {1:1,2:4,3:9})
# sum of all values in dictionary
assert(s.soln15({1:2,3:4}) == 6 )
# product of all values in dictionary
assert(s.soln16({1:2,3:4}) == 8)
# removes the key in dictionary returns False if key not present
assert(s.soln17({1:2,3:4,5:6},1) == 2 )
# checks for empty dictionary
assert(s.soln18({}))
# create dictionary with key, values list
assert(s.soln19([(1,2),(3,4),(5,6)]) == {1:2,3:4,5:6})
# returns encrypted msg
assert(s.soln20('cat') == 'km ')
#21
assert(s.soln21('asdfghjkl'))
#22
assert(s.soln22({'stu1':{'s1':81, 's2':78, 's3':89, 's4':75, 's5':86}, 'stu2':{'s1':84, 's2':48, 's3':79, 's4':65, 's5':76}, 'stu3':{'s1':91, 's2':88, 's3':79, 's4':85, 's5':66}}) == {'stu1':{'s1':(81,'A'), 's2':(78,'B'), 's3':(89,'A'), 's4':(75,'B'), 's5':(86,'A')}, 'stu2':{'s1':(84,'A'), 's2':(48,'F'), 's3':(79,'B'), 's4':(65,'C'), 's5':(76,'B')}, 'stu3':{'s1':(91,'A+'), 's2':(88,'A'), 's3':(79,'B'), 's4':(85,'A'), 's5':(66,'C')}})