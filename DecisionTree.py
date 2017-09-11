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
    data = np.loadtxt('dt-data.txt', dtype='string', comments='(', delimiter=', ', usecols=(1, 2))
    # classification column
    targetClass = data[:, 1]

    # Create Tuples of (feature, classification)
    # occupiedTup = zip(data[:, 0], targetClass)
    # priceTup = zip(data[:, 1], targetClass)
    # musicTup = zip(data[:, 2], targetClass)
    # locationTup = zip(data[:, 3], targetClass)
    # vipTup = zip(data[:, 4], targetClass)
    # beerTup = zip(data[:, 5], targetClass)

    attrs = data[:, 0:2]
    print attrs
    print targetClass
    buildTree(attrs,targetClass)


# =============Method Definitions===========================
def buildTree(attrs, target):
    gain = []
    for attr in attrs.T:
       gain.append(informationGain(target, attr))
       print gain
    selected_attr_index = np.argmax(gain)

    print selected_attr_index

    selected_attr_values, counts= np.unique(attrs[:,selected_attr_index], return_counts=True)
    attrs_subset = []
    for attr in attrs.T
    	if(attr==selected_attr_values[i])
    		attrs_subset.append(attrs[:,i])

    print selected_attr_values
    print counts
    print attrs_subset

    # buildTree(attrs_subset, target_subset)

def entropy(s):
    res = 0
    val, counts = np.unique(s, return_counts=True)
    freqs = counts.astype('float') / len(s)
    for p in freqs:
        if p != 0.0:
            res -= p * np.log2(p)
    return res


def informationGain(x, y):
    res = entropy(y)

    # We partition x, according to attribute values x_i
    val, counts = np.unique(x, return_counts=True)
    freqs = counts.astype('float') / len(x)

    # We calculate a weighted average of the entropy
    for p, v in zip(freqs, val):
        res -= p * entropy(y[x == v])

    return res


if __name__ == "__main__":
    main()
