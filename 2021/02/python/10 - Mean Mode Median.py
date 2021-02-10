#Python code to calculate mean, median, and mode.
#code can be refactored to reduce time complexity

def Mode(sample):
	mode = []
	freq = {}
	#counting the frequency of each value in the sample
	for x in sample:
	    if x not in freq.keys():
	        freq[x] = sample.count(x)
	maxFV = max(freq.values())

	#checking if max frequency is 1 or more
	if maxFV > 1:
		#listing all the values with same frequency
		for key in freq:
		    if freq[key] == maxFV:
	            mode.append(key)
	else:
	    mode = sample

	return mode


def Median(sample):
	if (len(sample)%2 == 0):
    	median = (sample[int(len(sample)/2)-1] + sample[int(len(sample)/2)])/2
	else:
    	median = sample[int(len(sample)/2)]
    return median


#driver function
sample = list(map(int,input().strip().split()))
sample.sort()
mean   = sum(sample)/len(sample)
median = Median(sample)
mode   = Mode(sample)

print(f'Mean:   {round(mean,2)}')
print(f'Median: {round(median,2)}')
print(f'Mode:   {mode}')