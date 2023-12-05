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

Сборка осуществляется с помощью **GitHub Actions**. Необходимо выполнить следующие шаги

## Запуск тестов

Запуск тестов осуществляется с помощью Docker. Для запуска тестирования нужно использовать команду:
```bash
docker-compose -f docker/docker-compose.tests.yml up
```
