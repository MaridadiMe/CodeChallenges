"""
This module will take a folder path and create a zip archive


"""
from zipfile import ZipFile
import os
import pathlib
import os.path

def create_zip(input_path, file_extensions, output_path):
    # if output path is not provided use the input path + .zip extension
    # if the input path is a file create a zip file
    try:
        with ZipFile(output_path, 'w') as myZip:
            for root, dirs, files in os.walk(input_path):
                relative_path = os.path.relpath(root, input_path)
                for file in files:
                    file_extension = pathlib.Path(file).suffix
                    if file_extension.lower() in file_extensions:
                        myZip.write(os.path.join(root, file), arcname=os.path.join(relative_path,file))
    except e as Exception:
        print(e)

            
if __name__ == '__main__':
    create_zip('../code_challenge', ['.csv'], 'csv.zip')
        