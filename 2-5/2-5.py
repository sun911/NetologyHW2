import subprocess
import os


def create_directory_if_missing(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print('Directory {0} was created'.format(folder_path))


def convert_images(current_dir, path_to_source, files):
    path_to_converter = os.path.join(current_dir, 'convert.exe')
    path_to_result = os.path.join(current_dir, 'Result')
    create_directory_if_missing(path_to_result)
    for file in files:
        subprocess.run(path_to_converter + ' "' + os.path.join(path_to_source, file) + '" -resize 200 "' + os.path.join(path_to_result, file) + '"')


if __name__ == '__main__':
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cur_dir, 'Source')
    files_list = os.listdir(path)
    convert_images(cur_dir, path, files_list)
