from aggregate.todo import Todo
import uuid
import boto3
import settings

dynamodb = boto3.resource('dynamodb', region_name=settings.AWS_REGION, endpoint_url=settings.DB_ENDPOINT)
client = boto3.client('dynamodb', region_name=settings.AWS_REGION, endpoint_url=settings.DB_ENDPOINT)

table_name = 'Todo'

def getTable():
  try:
    client.describe_table(TableName = table_name)
    table = dynamodb.Table(table_name)
    print("Loading Todos table")
  except:
    table = createTable(table_name)
    
  return table

def createTable(table_name):
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'creator',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'id',
                'KeyType': 'RANGE'  #Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'creator',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print("Todos table has been created")
    return table
  
table = getTable()
  
def createTodo(name):
  id = str(uuid.uuid4())
  return Todo(name, id)  
  
def saveTodo(todo):
  table.put_item(
    Item={
      'id': todo.id,
      'creator': todo.name
    }
  )
  
#  return todo_table.put_item
def fetchTodoByCreator(name):
  return None
  #  return todo

def fetchTodoById(id):
  response = table.get_item(
    Key={
      'id': id,
      'name': ''
    }
  )
  item = response['Item']
  return Todo(item.id, item.name)