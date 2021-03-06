
import os
import pwd

def add_username_segment():
    user = pwd.getpwuid(os.getuid())[0]

    if user not in ['root', 'jlee', 'jtl']:
        if powerline.args.shell == 'bash':
            user_prompt = ' \\u '
        elif powerline.args.shell == 'zsh':
            user_prompt = ' %n '
        else:
            user_prompt = ' %s ' % os.getenv('USER')

        powerline.append(user_prompt, Color.USERNAME_FG, Color.USERNAME_BG, bold = True)

add_username_segment()
