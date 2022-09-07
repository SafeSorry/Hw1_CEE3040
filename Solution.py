import math
import itertools
# 1. (10 pts) A hiring team has conducted interviews with 4 candidates and are now tasked with ranking the
# candidates. How many possible ways could they rank these candidates? Show all possible rankings using
# R/Python.

#Find the number of permutations, this will represent the number of ways they can rank the candidates
print(f"The team can rank the candidates in {math.factorial(4)} ways")

print(f"Here are the possible rankings the candidates can be organized in:")

for k in itertools.permutations([1,2,3,4]):
    print(k)

        

# 2. (10 pts) It is getting cold in Ithaca and you have found your winter jacket from the depths of your closet. While
# checking your jacket’s pockets, you find that there are some coins in one of them. You see that you have a
# penny, nickel, dime, quarter, loonie ($1 coin), and a toonie ($2 coin) (because you are Canadian). If you were
# to put these coins back in your pocket and draw 3 at a time, how many different monetary sums are possible?
# (For ex: draw a loonie, toonie, and a penny = $3.01) Use code to show your numerical solution.


#order does not matter for calculating the sum of 3 coins, so use combinations to calculate the different possible
#monetary sums
coin_combinations = (math.factorial(6))/(math.factorial(3)*math.factorial(3))
print(f"The number of different monetary sums is {int(coin_combinations)}.")





# 3. (10 pts) How many ways can the word TOPICAL be arranged such that all the vowels are together? Use code
# to calculate your solution.

letters = ['T','O','P','I','C','A','L']

topical_permutations = itertools.permutations(letters)
num_vowels = 0 #number of arrangements with the vowels together

for spell in topical_permutations:
    x = itertools.permutations(['I','A','O'])
    for vowels in x:
        if ''.join(vowels) in ''.join(spell):
            num_vowels += 1

print(f"The number of arrangements with vowels together is {num_vowels}")
        
        



# 4. (10 pts) Suppose you are planning a very cool block party with some of your house mates. You have 12 friends
# but you can only invite 7 of them. How many times will 3 particular friends always attend if you happen to
# invite them? Use code to support your numerical solution.

#To designate and select friends, I will treat them as a list of 12 integers, where each integer is a friend 
#and 7 must be selected to be "invited"

friends = list(range(1,13))

#I will then find all possible invite lists with permutations  of this list
#if we treat the select friends as the first three, we can find how many times
#they attend by seeing how many times they appear throughout  
#the following code performs that calculation



# friend_perm = list(itertools.permutations(friends,7))
friend_perm = itertools.combinations(friends,7)
time_attending = 0
num_perms = 0
for perms in friend_perm:

    if (1 and 2 and 3 in perms):
        #integers 1, 2, and 3 serve as the three chosen friends
        time_attending += 1
    

print(f"The number of times those friends will attend is {time_attending}.")
