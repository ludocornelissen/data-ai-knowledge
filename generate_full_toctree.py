import yaml
from typing import List, Dict, Union


def generate_full_toctree(toc_file: str = "_toc.yml", depth: int = 2) -> dict:
    """
    Generate a full table of contents from the toc definition in the source file.
    """
    with open(toc_file, "r") as f:
        toc_config = yaml.safe_load(f)
    
    toctree: List[Dict] = []

    for part in toc_config['parts']:
        part_title = part["caption"]
        part_dict = {part_title: []}
        
        for chapter in part["chapters"]:
            chapter_dict = {}
            chapter_path = chapter["file"]
            with open(chapter_path, "r") as f:
                for line in f.readlines():
                    start_hashes = line.count("#", 0, 5) # Max depth is 5
                    section_idx = -1
                    if start_hashes == 1 and depth > 0:
                        chapter_title = line.strip("#").strip()
                        chapter_dict[chapter_title] = []
                    elif start_hashes == 2 and depth > 1:
                        section_idx += 1
                        section_title = line.strip("##").strip()
                        chapter_dict[chapter_title].append(section_title)
                    else:
                        pass
            part_dict[part_title].append(chapter_dict)

        toctree.append(part_dict)
    return toctree


def pretty_print_toctree(
        toctree: Union[List[Dict], Dict], 
        level: int = 0, 
        last_in_super_list: bool = False, 
        file_to_write = None
    ):
    """Print the table of contents in a unix directory tree-like format."""

    space =  '    '
    branch = '│   '
    tee =    '├── '
    last =   '└── '

    if isinstance(toctree, list):
        for index, item in enumerate(toctree):
            is_last_in_list = index == len(toctree) - 1
            if isinstance(item, str):
                print(
                    space,
                    branch if not last_in_super_list else space,
                    space * (level - 3),
                    tee if level and not is_last_in_list else last,
                    item,
                    sep="",
                    file=file_to_write
                )
            else:
                pretty_print_toctree(item, level=level+1, last_in_super_list=is_last_in_list, file_to_write=file_to_write)
    elif isinstance(toctree, dict):
        for key, value in toctree.items():
            print(
                    space * (level - 2),
                    tee if level > 1 and not last_in_super_list else "",
                    last if level > 1 and last_in_super_list else "",
                    key,
                    sep="",
                    file=file_to_write
                )    
            pretty_print_toctree(value, level + 1, last_in_super_list=last_in_super_list, file_to_write=file_to_write)
    else:
        return

if __name__ == "__main__":
    toctree = generate_full_toctree()
    pretty_print_toctree(toctree)
