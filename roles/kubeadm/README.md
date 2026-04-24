# Kubeadm Role

## Описание
Роль для установки и настройки Kubeadm.

## Зависимости
- `ansible.builtin` - встроенные модули Ansible

## Переменные

| Переменная | Тип | Значение по умолчанию | Описание |
|------------|-----|----------------------|-----------|
| `kubernetes_version` | string | "1.32" | Версия Kubernetes |

## Пример использования

```yaml
- hosts: kubernetes
  become: yes
  roles:
    - role: kubeadm
      vars:
        kubernetes_version: "1.32"