Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 

Output: [1,-1,-1,3,5,6]

def calculate_median(array):
    if length(array)%2!=0:  #calculate median if array length is odd
        return array[length(array)%2] 
    else:                  #calculate median if array length is even
        return array[length(array)%2]+array[length(array)%2 +1]
    


def median_of_nums():
    medians=[]
    i=0
    j=k-1
    while i<j and j<length(nums):
        sub_array=nums[i:j+1]    # subarray from i to j
        sub_array=sort(sub_array)   #sorting the array to get median
        median=calculate_median(sub_array)  # function to calculate median 
        medians.append(median)
        i=i+1
        j=j+1
    return medians    # this will return list of medians


  


        
