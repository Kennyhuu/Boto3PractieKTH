import boto3

'''
Common DynamoDB types
When using boto3.client('dynamodb'), you must use:

'S' → String
'N' → Number (must be a string like '2008')
'BOOL' → Boolean
'M' → Map (dictionary/object)
'L' → List
'NULL' → Null

'''

def dynamodb_add_item():
    dynamodb = boto3.client('dynamodb') # boto3.client (low-level / raw API)

    #dynamodb = boto3.resource('dynamodb') # boto3.resource (high-level / Pythonic)

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


def dynamodb_get_all_items():
    dynamodb = boto3.client('dynamodb')

    items = []
    response = dynamodb.scan(
        TableName='Music',
    )
    items.extend(response['Items'])
    while 'LastEvaluatedKey' in response:
        response = dynamodb.scan(
            TableName='Music',
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        items.extend(response['Items'])

    return items


'''
if __name__ == "__main__":

    item = dynamodb_add_item()
    
    item = dynamodb_get_item()
    
    print(item)
    
    item = dynamoDB.dynamodb_get_all_items()
    for i in item:
        print(i)
'''

