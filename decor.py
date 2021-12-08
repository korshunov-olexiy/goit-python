from difflib import get_close_matches
import re

action_commands = ['help', 'hello', 'add', 'change', 'phone', 'show all']
exit_commands = ['good bye', 'close', 'exit']


def get_input_msg(input_msg):
    result = {}
    for cmd in action_commands + exit_commands:
        spaces = len(cmd.split())
        msg = re.sub(r" +", " ", input_msg).split(" ", maxsplit=spaces)
        raw_cmd, raw_msg = ' '.join(msg[:spaces]), ' '.join(msg[spaces:])
        match = ''.join(get_close_matches(raw_cmd, [cmd]))
        if match:
            result.update({match: raw_msg})
    return result


print(get_input_msg("hely   067 -431-23-15"))
