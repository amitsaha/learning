provider "aws" {
    access_key = "dwasd"
    secret_key = "asdsd"
    region = "us-west-2"
}

resource "aws_instance" "example1_terraform" {
    ami = "ami-01122131"
    instance_type = "t1.micro"
}
