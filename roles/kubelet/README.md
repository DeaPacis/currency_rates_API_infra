# Role: Kubelet

## Description

Роль для установки и настройки Kubelet на Ubuntu.

## Requirements

- `ansible.builtin` - встроенные модули Ansible
- `ansible.posix` - модуль mount для управления системой

## Variables

| Variable | Type | Default | Description |
| -------- | ---- | ------- | ----------- |
| `kubernetes_version` | string | "1.32" | Версия Kubernetes |
| `kubelet_extra_args` | string | "" | Дополнительные аргументы для kubelet |
| `kubelet_node_ip` | string | "" | IP адрес узла (пусто - автоопределение) |

## Example Playbook

```yaml
- hosts: kubernetes
  become: yes
  roles:
    - role: kubelet
      vars:
        kubernetes_version: "1.32"
        kubelet_extra_args: "--max-pods=110"
```