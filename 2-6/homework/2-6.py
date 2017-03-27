import glob
import os.path

def convert_files(list_files, result_dir):
    for file_name in list_files:
        print(file_name)
        image_name_output = os.path.join(result_dir, os.path.basename(file_name))
        cmd = 'convert {} -resize 200 {}'.format(file_name, image_name_output)
        print(cmd)
        os.system(cmd)

def main():
    images_dir = 'Source'

    files = glob.glob(os.path.join(images_dir, "*.jpg"))
    for file in files:
        print(file)

    result_dir = 'Result'
    try:
        os.mkdir(result_dir)
        #print(result_dir)
    except FileExistsError:
        print('Директория создана ранее.')

    convert_files(files, result_dir)
    print('Всего {} файлов'.format(len(files)))

if __name__ == '__main__':
    main()