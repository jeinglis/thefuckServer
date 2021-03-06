import re
from shells import shell
from specific.git import git_support
from utils import eager


@git_support
def match(command):
    return ('branch' in command.script
            and "fatal: A branch named '" in command.stderr
            and " already exists." in command.stderr)


@git_support
@eager
def get_new_command(command):
    branch_name = re.findall(
        r"fatal: A branch named '([^']*)' already exists.", command.stderr)[0]
    new_command_templates = [['git branch -d {0}', 'git branch {0}'],
                             ['git branch -D {0}', 'git branch {0}'],
                             ['git checkout {0}']]
    for new_command_template in new_command_templates:
        yield shell.and_(*new_command_template).format(branch_name)
