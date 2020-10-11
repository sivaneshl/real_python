import timeit
import search.random as rdm
import search.linear as lin
import search.binary_iterative as ibin
import search.binary_recursive as rbin

fruits = ['orange', 'plum', 'banana', 'watermelon', 'apple']

# Random Search
print('Random Search')
print(rdm.contains(fruits, 'banana'))
print(rdm.find_index(fruits, 'banana'))
print(rdm.find(fruits, 'banana'))
print(rdm.find(fruits, key=len, value=10))
print(timeit.timeit(lambda: rdm.contains(fruits, 'missing')))

# Linear Search
print('Linear Search')
print(lin.contains(fruits, 'banana'))
print(lin.find_index(fruits, 'banana'))
print(lin.find(fruits, 'banana'))
print(lin.find(fruits, key=len, value=10))
print(timeit.timeit(lambda: lin.contains(fruits, 'missing')))

# Hash based Search
print('Hash-based Search')
index_by_name = {
    name: index for index, name in enumerate(fruits)
}
print('banana' in index_by_name)
print(index_by_name['banana'])
print(timeit.timeit(lambda: 'missing' in index_by_name))

# Binary Search - Iterative
print('Binary Search - Iterative')
fruits_sorted = sorted(fruits)
print(ibin.contains(fruits_sorted, 'banana'))
print(ibin.find_index(fruits_sorted, 'banana'))
print(ibin.find(fruits_sorted, 'banana'))
print(ibin.find(fruits_sorted, key=len, value=10))
print(timeit.timeit(lambda: ibin.contains(fruits_sorted, 'missing')))

# Binary Search - Iterative - with duplicates
print('Binary Search - Iterative - with duplicates')
fruits_duplicate = ['orange', 'banana', 'plum', 'banana', 'watermelon', 'banana', 'apple']
fruits_duplicate = sorted(fruits_duplicate)
print(ibin.find_leftmost_index(fruits_duplicate, 'banana'))
print(ibin.find_rightmost_index(fruits_duplicate, 'banana'))
print(ibin.find_all_indices(fruits_duplicate, 'banana'))

# Binary Search - Recursive
print('Binary Search - Recursive')
print(rbin.contains(fruits_sorted, 'banana'))
print(rbin.find_index(fruits_sorted, 'banana'))
print(rbin.find(fruits_sorted, 'banana'))
print(rbin.find(fruits_sorted, key=len, value=10))
print(timeit.timeit(lambda: rbin.contains(fruits_sorted, 'missing')))