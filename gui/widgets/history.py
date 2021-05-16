import re
import subprocess


def get_git_history():
    result = subprocess.check_output(['git', 'log'])
    result = result.decode('utf-8')
    dates = re.findall(r'Date:\s*(.*)?\+\d*', result)
    return dates
