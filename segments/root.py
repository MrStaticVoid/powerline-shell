import os

def add_root_indicator_segment():
    root = os.getuid() == 0
    admin = os.getenv('ADMIN')
    background = Color.ROOT_BG if root else Color.USERNAME_BG

    if root and admin:
        powerline.append('', Color.USERNAME_FG, background, powerline.separator_thin, Color.SEPARATOR_FG)
    else:
        powerline.append('', Color.USERNAME_FG, background)

    if admin:
        powerline.append('', Color.USERNAME_FG, Color.ROOT_BG)

add_root_indicator_segment()
