var dt = require('../');

// get dataset
var dataset = dt.Dataset('enjoyed');

// Create tree and fit the model
var tree = new dt.Tree;
var nodes = tree.fit(dataset.train, dataset.features, dataset.target);

console.log('nodes:', JSON.stringify(tree.root, null, 2));