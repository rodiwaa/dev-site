# Dev Site
My dev portfolio website

## Website
- www.rohitdiwakar.com

## Tech Stack
- HTML Templates, JavaScript
- Azure Durable Functions, Python, Slack Integration (for [Contact Me Form](https://dev.to/rodiwa/how-i-implemented-a-smart-contact-me-form-1a48))

## Todos
- Headless CMS
- NextJS-ify completely

# Note

## URL
rohitdiwakar.com, www.rohitdiwakar.com

## Developer
### Local server
python3 -m http.server 8000

### Deploy to AWS
aws s3 sync . s3://rohitdiwakar.com

### Invalidate CFN cache
aws cloudfront create-invalidation --distribution-id E32FB74M1LHPJY --paths "/*"

### Folder
./client-updated-2
