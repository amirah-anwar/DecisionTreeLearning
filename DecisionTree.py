import numpy as np


# Calculate Entropy of entire data
# Calculate Entropy of each subset within an attribute
# Calculate Information gain of each level or attribute

def main():
    # ==============Process Data==================================
    # Get rid of the first column, may not be needed
    with open('dt-data.txt', 'r') as f:
        filedata = f.read()
    filedata = filedata.replace(':', ',')
    filedata = filedata.replace(';', ', ')

    with open('dt-data.txt', 'w') as f:
        f.write(filedata)

    # load txt file into a ndarray
    temp_data = np.loadtxt('dt-data.txt', dtype='string', comments='(', delimiter=', ', usecols=(1, 2, 3))
    data = np.insert(temp_data, 0, ['Occupied', 'VIP', 'Enjoy'], axis=0)
    print data
    # classification column
    targetClass = data[:, 2]
 
    # Create Tuples of (feature, classification)
    # occupiedTup = zip(data[:, 0], targetClass)
    # priceTup = zip(data[:, 1], targetClass)
    # musicTup = zip(data[:, 2], targetClass)
    # locationTup = zip(data[:, 3], targetClass)
    # vipTup = zip(data[:, 4], targetClass)
    # beerTup = zip(data[:, 5], targetClass)

    attrs = data[:, 0:2]
    print attrs.T
    print targetClass
    result = buildTree(attrs,targetClass)
    print result

# =============Method Definitions===========================
def buildTree(attrs, target):

	if len(set(target)) == 1 or len(target) == 0:
        return target

    gain = []
    for attr in attrs.T:
       gain.append(informationGain(target, attr))
       print gain

    selected_attr_index = np.argmax(gain)

    print selected_attr_index

    indices = partitonSet(attrs, selected_attr_index)
    temp_attrs = []

  	for index in indices:
  		temp = attrs.take(index)
  		temp_attrs_final = np.delete(temp, selected_attr_index, axis=1)
  		temp_attrs.append(temp_attrs_final)

  	for arr in temp_attrs
   		attrs_subset = arr[:, 0:len(arr)-1]
   		target_subset = arr[:, len(arr)-1]
   		result.append(arr[0,selected_attr_index])
   		print attrs_subset
    	print target_subset
   		buildTree(attrs_subset, target_subset)

    return result.append(attrs[0,selected_attr_index])

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
