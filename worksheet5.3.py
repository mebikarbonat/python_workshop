#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

from netmiko import ConnectHandler
linux = {
        'device_type': 'linux',
        'ip': '192.168.114.13',
        'username': 'python',
        'password': 'python123',
        'secret': 'python123',
        'port': 22,
        'verbose': True
        }
connection = ConnectHandler(**linux)
output = connection.send_command('uname -a')
print('This is your kernel version: \n')
print(output)
print(" \n")
print("Installing Apache2 Web Server...")

#installing apache2 web server
connection.enable()
output = connection.send_command('apt install apache2')
print(output)
connection.exit_enable_mode()