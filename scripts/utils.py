from subprocess import run, PIPE

run_command_memo = {}


def run_command(args):
    key = ''.join(args)
    if key not in run_command_memo:
        results = run(args, stdout=PIPE).stdout.splitlines()
        run_command_memo[key] = [b.decode("utf-8") for b in results]
    return run_command_memo[key]
