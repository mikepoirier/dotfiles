import os
from subprocess import PIPE, run


def run_command(args, input_data=None, stdout=PIPE):
    result = run(args, input=input_data, stdout=stdout).stdout
    return result


def parse_network(output):
    return str(output)[2:-3]


command1 = ['nmcli', 'd']
command2 = ['grep', 'wifi']
command3 = ['awk', '{print $4}']

output = run_command(command3,
                     run_command(command2,
                                 run_command(command1)))

print(" : {}".format(parse_network(output)))
