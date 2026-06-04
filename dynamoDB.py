import boto3


def dynamodb_add_item():
    dynamodb = boto3.client('dynamodb')

    dynamodb.put_item(
        TableName='Music',
        Item={
            'Artist': {'S': 'Taylor Swift'},
            'Song': {'S': 'Love Story'},
            'Album': {'S': 'Fearless'},
            'Year': {'N': '2008'}
        }
    )

def dynamo_get_item():
    dynamodb = boto3.client('dynamodb')

    item = dynamodb.get_item(
        TableName='Music',
        Key={
            'Artist': {'S': 'Taylor Swift'},
            'Song': {'S': 'Love Story'}
        }
    )
    return item;