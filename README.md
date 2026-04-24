Отдельный репозиторий для хранения конфигурации инфраструктуры

Для конфигурирования хостов с помощью Ansible необходимо установить на control-node:
```bash
sudo apt install python3
sudo apt install python3.12-venv
```
Создать виртуальное окружение:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Установить ansible и molecule и проверить установку:
```bash
pip install ansible ansible-dev-tools molecule molecule-docker docker testinfra
which ansible
```
Запустить раскатку через:
```bash
ansible-playbook playbook.yml -i inventory.yml
```
Запуск тестирования с помощью Molecule (в директории каждой отдельной роли):
```bash
molecule test
```