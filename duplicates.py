import argparse
import os


def get_dir_from_terminal():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory_path", help="Initial directory location", type=str)
    args = parser.parse_args()
    return args.directory_path

def output_duplicates_to_terminal(duplicates):
    num_of_duplicates = len(duplicates)
    print("Found %i duplicate(s)!" % num_of_duplicates)
    for num, duplicate in zip(range(1, num_of_duplicates + 1), duplicates):
        print("%i) File name: %s\nAppearances:" % (num, duplicate))
        for appearance in duplicates[duplicate]:
            print(" • %s" % appearance)

def are_files_duplicates(file_path_1, file_path_2):
    return os.path.basename(file_path_1) == os.path.basename(file_path_2)\
     and os.path.getsize(file_path_1) == os.path.getsize(file_path_2)

def get_duplicates(directory):
    found_files = set()
    duplicates = {}
    for rootdir, dirs, file_names in os.walk(directory):
        for file_name in file_names:
            path_to_current_file = os.path.join(rootdir, file_name)
            for path_to_found_file in found_files:
                if are_files_duplicates(path_to_current_file, path_to_found_file):
                    if file_name not in duplicates:
                        duplicates[file_name] = set()
                    duplicates[file_name].update({
                        path_to_found_file, 
                        path_to_current_file
                        })
            found_files.add(path_to_current_file)
    return duplicates


if __name__ == '__main__':
    directory = get_dir_from_terminal()
    if os.path.isdir(directory):
        duplicates = get_duplicates(directory)
        output_duplicates_to_terminal(duplicates)
    else:
        print("Incorrect directory.")

