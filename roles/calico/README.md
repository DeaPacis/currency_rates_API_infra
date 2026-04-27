# Role: calico

## Description

Роль устанавливает CNI плагин Calico в Kubernetes кластер.

Обеспечивает:

* сетевое взаимодействие между pod'ами
* настройку pod network

## Requirements

* Кластер должен быть инициализирован (`kubeadm init`)
* kubectl должен быть настроен
* Доступ к kubeconfig (admin.conf)

## Dependencies

* role: kubeadm_init

## Variables

| Variable            | Type   | Default                                                | Description          |
| ------------------- | ------ | ------------------------------------------------------ | -------------------- |
| calico_manifest_url | string | "https://docs.projectcalico.org/manifests/calico.yaml" | URL манифеста Calico |
| kubeconfig_path     | string | "/etc/kubernetes/admin.conf"                           | Путь к kubeconfig    |

## Example Playbook

```yaml
- hosts: master
  become: true
  roles:
    - role: calico
```

## Notes

* После установки Calico статус нод должен перейти в Ready
* Если pod_network_cidr не совпадает с конфигурацией Calico — сеть работать не будет