from subprocess import run, PIPE

run_command_memo = {}


def run_command(args):
    key = ''.join(args)
    if key not in run_command_memo:
        results = run(args, stdout=PIPE).stdout.splitlines()
        run_command_memo[key] = [b.decode("utf-8") for b in results]
    return run_command_memo[key]


def get_number_of_updates():
    results = run_command(['pacaur', '-Qu'])
    return len(results)


def get_formatted_output():
    updates = get_number_of_updates()
    underline_color = '0x80000000'
    if updates > 0:
        underline_color = '0xFFE97F02'
    return '!Y U {} Y! : {}'.format(underline_color, updates)

print(get_formatted_output())
