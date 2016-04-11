import re
from utils import for_app
from specific.sudo import sudo_support
from shells import shell


@sudo_support
@for_app('cd')
def match(command):
    return (('no such file or directory' in command.stderr.lower()
             or 'cd: can\'t cd to' in command.stderr.lower()
             or 'the system cannot find the path specified.' in command.stderr.lower()))


@sudo_support
def get_new_command(command):
    repl = shell.and_('mkdir -p \\1', 'cd \\1')
    return re.sub(r'^cd (.*)', repl, command.script)
