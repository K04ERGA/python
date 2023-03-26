import paramiko

host = input('Host: ')
user = input('User: ')
secret = input('Password: ')
port = 22


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
choice = int(input("show ip interfaces - 1,\n"
                   "show ip routes - 2,\n"
                   "show ip neighbours - 3,\n"
                   "show netstat statistic - 4\n"
                   "show list of open files - 5\n"
                   "show uptime - 6\n"
                   ))

commands = ("ip a", "ip r", "ip neigh", "netstat", "lsof", "uptime")

(stdin, stdout, stderr) = client.exec_command(commands[choice - 1])

output = stdout.read()
print(str(output, 'utf8'))
if str(stderr.read(), 'utf8') != '':
    print("This tool is not installed")
