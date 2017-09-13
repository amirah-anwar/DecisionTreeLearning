import numpy as np
from pprint import pprint
# ==============Gloabl Vars==================================
attValDic = {'Occupied': ['High', 'Moderate', 'Low'], 'Price': ['Expensive', 'Normal', 'Cheap'], 
'Music': ['Loud', 'Quiet'], 'Location': ['Talpiot', 'City-Center', 'German-Colony', 'Ein-Karem','Mahane-Yehuda'],
'VIP': ['Yes', 'No'], 'Favorite Beer': ['Yes', 'No']};

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
	filedata = filedata.replace('(', 'h, ')
	filedata = filedata.replace(')', ', ')

	with open('dt-data.txt', 'w') as f:
		f.write(filedata)

	#load txt file into a ndarray
	data = np.loadtxt('dt-data.txt', dtype='string', delimiter=', ', usecols=(1,2,3,4,5,6,7))

	#classification columns
	examples = data[:, 0:7]
    attributes = data[0, :]
    targetClass = data[:, 6]	

    # print "examples", examples
    # print "attributes", attributes
    # print "targetClass", targetClass		
    global result
    global result_stack
    global big_results

    result = {}
    result_stack = []
    big_results = []
    result = buildTree(examples, attributes, targetClass)
    pprint(result_stack)

# =============Method Definitions===========================
def buildTree(examples, attributes, target):

	global result
	# print "original data", examples
	# if np.all(target == 'Yes'):
	# 	result_stack.append('Yes')
	# 	createPath(result_stack)
	# 	result_stack.pop()
	# 	return 'Yes'
	# if np.all(target == 'No'):
	# 	result_stack.append('No')
	# 	createPath(result_stack)
	# 	result_stack.pop()
	# 	return 'No'
	# if len(attributes) == 0:
	# 	value = np.delete(target, 0)
	# 	result_stack.append(set(value))
	# 	createPath(result_stack)
	# 	result_stack.pop()
	# 	return node
	if (len(set(target)) == 2) or (len(target) == 1):
		value = np.delete(target, 0)
		result_stack.append(set(value))
		createPath(result_stack)
		result_stack.pop()
		return value

	temp_gain = []
	for attr in examples.T:
		if attr[0] == 'Enjoy':
			continue
		temp_gain.append(informationGain(target, attr))
	gain = np.array(temp_gain)
	# print "gain", gain

	# if np.all(gain == 0):
	# 	value = np.delete(target, 0)
	# 	result_stack.append(set(value))
	# 	createPath(result_stack)
	# 	result_stack.pop()
	# 	return np.delete(target, 0)

	selected_attr_index = np.argmax(gain)
	# print "selected attribute", selected_attr_index

	node = attributes[selected_attr_index]
	result_stack.append(node)

	indices = partitionSet(examples, selected_attr_index)
	# print "indices of partition", indices

	if set(indices.keys()) != attValDic[node]:
		result_stack.append('Yes')
		createPath(result_stack)
		result_stack.pop()


	temp_examples = []
  	for key, index in indices.items():
   		if key not in attValDic[node]:
   			createPath(result_stack)
   			# print result
   		else:
   			# print "index", index
   			# print "examples", examples
   			
   			temp = examples[index]
   			# print "rows with that index", temp
   			
   			temp_examples_final = np.delete(temp, selected_attr_index, axis=1)
   			attributes = np.delete(attributes, selected_attr_index)
   			# print "after deletion temp_examples_final", temp_examples_final
   			# print "after deletion attributes", attributes

	  		examples_subset = temp_examples_final[:, 0:temp_examples_final.shape[1]]
	   		target_subset = temp_examples_final[:, temp_examples_final.shape[1]-1]
	   		# print "examples_subset", examples_subset
	   		# print 'target_subset', target_subset
   			print "node", node
   			print "key", key
   			result["%s = %s" % (node, key)] = buildTree(examples_subset, attributes, target_subset)
   			result_stack.pop()
   			print result

   	return result

def createPath(list):
	temp = list
	output = []
	for item in temp:
		output.append(item)
	big_results.append(output)	

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
		dic[key] = modified
	return dic

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
