from subprocess import run, PIPE

run_command_memo = {}


def run_command(args):
    key = ''.join(args)
    if key not in run_command_memo:
        results = run(args, stdout=PIPE).stdout.splitlines()
        run_command_memo[key] = [b.decode("utf-8") for b in results]
    return run_command_memo[key]


def wifi_connected():
    results = run_command(['iwgetid'])
    return len(results) > 0


def get_ssid():
    results = run_command(['iwgetid'])[0]
    connection_name = results[results.find('"'):].replace('"', '')
    return connection_name


def get_connection_strength():
    with open("/proc/net/wireless") as f:
        lines = f.readlines()
        strength = lines[2].split()[2].replace('.', '')

    return strength


msg = "!Y u0xffffffff Y! : {}"
info = "Disconnected"
if wifi_connected():
    info = '{} ({}%)'.format(get_ssid(), get_connection_strength())

print(msg.format(info))
