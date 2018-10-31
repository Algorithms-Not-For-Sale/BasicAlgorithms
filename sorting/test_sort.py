import numpy
import sort

nums = numpy.random.randint(100, size=20).tolist()
sortedNums = sorted(nums)

try:
    if(sort.insertsort(nums) == sortedNums):
        print('insertsort success!')
    else:
        print('insertsort incorrect.')
except:
    print('insertsort function error or is incomplete.')