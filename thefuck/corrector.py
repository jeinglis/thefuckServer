from pathlib import Path
from thefucktypes import Rule

from rules.git import git_category
from rules.brew import brew_category
from rules.django import django_category
from rules.grep import grep_category
from rules.grep import grep_category
from rules.cargo import cargo_category
from rules.maven import maven_category
from rules.rm import rm_category
from rules.cd import cd_category
from rules.tsuru import tsuru_category

def get_loaded_rules(rules_paths):
    """Yields all available rules.

    :type rules_paths: [Path]
    :rtype: Iterable[Rule]

    """
    rules = []
    for path in rules_paths:
        if path.name != '__init__.py' and not path.name.endswith('_category.py'):
            rule = Rule.from_path(path)
            if rule.is_enabled:
                # yield rule
                rules.append(rule)
    return rules


def get_categories(command):
    """
    CATEGORIES = {folder : [keywords]}
    """
    CATEGORIES = {'git': git_category.match,
                  'brew': brew_category.match,
                  'django': django_category.match,
                  'grep': grep_category.match,
                  'grep': grep_category.match,
                  'cargo': cargo_category.match,
                  'maven': maven_category.match,
                  'rm': rm_category.match,
                  'cd': cd_category.match,
                  'tsuru': tsuru_category.match}
    rules = []
    rules += Path(__file__).parent \
        .joinpath('rules') \
        .joinpath('other') \
        .glob('*.py')

    for category, match_func in CATEGORIES.items():
        if match_func(command):
            print("Using category: " + category)    
            rules += Path(__file__).parent \
                .joinpath('rules') \
                .joinpath(category) \
                .glob('*.py')
        else:
            print("Ignoring category: " + category) 

    return rules


def get_rules(command):
    """Returns all enabled rules.

    :rtype: [Rule]

    """
    bundled = get_categories(command)
    return sorted(get_loaded_rules(sorted(bundled)),
                  key=lambda rule: rule.priority)


def organize_commands(corrected_commands):
    """Yields sorted commands without duplicates.

    :type corrected_commands: Iterable[thefuck.types.CorrectedCommand]
    :rtype: Iterable[thefuck.types.CorrectedCommand]

    """
    try:
        first_command = next(corrected_commands)
        return [first_command]
    except StopIteration:
        return

    without_duplicates = {
        command for command in sorted(
            corrected_commands, key=lambda command: command.priority)
        if command != first_command}

    sorted_commands = sorted(
        without_duplicates,
        key=lambda corrected_command: corrected_command.priority)

    print('Corrected commands: '.format(    
        ', '.join(u'{}'.format(cmd) for cmd in [first_command] + sorted_commands)))

    return sorted_commands
    # for command in sorted_commands:
        # yield command


def get_corrected_commands(command):
    """Returns generator with sorted and unique corrected commands.

    :type command: thefuck.types.Command
    :rtype: Iterable[thefuck.types.CorrectedCommand]

    """
    corrected_commands = (
        corrected for rule in get_rules(command)
        if rule.is_match(command)
        for corrected in rule.get_corrected_commands(command))
    return organize_commands(corrected_commands)
