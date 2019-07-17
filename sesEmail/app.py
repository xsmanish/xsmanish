from chalice import Chalice
import boto3
from botocore.exceptions import ClientError

app = Chalice(app_name='sesEmail')


@app.route('/')
def index():
    return {'response': 'ok'}

@app.route('sendsesEmail')
def ses_email(send_email):
ACCESS_KEY_ID = '*'
ACCESS_SECRET_KEY = '*'
AWS_DEFAULT_REGION='us-east-2'
AWS_REGION = "us-west-2"
SENDER = "Manish Shrivastava <xsmanish@gmail.com>"
RECIPIENT = "xsmanish@gmail.com"
SUBJECT = "Amazon SES Test Email"

BODY_TEXT = ("Amazon SES Test Email \r\n"
             "This email was sent with Amazon "
            )

BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test EMAIL</h1>
</body>
</html>
            """

CHARSET = "UTF-8"
client = boto3.client('ses',region_name=AWS_REGION)

try:
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId']) 
    




# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
