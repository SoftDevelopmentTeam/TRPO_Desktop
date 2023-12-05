# TRPO_Desktop

[![Flake8](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/flake.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/flake.yml)
[![Tests](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/tests.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/tests.yml)
[![Build on Ubuntu](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_ubuntu.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_ubuntu.yml)
[![Build on Windows](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_windows.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_windows.yml)
[![Build on macOS](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_macOS.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_macOS.yml)

## Сборка Linux

Для сборки необходимо перейти в папку **scripts** и выполнить

```bash
sudo ./build.sh
```

Запуск скрипта необходимо выполнять от имени суперпользователя, поскольку происходит копирование файла **client_secrets.json**, необходимого для корректной работы с Google Drive, в папку с исполняемым файлом приложения. В противном случае данный файл нужно копировать вручную

## Сборка Windows

Сборка осуществляется с помощью **GitHub Actions**. Необходимо сделать fork данного репозитория и выполнить следующие шаги

![image](https://github.com/RiMikheev/TRPO_Desktop/assets/122991783/a346046f-eb56-4cd3-a63c-9e8f30a6809c)

![image](https://github.com/RiMikheev/TRPO_Desktop/assets/122991783/2454868b-475d-4883-981a-3dbd6a014290)

![image](https://github.com/RiMikheev/TRPO_Desktop/assets/122991783/f9bbf0a5-1690-484f-a79f-809011c03af6)

![image](https://github.com/RiMikheev/TRPO_Desktop/assets/122991783/2ee2dd99-4760-4e56-afbd-8747fc224b0b)

![image](https://github.com/RiMikheev/TRPO_Desktop/assets/122991783/f5342075-c76f-41da-b380-e7e14fa9645b)

После выполнения вышеуказанных шагов запустится пайплайн сборки. После его выполнения нужно скачать следующий архив

![image](https://github.com/RiMikheev/TRPO_Desktop/assets/122991783/8745c569-40e9-46e4-b4ea-2382854f23ce)

Нельзя перемещать исполняемый файл отдельно от **client_secrets.json**, так как он необходим для корректной работы Google Drive

## Запуск тестов

Запуск тестов осуществляется с помощью Docker. Для запуска тестирования нужно использовать команду:
```bash
docker-compose -f docker/docker-compose.tests.yml up
```
