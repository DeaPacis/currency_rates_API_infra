# Role: CRIO

## Description

Роль для установки и настройки CRI-O (Container Runtime Interface for OCI) версии 1.32.

## Requirements

- `ansible.builtin` - встроенные модули Ansible
- `community.general` - дополнительные модули (при необходимости)
- `ansible.posix` - модуль sysctl для настройки ядра

## Variables

| Variable | Type | Default | Description |
| -------- | ---- | ------- | ----------- |
| `crio_version` | string | "1.32" | Версия CRI-O |
| `crio_kubernetes_version` | string | "1.32" | Версия Kubernetes для совместимости |
| `crio_cgroup_driver` | string | "systemd" | Cgroup driver для CRI-O |
| `crio_container_storage_dir` | string | "/var/lib/containers" | Директория для хранения контейнеров |

## Example Playbook

```yaml
- hosts: kubernetes
  become: yes
  roles:
    - role: crio
      vars:
        crio_version: "1.32"
        crio_cgroup_driver: "systemd"
```