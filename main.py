from netifaces import AF_INET, gateways
import paramiko, os, subprocess

user = 'login'
secret = 'password'
port = 22
command = 'system reboot'

gws = gateways() # Смотрит все сетевые подключения
device = gws['default'][AF_INET][0] # Тут берем IP шлюза


def reboot():
    client = paramiko.SSHClient() # Создание SSH сессии
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Разрешение SSH ключей
    print("Connect to", '"' + device + '"')
    client.connect(hostname=device, username=user, password=secret, port=port) # Подключение к шлюзу
    print("send", '"' + command + '"')
    client.exec_command(command) # Отправка в ребут
    print("send y")
    client.exec_command("y") # Подтверждение
    print(f" {device} done")
    client.close() # Закрытие SSH сессии


def main():
    reboot()


if __name__ == "__main__":
    main()