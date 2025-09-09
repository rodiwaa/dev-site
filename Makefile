site-run:
	python3 -m http.server 8001

deploy-aws:
	aws s3 sync . s3://rohitdiwakar.com

cfn-invalidate:
	aws cloudfront create-invalidation --distribution-id E32FB74M1LHPJY --paths "/*"

fresh-deploy:
	make deploy-aws cfn-invalidate
	