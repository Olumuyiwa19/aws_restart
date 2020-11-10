import subprocess
subprocess.run(["ls"])
subprocess.run(["ls", "-l"])

command = "uname"
commandArg = "-a"
print(f'Gathering system info with command: {command} {commandArg}')

subprocess.run([command, commandArg])

command = "ps"
commandArg = "-x"
print(f'Gathering active process info with command: {command} {commandArg}')
subprocess.run([command, commandArg])

command = "top"
print(f'Gathering active process info with command: {command}')
subprocess.run([command])