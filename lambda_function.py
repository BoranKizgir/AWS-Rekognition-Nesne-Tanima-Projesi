Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import boto3
... 
... def lambda_handler(event, context):
...     rekognition = boto3.client('rekognition')
...     s3 = boto3.client('s3')
...     
...     # Event içinden bucket ve dosya adını al
...     bucket = event['Records'][0]['s3']['bucket']['name']
...     key = event['Records'][0]['s3']['object']['key']
...     
...     # Rekognition ile analiz et
...     response = rekognition.detect_labels(
...         Image={'S3Object': {'Bucket': bucket, 'Name': key}},
...         MaxLabels=10
...     )
...     
...     print(f"Analiz edilen dosya: {key}")
...     for label in response['Labels']:
...         print(f"Nesne: {label['Name']} - Güven: %{label['Confidence']:.2f}")
...         
