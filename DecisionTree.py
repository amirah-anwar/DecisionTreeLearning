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

	#Create Tuples of (feature, classification)
	occupiedTup = zip(data[:,0], targetClass)
	priceTup = zip(data[:,1], targetClass);
	musicTup = zip(data[:,2], targetClass);
	locationTup = zip(data[:,3], targetClass);
	vipTup = zip(data[:,4], targetClass);
	beerTup = zip(data[:,5], targetClass);

	print priceTup

#=============Method Definitions===========================
def entropy(s):
	sum = 0;
	uniqueArr, counts = np.unique(s, return_counts=True)
	freq = counts.astype('float')/len(s)

	for p in freq:
		if p != 0.0:
			sum += -p*np.log2(p)
	return sum

def informationGain(s, att):
	entropySet = entropy(s)
	branches, counts = np.unique(att, return_counts=True)
	print branches, counts

if __name__ == "__main__":
    main()