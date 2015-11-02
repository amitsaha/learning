var graphql = require('graphql');
var graphqlHTTP = require('express-graphql');
var express = require('express');
var http_promise = require('request-promise');

// Define project type
var projectType = new graphql.GraphQLObjectType({
    name: 'Project',
    fields: {
        id: { type: graphql.GraphQLInt },
        owner_id: { type: graphql.GraphQLInt },
        description: { type: graphql.GraphQLString},
    }
});

var get_request_data = {
    'headers': {
        'Freelancer-Developer-Auth-V1': process.env.TOKEN,
    }
}

var schema = new graphql.GraphQLSchema({
    query: new graphql.GraphQLObjectType({
        name: 'Query',
        fields: {
            project: {
                type: projectType,
                // Query project by ID
                args: {
                    id: { type: graphql.GraphQLInt },
                },
                resolve: function (_, args) {
                    if (args.id) {
                        get_request_data['uri'] = 'https://www.freelancer.com/api/projects/0.1/projects/' + args.id + '/';
                        var get_result = http_promise(get_request_data)
                            .then(function(data) {
                                json_data = JSON.parse(data);
                                return {'id': args.id,
                                        'owner_id': json_data['result']['owner_id'],
                                        'description': json_data['result']['preview_description'],
                                       };
                        })
                            .catch(function(err) {
                                return new Error(err['response']['body']);
                            });
                        return get_result;
                    } else {
                        return null;
                    }
                }
            }
        }
    })
});
console.log('GraphQL Server online!');
express()
    .use('/graphql', graphqlHTTP({ schema: schema, pretty: true }))
    .listen(8000);
