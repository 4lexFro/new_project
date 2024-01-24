# import os
# from pathlib import Path
# print(os.getcwd())
# print(Path.cwd())

# Перемещение на два уровня вверх:
# import os
# from pathlib import Path
# print(os.getcwd())
# print(Path.cwd())
# os.chdir('../..')
# print(os.getcwd())
# print(Path.cwd())

# Создание каталогов:
# import os
# from pathlib import Path
# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()

#Cоздать несколько вложенных друг в друга каталогов:
import os
from pathlib import Path
#os.makedirs('dir/other_dir/new_os_dir')
#Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True)

# Удаление каталогов:
import os
from pathlib import Path
# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()
# Удалить можно лишь пустой каталог. Если внутри удаляемого
# каталога есть другие каталоги или файлы, возникнет ошибка OSError.

# Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и
# файлы), подойдёт функция из модуля shutil
import shutil
shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')
# В первом случае будет удалена директория other_dir со всем содержимым.
# Директория dir останется на месте.
# Во втором случае удаляется каталог some_dir и его содержимое.