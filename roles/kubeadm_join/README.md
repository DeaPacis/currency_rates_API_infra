# Role: kubeadm_join

## Description

Роль подключает worker-ноды к Kubernetes кластеру с помощью команды `kubeadm join`.

Команда подключения должна быть получена с master-ноды.

## Requirements

* Выполнен `kubeadm init` на master
* Доступна join-команда
* Установлены:

  * kubeadm
  * kubelet
  * container runtime (CRI-O)

## Dependencies

* role: crio
* role: kubelet
* role: kubeadm
* role: kubeadm_init (на master)

## Variables

| Variable          | Type   | Default | Description                                |
| ----------------- | ------ | ------- | ------------------------------------------ |
| kube_join_command | string | ""      | Команда подключения worker-ноды к кластеру |

## Example Playbook

```yaml
- hosts: workers
  become: true
  roles:
    - role: kubeadm_join
```

## Notes

* Роль использует hostvars для получения join-команды с master-ноды
* Повторный запуск роли не приводит к повторному подключению (идемпотентность через creates)