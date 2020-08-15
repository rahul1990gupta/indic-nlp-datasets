import sys
_ver = sys.version_info

py2 = _ver.major == 2
py3 = _ver.major == 3

if py2:
    import subprocess.call as run_process
if py3:
    import subprocess.run as run_process
