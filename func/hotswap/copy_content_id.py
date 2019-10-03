# 复制 content id

import pyperclip
import re

def copyCID():
    res = 'content|%d' % self.content_layout_current_id
    pyperclip.copy(res)