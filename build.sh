# Build Docker image
docker build -t konlpy-lambda .

# Create ECR repository if it doesn't exist
aws ecr create-repository --repository-name konlpy-lambda

# Authenticate Docker to the ECR registry
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 957109489055.dkr.ecr.ap-northeast-2.amazonaws.com

# Tag Docker image
docker tag konlpy-lambda:latest 957109489055.dkr.ecr.ap-northeast-2.amazonaws.com/konlpy-lambda:latest

# Push Docker image
docker push 957109489055.dkr.ecr.ap-northeast-2.amazonaws.com/konlpy-lambda:latest
