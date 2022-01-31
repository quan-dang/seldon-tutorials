#!/usr/bin/env bash
# deploy online
kubectl apply -f seldon.yml -n models
# rollout
kubectl rollout status deploy/$(kubectl get deploy -l seldon-app=sklearn-default -o jsonpath='{.items[0].metadata.name}' -n models) -n models