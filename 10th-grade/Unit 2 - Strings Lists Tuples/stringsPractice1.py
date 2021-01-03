'''
Kesar Sampat 
Period 3 HCP
Unit 2- Strings, Lists, Tuples
Practice with Lists
'''

#define lists
line = ['To','be','or', 'not', 'to' ,'be']
cereal = ["Snap", "Crackle", "Pop"]
nums = [34,56,78,22,4]

#printing lists
print(line) #regular print outputs with []
print(" ".join(cereal))    #output with no [], separated by spaces 

nums.sort()      #sorts, then outputs 
print(nums)

print("Sum:" , sum(nums))
print("Max:" , max(nums))
print("Min:" , min(nums))