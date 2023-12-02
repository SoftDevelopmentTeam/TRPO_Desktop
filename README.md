# TRPO_Desktop

[![Flake8](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/flake.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/flake.yml)
[![Tests](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/tests.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/tests.yml)
[![Build on Ubuntu](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_ubuntu.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_ubuntu.yml)
[![Build on Windows](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_windows.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_windows.yml)
[![Build on macOS](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_macOS.yml/badge.svg)](https://github.com/RiMikheev/TRPO_Desktop/actions/workflows/build_macOS.yml)

## Сборка

Для сборки приложения необходимо установить Pyinstaller:
```bash
pip/pip3 install pyinstaller
```

Сборка одним файлом:
```bash
pyinstaller --onefile app/main.py
```
Исполняемый файл будет располагаться в папке ./dist

## Запуск тестов

Запуск тестов осуществляется с помощью Docker. Для первого запуска тестирования нужно использовать команду:
```bash
docker-compose up
```
Для последующих запусков:
```bash
docker-compose build --no-cache
docker-compose up
```
