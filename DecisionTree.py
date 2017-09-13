import numpy as np
import collections

# ==============Gloabl Constants==================================
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

	#attributes and examples columns
	examples = data[:, 0:7]
    attributes = data[0, :]

    #classification column
    targetClass = data[:, 6]	

    #global dictionary for decision tree
    global result_counter
    result_counter = {}

    #counter for keeping track of levels of tree
    counter = 0

    # ==============Decision Tree==================================
    #build tree
    buildTree(examples, attributes, targetClass, counter)

	#print tree
    sorted_output = collections.OrderedDict(sorted(result_counter.items()))
    for i in range(len(sorted_output)):
    	output_string = ', '.join(sorted_output[i+1])
    	print output_string

# =============Method Definitions===========================
def buildTree(examples, attributes, target, counter):
	#recurrsion end conditions
	#if classification column has same values or no values
	if (len(set(target)) == 2) or (len(target) == 1):
		value = np.delete(target, 0)
		counter += 1
		pushNode(counter, value[0])
		return counter

	# if len(attributes) == 1:
	# 	pushNode(counter, 'Yes')
	# 	return counter

	# if len(examples) == 1:
	# 	pushNode(counter, 'Yes')
	# 	return counter

	#calculate information gains of all examples
	temp_gain = []
	for attr in examples.T:
		if attr[0] == 'Enjoy':
			continue
		temp_gain.append(informationGain(target, attr))
	gain = np.array(temp_gain)

	#get the highest information gain of all gains of examples
	if(len(gain) > 1):
		selected_attr_index = np.argmax(gain[0: len(gain)-1])
	else: #if there is tie between Yes or No in the last remaining attribute
		counter += 1
		pushNode(counter, 'Tie')
		return

	#add the selected node in decision tree
	node = attributes[selected_attr_index]
	counter += 1
	pushNode(counter, node)

	#get the examples indices for selected attribute
	indices = partitionSet(examples, selected_attr_index)

	#recurrsion begins
	temp_counter = counter + 1
	for i in range(len(attValDic[node])):
		#iterate over all the values of an attribute
		v_i = attValDic[node][i]
		#if no data present for the value
		if v_i not in indices.keys():
			if temp_counter == None:
				temp_counter = counter + 1
			pushNode(temp_counter, 'Yes')
		else: 
			#get data for the value
			index = indices[v_i]
			temp = examples[index]

			#delete the column of selected attribute from the data
			temp_examples_final = np.delete(temp, selected_attr_index, axis=1)
			#delete the column of selected attribute from the attributes array
 			attributes_copy = np.delete(attributes, selected_attr_index)
 			#separate examples and classification column from data
 			examples_subset = temp_examples_final[:, 0:temp_examples_final.shape[1]]
	   		target_subset = temp_examples_final[:, temp_examples_final.shape[1]-1]

	   		#build sub-tree
	   		temp_counter = buildTree(examples_subset, attributes_copy, target_subset, counter)
   	return

def pushNode(level, node):
	if (level) not in result_counter:
		result_counter[(level)] = [node]
	else:
		result_counter[(level)].append(node)

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
