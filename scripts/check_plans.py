import os
import glob
import datetime

for f in sorted(glob.glob("docs/trade_plans/*.md")):
    stat = os.stat(f)
    mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
    size = stat.st_size
    print(f"{f}: size={size} bytes, mtime={mtime}")
