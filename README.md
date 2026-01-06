# AWS-Rekognition---Nesne-Tan-ma-Projesi


Bu proje, AWS S3'e yüklenen görselleri AWS Lambda ve Amazon Rekognition kullanarak otomatik olarak analiz eder.

## Mimari
1. Kullanıcı S3 Bucket'ına bir görsel yükler.
2. S3 "ObjectCreated" olayı Lambda fonksiyonunu tetikler.
3. Lambda, görseli Amazon Rekognition'a gönderir.
4. Sonuçlar CloudWatch Logs üzerinde listelenir.

## Kullanılan Servisler
- **Amazon S3:** Görsel depolama.
- **AWS Lambda:** Serverless işleme.
- **Amazon Rekognition:** Derin öğrenme tabanlı nesne tanıma.
- **IAM:** Yetkilendirme ve roller.
