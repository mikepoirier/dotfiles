from utils import run_command


def format_uptime(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return '{0:02.0f}:{1:02.0f}:{2:02.0f}'.format(h, m, s)


uptime = float(run_command(['cat', '/proc/uptime'])[0].split()[0])

print(uptime)
print(format_uptime(uptime))
