[![Build Status](https://travis-ci.org/Kaytbode/barbershop_api.svg?branch=develop)](https://travis-ci.org/Kaytbode/barbershop_api)
[![Coverage Status](https://coveralls.io/repos/github/Kaytbode/barbershop_api/badge.svg?branch=develop)](https://coveralls.io/github/Kaytbode/barbershop_api)
[![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)
[![Hosted on Heroku](https://img.shields.io/badge/hosted%20on-Heroku-blue.svg)](https://barber-backend.herokuapp.com/)
[![API-DOCS on Swagger](https://img.shields.io/badge/API--DOCS%20on-Swagger-green.svg)](https://app.swaggerhub.com/apis-docs/Kaytbode/Barbershop/1.0.0)  
# Barbershop API
A Graphql API for a haircut services application

## Usage
+ ``` Fork and clone the repo on your local machine ```
+ **``` pip install requirements.txt```** to get all the necessary applications dependencies
+ ``` Create a postgres database to be used with the application ```
+ ``` Register with ipstack for a free API KEY ```
+ ``` Create a .env file, using the .env.sample as a guide ```
+ Start the application running the command ```flask run``` on your terminal

## Examples

### Queries
This query returns the last names of all registered Barbers in the application
```query{
    allBarbers{
      edges{
        node{
          lastName
        }
      }
    }
  }
```
### Mutation
This adds a new user(barber) to the application
```
mutation{
    createBarber(input: {
        email:"abced@yahoo.com",
        firstName: "abc",
        lastName: "xyz",
        password: "12we34r4e",
        confirmPassword: "12we34r4e"
    }){
        barber{
            email,
            firstName,
            lastName
        }
    }
}
```
This confirms if a user(barber) is registered to use the application
```
mutation{
    verifyBarber(input: {
        email:"abced@yahoo.com",
        password: "12we34r4e"
    }){
        barber{
            email,
            firstName,
            lastName,
        }
    }
}
```
This adds a ongoing service to the database
```
mutation{
    createService(input: {
        barberEmail:"abced@yahoo.com",
        customer: "flip burger"
    }){
        service{
            customer,
            status,
            location
        }
    }
}
```
#### Response Format
Response from registering a user
```
{
    "data": {
        "createBarber": {
            "barber": {
                "email": "abced@yahoo.com",
                "firstName": "abc",
                "lastName": "xyz"
            }
        }
    }
}
```
Response from a user confirmation
```
{
    "data": {
        "verifyBarber": {
            "barber": {
                "email": "abced@yahoo.com",
                "firstName": "abc",
                "lastName": "xyz"
            }
        }
    }
}
```
Response from adding a service to the database
```
{
    "data": {
        "createService": {
            "service": {
                "customer": "flip burger",
                "status": "current",
                "location": "4/5 binge lagos, Nigeria"
            }
        }
    }
}
```
Besides the response parameters specified in the examples, You can add more parameters to be returned by your **query** or **mutation**. [Here](https://graphql.org/), for more on graphql.

## Built With
+ [Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/) 
+ [Graphql](https://graphql.org/)
+ [ipstack](https://ipstack.com/quickstart) 
