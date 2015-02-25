states = { 
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA' ,
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = { 
	'CA' : 'San Francisco',
	'MI': 'Detroit',
	 'FL': 'Jacksonvile'
}

cities['NY'] = 'NEW York'
cities['OR'] = 'Portland'

#print out some cities
print '_' * 50
print "NY State has: ",cities['NY']
print "OR State has: ",cities['OR']

#print some states
print '_' * 50
print "Michigan's abbreviation is :",states['Michigan']
print "Florida has abbreviation is: ",states['Florida']

#do it byu using the state then citis dict

print '_' * 50
print "Michigan's has: " ,cities[states['Michigan']]
print "Florida has: ",cities[states['Florida']]

#print every state abbreviation

print '_' * 50
for state ,abbrev in cities.items():
	print "%s is abbreviated %s " % (state,abbrev)

#print every city 
print '_' * 50
for state,abbrev in states.items():
	print "%s state is abbreviated %s and has city %s " %(state ,abbrev,cities[abbrev])

print '_' * 50
#safely get an abbreviation buy state that might not be there
state = states.get('Texas',None)

if not state:
	print "Sorry ,no Texas."

#get a city with a default value
city = cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is: ", city


city = cities.get('NY') ;

print "the citt CY is : " ,city
