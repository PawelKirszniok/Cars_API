# Books_API


## Table of contents

* .[About](#about)
* .[Documentation](#documentation)


## About

a simple API allowing users to save cars to the database and then later retrieve them


## Documentation:

the API contains three endpoints with the following functionality :

#### POST /api/car

creates a new car resource given a payload matching this syntax:
~~~
{
"make": "Mercedes",
"color": "#FF0000",	# this also handles other CSS compatible colors such as "red" or (255, 255, 255) and converts them to a hex format
"production_year": 2019,   
"avg_fuel_consumption_per_100km": 8.5.
"max_passengers": 5,
}
~~~

#### GET /api/car

returns a list of all car objects from the database

#### GET /api/car/{car_id}

takes an integer and returns the car matching the provided id 