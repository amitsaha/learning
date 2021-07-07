package main

import (
	"dagger.io/gcp"
	"dagger.io/aws"

)

// FIXME: remove hardcoded input values
infra: {

	// AWS INFRA SETUP

	// AWS auth & default region
	awsConfig: aws.#Config & {
		region: "us-east-1"
	}
	// VPC Id
	vpcId: "vpc-020aefe0bcde19146" @dagger(input)
	// ECR Image repository
	ecrRepository: "125635003186.dkr.ecr.us-east-1.amazonaws.com/apps" @dagger(input)
	// ECS cluster name
	ecsClusterName: "bl-ecs-acme-764-ECSCluster-lRIVVg09G4HX" @dagger(input)
	// ELB listener ARN
	elbListenerArn: "arn:aws:elasticloadbalancing:us-east-1:125635003186:listener/app/bl-ec-ECSAL-OSYI03K07BCO/3c2d3e97468bde5b/d02ac91cc007e34e" @dagger(input)
	// Secret ARN for the admin password of the RDS Instance
	rdsAdminSecretArn: "arn:aws:secretsmanager:us-east-1:125635003186:secret:AdminPassword-NQbBi7oU4329-IGgS3B" @dagger(input)
	// ARN of the RDS Instance
	rdsInstanceArn: "arn:aws:rds:us-east-1:125635003186:cluster:bl-rds-acme-764-rdscluster-8eg3mjrkvrsg" @dagger(input)

	// GOOGLE CLOUD INFRA SETUP
	gcpConfig:      gcp.#Config                @dagger(input)
	gkeClusterName: "test-cluster"             @dagger(input)
	gcrRepository:  "gcr.io/dagger-ci/example" @dagger(input)
}
