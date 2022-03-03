#Given an array of sorted integers and a number k. Check if there is a pair of integers in the array that sums to K.
#Return true or False. Also mention the Time and Space complexity of your problem
#Interview time: 10-15mins
#Follow up: Return a pair of the indices instead of just existence

def two_sum_sorted(nums,k):
    i=0
    j=(len(nums))-1

    for _ in range(len(nums)-1):
        sum=nums[i]+nums[j]
        if(sum==k):
            return (True,i,j)
        elif(sum>k):
            j=j-1
        else:
            i=i+1
    return False


print(two_sum_sorted([1,2,3,4,5],5))




