import os
from common.handlepath import REPORTDIR


def delete_report():

    files = os.listdir(REPORTDIR)

    if len(files) == 5:
        for i in files:
            file_path = os.path.join(REPORTDIR, i)
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                pass
    else:
        pass

delete_report()