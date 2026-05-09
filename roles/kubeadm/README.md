# Role: Kubeadm

## Description

Роль для установки и настройки Kubeadm.

## Requirements

- `ansible.builtin` - встроенные модули Ansible

## Variables

| Variable | Type | Default | Description |
| -------- | ---- | ------- | ----------- |
| `kubernetes_version` | string | "1.32" | Версия Kubernetes |

## Example Playbook

```yaml
- hosts: kubernetes
  become: yes
  roles:
    - role: kubeadm
      vars:
        kubernetes_version: "1.32"
```