## Использование

Для запуска проекта Store Backend с использованием Docker Compose выполните следующие шаги:

1. Откройте окно терминала.

2. Перейдите в директорию `scripts`:

   ```sh
   cd scripts
   ```
3. Запустите скрипт local_start.sh:
    ```sh
    ./local_start.sh
    ```
    Этот скрипт будет использовать Docker Compose для сборки и запуска проекта Django и связанных сервисов.

Не забудьте предоставить права на выполнение скрипту local_start.sh, если это необходимо:

```sh
chmod +x local_start.sh

```
Также не забудьте файл .env в src:
```sh
cp .env.Example src/.env
```
Эта команда копирует файл .env.example в директорию src и одновременно переименовывает его в .env. Пожалуйста, убедитесь, что вы выполняете эту команду из корневой директории вашего проекта.

## Эндпоинты