import json
from subprocess import run, PIPE

run_command_memo = {}


def run_command(args):
    key = ''.join(args)
    if key not in run_command_memo:
        results = run(args, stdout=PIPE).stdout.splitlines()
        run_command_memo[key] = [b.decode("utf-8") for b in results]
    return run_command_memo[key]


def get_workspaces():
    results = run_command(['i3-msg', '-t', 'get_workspaces'])[0]
    data = json.loads(results)
    return data


def foo(x):
    template = '<span>{}</span>'
    focused_template = '<span underline="single">{}</span>'
    if x['focused']:
        return focused_template.format(x['name'])
    else:
        return template.format(x['name'])


def get_output():
    workspaces = get_workspaces()
    return [foo(x) for x in workspaces]


print(' | '.join(get_output()))
