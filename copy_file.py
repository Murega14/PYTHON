#copyfile() = copies file content
# copy() = copies file + permission mode + destination canbe a directory
# copy2() =copy() + copies metadata

import shutil
shutil.copyfile('text.txt', 'copy.txt')