# This is the configuration file for your powerline-shell prompt
# Every time you make a change to this file, run install.py to apply changes
#
# For instructions on how to use the powerline-shell.py script, see the README

# Add, remove or rearrange these segments to customize what you see on the shell
# prompt. Any segment you add must be present in the segments/ directory

SEGMENTS = [
# Show current virtual environment (see http://www.virtualenv.org/)
    'virtual_env',

# Show the current user's username as in ordinary prompts
    'username',

# Show the machine's hostname. Mostly used when ssh-ing into other machines
    'hostname',

# Show the current directory. If the path is too long, the middle part is
# replaced with ellipsis ('...')
    'cwd',

# Show a padlock if the current user has no write access to the current
# directory
    'read_only',

# Show number of running jobs
    'jobs',
]

# Change the colors used to draw individual segments in your prompt
THEME = 'tomorrow'
