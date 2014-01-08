# Basic theme which only uses colors in 0-15 range

class Color(DefaultColor):
    USERNAME_FG = 0
    USERNAME_BG = 4
    USERNAME_SEPARATOR = 9

    HOSTNAME_FG = -1 # no color
    HOSTNAME_BG = 7  # medium gray

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 15 # dark gray
    PATH_FG = -1 # no color
    CWD_FG = -1  # no color
    SEPARATOR_FG = 7

    READONLY_BG = 1
    READONLY_FG = 0

    REPO_CLEAN_BG = 2  # green
    REPO_CLEAN_FG = 0  # black
    REPO_DIRTY_BG = 1  # red
    REPO_DIRTY_FG = 15 # white

    JOBS_FG = 0
    JOBS_BG = 10

    CMD_PASSED_BG = 8
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0
