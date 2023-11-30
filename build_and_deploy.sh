#! /bin/bash
docker build --platform=linux/amd64 -t template-test .

docker tag template-test:latest 716039874842.dkr.ecr.us-west-2.amazonaws.com/template-test:latest

docker push 716039874842.dkr.ecr.us-west-2.amazonaws.com/template-test:latest

kubectl delete deployment template-test

kubectl apply -f ./kubernetes-manifests

kubectl get pods

