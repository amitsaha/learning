var graphql = require('graphql');
var graphqlHTTP = require('express-graphql');
var express = require('express');

// Import our data set from above
var data = require('./data.json');

// Define our user type, with two string fields; `id` and `name`
var userType = new graphql.GraphQLObjectType({
    name: 'User',
    fields: {
        id: { type: graphql.GraphQLString },
        name: { type: graphql.GraphQLString },
    }
});

// Define our schema, with one top level field, named `user`, that allows
// querying by name, id or both
var schema = new graphql.GraphQLSchema({
    query: new graphql.GraphQLObjectType({
        name: 'Query',
        fields: {
            user: {
                type: userType,
                // Query arguments
                args: {
                    id: { type: graphql.GraphQLString },
                    name: { type: graphql.GraphQLString }
                },
                resolve: function (_, args) {
                    if (args.id && args.name) {
                        for (var id in data) {
                            if (args.id == data[id]["id"] && args.name == data[id]["name"]) {
                                return data[id];
                            }
                        }
                    } else if (args.id) {
                        return data[args.id];
                    } else  if (args.name) {
                        for (var id in data) {
                            if (args.name == data[id]["name"]) {
                                return data[id];
                            }
                        }
                    }
                }
            }
        }
    })
});

console.log('Server online!');
express()
    .use('/graphql', graphqlHTTP({ schema: schema, pretty: true }))
    .listen(3000);
