action_commands = ['help', 'hello', 'add', 'change', 'phone', 'show all']
exit_commands = ['good bye', 'close', 'exit']

action_commands = set(action_commands)
exit_commands = set(exit_commands)
user_commands = set(['good bye', 'help', 'add'])

#print(exit_commands.isdisjoint(user_commands))

print(bool(user_commands.difference(exit_commands)) & bool(user_commands.difference(action_commands)))

print([1] == [])
