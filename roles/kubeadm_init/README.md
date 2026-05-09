# Role: kubeadm_init

## Description

Роль выполняет инициализацию Kubernetes control plane с помощью kubeadm.

В рамках роли:

* выполняется `kubeadm init`
* настраивается доступ к кластеру через kubectl
* генерируется команда для подключения worker-нод

## Requirements

* kubeadm
* kubelet
* CRI-O (или другой container runtime)
* Отключенный swap
* Настроенные sysctl параметры

## Dependencies

* role: crio
* role: kubelet
* role: kubeadm

## Variables

| Variable | Type | Default | Description |
| -------- | ---- | ------- | ----------- |
| pod_network_cidr | string | "192.168.0.0/16" | CIDR для pod-сети (должен совпадать с CNI) |
| kubeconfig_path  | string | "/etc/kubernetes/admin.conf" | Путь к kubeconfig |

## Example Playbook

```yaml
- hosts: master
  become: true
  roles:
    - role: kubeadm_init
      vars:
        pod_network_cidr: "192.168.0.0/16"
```