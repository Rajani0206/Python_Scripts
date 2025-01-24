awsdata={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": ["iam:ChangePassword"],
      "Resource": "*"
    },
    {
      "Sid": "SecondStatement",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "ThirdStatement",
      "Effect": "Allow",
      "Action": [
        "s3:List*",
        "s3:Get*"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data",
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data/*"
      ],
      "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
    }
  ]
}

print(awsdata)
print(awsdata["Version"])
print(awsdata["Statement"][0]["Sid"])
print(awsdata["Statement"][1])
print(awsdata["Statement"][1]["Action"])
print(awsdata["Statement"][2]["Action"][1])
print(awsdata["Statement"][1]["Action"])
print(awsdata["Statement"][2]["Action"][0])
print(awsdata["Statement"][2]["Resource"][0])
print(awsdata["Statement"][2]["Resource"][1])
print(awsdata["Statement"][2]["Condition"]["Bool"]["aws:MultiFactorAuthPresent"])

