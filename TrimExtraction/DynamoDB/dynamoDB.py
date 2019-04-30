import os
# os.environ["TZ"] = "UTC"
import boto3


def connect():
    try:
        dynamodb_client = getClientInstance()
        response = dynamodb_client.describe_table(TableName='vehicle_image')
        return True
    except:
        try:
            create_table()
            return True
        except:

            return False

def create_table():
    try:
        dynamodb = getResourceInstance()
        table = dynamodb.create_table(
        TableName='vehicle_image',
        KeySchema=[
            {
                'AttributeName': 'ImageID',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'Action',
                'KeyType': 'RANGE'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'ImageID',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Action',
                'AttributeType': 'S'  #Partition key
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 2
        }
        )

        #print("Table status:", table.table_status)
    except:
        print("Error While creating database")

def getResourceInstance():
    return boto3.resource('dynamodb')

def getClientInstance():
    return boto3.client('dynamodb')

def log_entry(msg):
    try:
        dynamodb = getResourceInstance()
        connect()
        table = dynamodb.Table("vehicle_image")
        table.put_item(Item = msg)
    except Exception as e:
        print("Error while pushing log to DB" + str(e))
