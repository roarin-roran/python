# leetcode challenge attempt:
# https://leetcode.com/problems/container-with-most-water/
#
# personal goals:
# 1. refamiliarise self with python
# 2. demonstrate basic python & algorithmic skills
# 3. upload successfully to git

#input list - the vertical lines to be tested
input = [1, 8, 6, 2, 5, 4, 8, 3, 7]

#maximum area to the right of this element, if the last element is infinite
maxRHResult = []
for i in range(len(input)):
	maxRHResult.append(input[i]*(len(input)-i-1))

#maximum area to the left of this element, if the first element is infinite
maxLHResult = []
for i in range(len(input)):
	maxLHResult.append(input[i]*i)

#max area found so far
maxArea = 0
#used to monitor the success of efficiency improvements
numComparisons = 0

#outer loop defines the left handed participant
for i in range(len(input)-1):
	#only examine possible right hand walls if this left hand wall is high enough
	if maxRHResult[i] > maxArea:
	#inner loop defines the right handed participant
		for j in range(i+1, len(input)):
			#only examine this combination if the right hand partner is viable
			if(maxLHResult[j] > maxArea):
				#print("("+str(i)+","+str(j)+")")
				numComparisons += 1
				area = min(input[i], input[j])*(j-i)
				if(area > maxArea):
					print(area)
					maxArea = area

print("found max area of "+str(maxArea)+" in "+str(numComparisons)+" comparisons")
