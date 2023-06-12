### AI Chatbot
Leveraging the power of LLM's to serve as a chatbot to summarize and answer questions about a given text.

### This branch is deployed on elastic beanstalk

### How to run locally:
1. Pull docker containers:
```
docker pull 444133344330.dkr.ecr.eu-central-1.amazonaws.com/api:latest && docker pull 444133344330.dkr.ecr.eu-central-1.amazonaws.com/web:latest
```
2. run `docker-compose up -d`
3. In the browser type `localhost:80`
