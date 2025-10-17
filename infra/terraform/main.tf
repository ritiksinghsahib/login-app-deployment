
resource "null_resource" "kubeadm_init" {
  provisioner "local-exec" {
    command = "ssh root@master-node 'kubeadm init --pod-network-cidr=10.244.0.0/16'"
  }
}

resource "null_resource" "kubeadm_join" {
  count = 3
  provisioner "local-exec" {
    command = "ssh root@worker-node-${count.index} 'kubeadm join <master-ip>:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>'"
  }
}
