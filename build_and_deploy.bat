docker build -t template-test .
kubectl apply -f .\kubernetes-manifests\
kubectl rollout restart deployment/template-test
kubectl get pods

