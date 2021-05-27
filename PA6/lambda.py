import json, boto3
from dateutil import tz
from datetime import datetime

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    
    if 'status' in event.keys():
        #print(f"office hours are currently {event['status']}")
        timezone = tz.gettz("America/New_York")
        print(timezone)
        rn = datetime.now(tz=timezone)
        rn_fmtd = rn.strftime("%A %B %d, %Y at %I:%M %p %Z")
        print(rn_fmtd)
        string = f"<p>Prof. Humphrey's office hours are currently {event['status']} <br><br> Last Generated: {rn_fmtd}</p>"
        
        
        bucket_name = "bwe3bx-cs4740-pa6"
        file_name = "index.html"
        lambda_path = "/tmp/" + file_name
        
        s3 = boto3.resource("s3")
        s3.Bucket(bucket_name).put_object(Key=file_name, Body=string, 
        ContentType='text/html')
    #raise Exception('Something went wrong')

