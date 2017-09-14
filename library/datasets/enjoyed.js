module.exports = {

  target: 'Enjoy',

  features: ['Occupied', 'Price', 'Music', 'Location', 'VIP', 'Favorite_Beer'],

  train: [
		{Occupied: 'High', Price: 'Expensive', Music: 'Loud', Location: 'Talpiot', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'No'},
		{Occupied: 'High', Price: 'Expensive', Music: 'Loud', Location: 'City-Center', VIP: 'Yes', Favorite_Beer: 'No', Enjoy: 'Yes'},
		{Occupied: 'Moderate', Price: 'Normal', Music: 'Quiet', Location: 'City-Center', VIP: 'No', Favorite_Beer: 'Yes', Enjoy: 'Yes'},
		{Occupied: 'Moderate', Price: 'Expensive', Music: 'Quiet', Location: 'German-Colony', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'No'},
		{Occupied: 'Moderate', Price: 'Expensive', Music: 'Quiet', Location: 'German-Colony', VIP: 'Yes', Favorite_Beer: 'Yes', Enjoy: 'Yes'},
		{Occupied: 'Moderate', Price: 'Normal', Music: 'Quiet', Location: 'Ein-Karem', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'Yes'},
		{Occupied: 'Low', Price: 'Normal', Music: 'Quiet', Location: 'Ein-Karem', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'No'},
		{Occupied: 'Moderate', Price: 'Cheap', Music: 'Loud', Location: 'Mahane-Yehuda', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'Yes'},
		{Occupied: 'High', Price: 'Expensive', Music: 'Loud', Location: 'City-Center', VIP: 'Yes', Favorite_Beer: 'Yes', Enjoy: 'Yes'},
		{Occupied: 'Low', Price: 'Cheap', Music: 'Quiet', Location: 'City-Center', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'No'},
		{Occupied: 'Moderate', Price: 'Cheap', Music: 'Loud', Location: 'Talpiot', VIP: 'No', Favorite_Beer: 'Yes', Enjoy: 'No'},
		{Occupied: 'Low', Price: 'Cheap', Music: 'Quiet', Location: 'Talpiot', VIP: 'Yes', Favorite_Beer: 'Yes', Enjoy: 'No'},
		{Occupied: 'Moderate', Price: 'Expensive', Music: 'Quiet', Location: 'Mahane-Yehuda', VIP: 'No', Favorite_Beer: 'Yes', Enjoy: 'Yes'},
		{Occupied: 'High', Price: 'Normal', Music: 'Loud', Location: 'Mahane-Yehuda', VIP: 'Yes', Favorite_Beer: 'Yes', Enjoy: 'Yes'},
		{Occupied: 'Moderate', Price: 'Normal', Music: 'Loud', Location: 'Ein-Karem', VIP: 'No', Favorite_Beer: 'Yes', Enjoy: 'Yes'},
		{Occupied: 'High', Price: 'Normal', Music: 'Quiet', Location: 'German-Colony', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'No'},
		{Occupied: 'High', Price: 'Cheap', Music: 'Loud', Location: 'City-Center', VIP: 'No', Favorite_Beer: 'Yes', Enjoy: 'Yes'},
		{Occupied: 'Low', Price: 'Normal', Music: 'Quiet', Location: 'City-Center', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'No'},
		{Occupied: 'Low', Price: 'Expensive', Music: 'Loud', Location: 'Mahane-Yehuda', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'No'},
		{Occupied: 'Moderate', Price: 'Normal', Music: 'Quiet', Location: 'Talpiot', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'Yes'},
		{Occupied: 'Low', Price: 'Normal', Music: 'Quiet', Location: 'City-Center', VIP: 'No', Favorite_Beer: 'No', Enjoy: 'Yes'}
	],

 	predict: [
 		{Occupied: 'Moderate', Price: 'Cheap', Music: 'Loud', Location: 'City-Center', VIP: 'No', Favorite_Beer: 'No'}
 	]
};
