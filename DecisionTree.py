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
	filedata = filedata.replace('(', 'h,  ')
	filedata = filedata.replace(')', ', ')

	with open('dt-data.txt', 'w') as f:
		f.write(filedata)

	#load txt file into a ndarray
	data = np.loadtxt('dt-data.txt', dtype='string', delimiter=', ', usecols=(1,2,3,4,5,6,7))
	#classification column
	targetClass = data[:,6]			
 
    # Create Tuples of (feature, classification)
    # occupiedTup = zip(data[:, 0], targetClass)
    # priceTup = zip(data[:, 1], targetClass)
    # musicTup = zip(data[:, 2], targetClass)
    # locationTup = zip(data[:, 3], targetClass)
    # vipTup = zip(data[:, 4], targetClass)
    # beerTup = zip(data[:, 5], targetClass)

    attrs = data[:, 0:7]
    # print attrs.T
    # print targetClass
    result = buildTree(attrs,targetClass)
    print result

# =============Method Definitions===========================
def buildTree(attrs, target):

	if (len(set(target)) == 1) or (len(target) == 0):
		return target

	gain = []
	print "original data", attrs
	for attr in attrs.T:
		if attr[0] == 'Enjoy':
			continue
		gain.append(informationGain(target, attr))
	print "gain", gain

	if np.all(gain < 1e-6):
		return target

	selected_attr_index = np.argmax(gain)
	print "selected attr", selected_attr_index

	indices = partitionSet(attrs, selected_attr_index)
	print "indices of partition", indices

	temp_attrs = []
	result = []
  	for index in indices:
  		print "index", index
  		temp = attrs[index]
  		print "rows with that index", temp
  		temp_attrs_final = np.delete(temp, selected_attr_index, axis=1)
  		print "after deletion", temp_attrs_final
  		attrs_subset = temp_attrs_final[:, 0:temp_attrs_final.shape[1]]
   		target_subset = temp_attrs_final[:, temp_attrs_final.shape[1]-1]
   		# result.append(temp_attrs_final[0, selected_attr_index])
   		print "attrs_subset", attrs_subset
   		print 'target_subset', target_subset
   		buildTree(attrs_subset, target_subset)
  		# temp_attrs.append(temp_attrs_final)

  	print "final for next iteration", temp_attrs
  	# for arr in temp_attrs:
  	# 	print "arr", arr
   # 		attrs_subset = arr[:, 0:arr.shape[1]]
   # 		target_subset = arr[:, arr.shape[1]-1]
   # 		result.append(arr[0, selected_attr_index])
   # 		print "attrs_subset", attrs_subset
   # 		print 'target_subset', target_subset
   # 		buildTree(attrs_subset, target_subset)

   	return result.append(attrs[0,selected_attr_index])
	
def partitionSet(table, colIndex):
	#select the specified colum
	selectedCol = table[:, colIndex]
	#Count the number of unique occurances and return an array of indices
	dic = {}
	listOfIndices = []
	for i in range(len(selectedCol)):
		val = selectedCol[i]
		if val not in dic:
			if i != 0:
				dic[val] = [i]
		else:
			dic[val].append(i)
	for key in dic:

		modified = dic[key]
		modified.insert(0,0)
		listOfIndices.append(modified)
	return listOfIndices

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

def informationGain(target, attr):
	#Ignore the first row i = 0 as this is attribute names
	s = target.tolist()
	del s[0]
	att = attr.tolist()
	del att[0]

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
