var graphql = require('graphql');
var graphqlHTTP = require('express-graphql');
var express = require('express');
//var https = require('https');
//var requ = require('request');
var rp = require('request-promise');

// Define project type
var projectType = new graphql.GraphQLObjectType({
    name: 'Project',
    fields: {
        id: { type: graphql.GraphQLInt },
        owner_id: { type: graphql.GraphQLInt },
    }
});

var get_request_data = {
                        'headers': {'Freelancer-Developer-Auth-V1'
                                    : '18;FLNCGQ5TPC1KFOTMSIFJME87N5NT2E63',
                                   },
                       }

var schema = new graphql.GraphQLSchema({
    query: new graphql.GraphQLObjectType({
        name: 'Query',
        fields: {
            project: {
                type: projectType,
                // Query arguments
                args: {
                    id: { type: graphql.GraphQLInt },
                    owner_id: { type: graphql.GraphQLInt },
                    description: {type: graphql.GraphQLString}
                },
                resolve: function (_, args) {
                    var json_data;
                    if (args.id) {
                        // Make a HTTP GET request to Freelancer.com API
                        get_request_data['uri'] = 'https://www.freelancer.com/api/projects/0.1/projects/' + args.id + '/';
                        rp(get_request_data)
                            .then(JSON.parse).
                            then(function(json_data) {
                                console.log(json_data['result']['owner_id']);
                                return {'owner_id': json_data['result']['owner_id']}
                            })
                            .catch(function (err) {
                                console.log(err);
                            });
                    } else if (args.owner_id) {
                        return {'owner_id': args.owner_id};
                    } else {
                        return null;
                    }
                 
                }
            }
        }
    }
                                        )
});

console.log('GraphQL Server online!');
express()
    .use('/graphql', graphqlHTTP({ schema: schema, pretty: true }))
    .listen(8000);
