action_cmd = ['help', 'hello', 'add', 'change', 'phone', 'show all']
exit_cmd = ['good bye', 'close', 'exit']
list_of_function = ['cmd_help', 'cmd_hello', 'cmd_add', 'cmd_change', 'cmd_phone', 'cmd_show_all'] + ['cmd_exit']*len(exit_cmd)

user_cmd = {'close', 'add'}
commands_func = {cmd: func for cmd, func in zip(action_cmd+exit_cmd, list_of_function)}

print(commands_func)


def analize_input_msg(cmd_user, cmd_action, cmd_exit):
    action_cmd = set(cmd_action)
    exit_cmd = set(cmd_exit)
    # если есть элемент из user_cmd в action_cmd возвращается False !!
    in_action = not cmd_user.isdisjoint(cmd_action)
    in_exit = not cmd_user.isdisjoint(cmd_exit)

    if in_exit and in_action:
        '''check action or exit'''
        print("Choice command:")
        commands_func.update({cmd_exit[0]: None})
        for one_cmd_user in cmd_user:
            '''run command choces user from menu'''
    elif in_exit and not in_action:
        '''exit program'''
    elif not in_exit and in_action:
        '''check what is action'''
    elif not in_exit and not in_action:
        '''print(not know command)'''


#  1 & 1  =  1
#  1 & 0  =  0
#  0 & 1  =  0
#  0 & 0  =  0
