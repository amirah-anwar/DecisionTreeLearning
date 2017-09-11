import numpy as np

#Calculate Entropy of entire data
#Calculate Entropy of each subset within an attribute
#Calculate Information gain of each level or attribute

def main():
#==============Process Data==================================
	#Get rid of the first column, may not be needed
	with open('dt-data.txt', 'r') as f:
		filedata = f.read()
	filedata = filedata.replace(':', ',')
	filedata = filedata.replace(';', ', ')

	with open('dt-data.txt', 'w') as f:
		f.write(filedata)

	#load txt file into a ndarray
	data = np.loadtxt('dt-data.txt', dtype='string', comments='(', delimiter=', ', usecols=(1,2,3,4,5,6,7))
	#classification column
	targetClass = data[:,6]	

	print informationGain(targetClass, data[:,0])
	
#=============Method Definitions===========================
def entropy(currSet, indices):

	sum = 0.0;
	#Get the classification subset based on indices[]
	classSubSet = [currSet[i] for i in indices]
	uniqueArr, counts = np.unique(classSubSet, return_counts=True)
	freq = counts.astype('float')/len(indices)
	#Calculate the entropy of this classification subset
	for p in freq:
		if p != 0.0:
			sum += -p*np.log2(p)
	return sum

def informationGain(s, att):
	oldEntropy = entropy(s, range(len(s)))

	iDic = {}
	newEntropy = 0.0;
	#Set up dicitonary for (val, idicies)
	for i in range(len(att)):
		val = att[i]
		if val not in iDic:
			iDic[val] = [i]
		else:
			iDic[val].append(i)
	#Calculate information gain 
	for key in iDic:
		val = iDic[key]
		p_i = (float(len(val))/float(len(s)))
		newEntropy += p_i*entropy(s, val)
	return oldEntropy - newEntropy

if __name__ == "__main__":
    main()