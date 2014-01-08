
import os

def add_username_segment():
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u '
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n '
    else:
        user_prompt = ' %s ' % os.getenv('USER')

    root = os.getenv('USER') == 'root'
    admin = os.getenv('ADMIN')
    background = Color.READONLY_BG if root else Color.USERNAME_BG

    if root and admin:
        powerline.append(user_prompt, Color.USERNAME_FG, background, powerline.separator_thin, Color.SEPARATOR_FG, bold = True)
    else:
        powerline.append(user_prompt, Color.USERNAME_FG, background, bold = True)

    if admin:
        powerline.append(' admin ', Color.USERNAME_FG, Color.READONLY_BG, bold = True)

add_username_segment()
