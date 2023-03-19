import tarfile
import sys
import zipfile
from pathlib import Path
from normalize import normalize





CATEGORIES = {'audio': ['.mp3','.ogg', '.wav', '.amr'],
              'images': ['.png', '.jpg', '.svg', '.jpeg'],
              'documents': ['.txt', '.doc', '.docx', '.pdf', '.xlsx', '.pptx'],
              'video': ['.avi', '.mp4', '.mov', '.mkv'],
              'archives': ['.zip', '.tar', '.gz']
              }





def move_file(file:Path, root_dir:Path, category:str):
    
    
    if category == 'unknown':
        return file.replace(root_dir.joinpath(file.name))
    
    target_dir = root_dir.joinpath(category)
    
    if not target_dir.exists():
        target_dir.mkdir()\


    if category == 'archives':
        archive_dir = target_dir.joinpath(normalize(file.stem))
        if not archive_dir.exists():
            archive_dir.mkdir()

        if file.suffix == '.zip':
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(archive_dir)
        elif file.suffix in ('.tar', '.gz'):
            with tarfile.open(file, 'r:*') as tar_ref:
                tar_ref.extractall(archive_dir)
    else:
        normalized_name = normalize(file.name)
        return file.replace(target_dir.joinpath(normalized_name))




def get_categories(file:Path):
    extension = file.suffix.lower()
    
    for cat, exts in CATEGORIES.items():
        if extension in exts:
            return cat
    
    return 'unknown'



def sort_dir(root_dir:Path, current_dir:Path):
    
    for item in [f for f in current_dir.glob('*') if  f.name not in CATEGORIES.keys()]:
        if not item.is_dir():
            category = get_categories(item)
            new_path = move_file(item, root_dir, category)
            print(new_path)
        else:
            sort_dir(root_dir, item)
            item.rmdir()



def main ():
    try:
        path = Path(sys.argv[1])
        # return 'all ok'
    except IndexError:
        return f'No path to folder. Take as parameter'
    
    if not path.exists():
        return 'sorry, folder not exist'
    
    sort_dir(path, path)
    
    return 'all ok'



if __name__ == '__main__':
    print(main())