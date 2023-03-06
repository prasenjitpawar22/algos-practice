#1539 problem no
arr = [2, 3, 5, 6, 8, 9, 20]
k = 1
# time complexity O(long n)
# space complexity O(1)

# left right pointer
l, r = 0, len(arr) - 1

while l <= r:
  mid = (l + r) // 2  #mid pointer
  #calcualte the missing values
  # e.g
  #        0 1 2 3 4 5  6
  # arr = [2,3,5,6,8,9,20]    m = (0+6)/2 => 3
  #        l     m      r
  #
  # the missing values at pointer mid can be calucated as
  # formula = (arr[mid] - mid - 1) => 6-3-1 => missing => 2
  # NOTE: missing values from left to mid pointer
  # so now if
  # missing value < k
  #   move the left pointer to mid+1
  #   else move the right pointer to mid-1
  # this tells that the kth value is either left or right of subarray
  missing = arr[mid] - mid - 1
  # this works because the array does not have any duplicates
  # here in given e.g
  # missing -> 2 is greater then k-> 1
  # so will hit the else condition: r = mid-1
  if missing < k:
    l = mid + 1
  else:
    r = mid - 1

print(r + k + 1)

# here's how the second loop iteration will look
#
#        0 1 2 3 4 5  6
#       [2,3,5,6,8,9,20]    m = (0+2)/2 => 1
#        l m r
#
# missing values => arr[m] - m -1 => 3-1-1 => 1
# so in else condition r=> m-1
#
# thrid iteration
#        0 1 2 3 4 5  6
#       [2,3,5,6,8,9,20]    m = (0+1)/2 => 0
#        ^ ^
#      m,l r
#
# missing values => arr[m] - m -1 => 2-0-1 => 1
# so in else condition r=> m-1
#
# fourth iteration
#        0 1 2 3 4 5  6
#       [2,3,5,6,8,9,20]    m = (0+0)/2 => 0
#        ^ 
#      m,l,r
#
# missing values => arr[m]-m-1 => 2-0-1 => 1
# so in else condition r=> m-1
# no fifth iteration as r is now less then l i.e r=-1

# return will be formula2 -> r+k+1
# i.e -1+1+1 => 1
