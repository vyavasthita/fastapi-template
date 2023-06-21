#!/bin/bash

DEBIAN_FRONTEND=noninteractive

echo "Downloading Minikube..."
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb

echo "Installing minikube"
sudo dpkg -i minikube_latest_amd64.deb

echo "Removing minikube debian package if exists"
[ -e minikube_latest_amd64.deb ] && rm minikube_latest_amd64.deb

# echo "Install kubectl"
snap install kubectl --classic
# echo "Downloading kubectl"
# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# echo "Download the kubectl checksum file"
# curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

# echo "Validate the kubectl binary against the checksum file"
# echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check

# echo "Install kubectl"
# sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

