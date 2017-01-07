#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import os


def get_dir_from_terminal():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory_path", help="Initial directory location", type=str)
    args = parser.parse_args()
    return args.directory_path

def output_duplicates_to_terminal(duplicates):
    num_of_duplicates = len(duplicates)
    print("Found {} duplicate(s)!".format(num_of_duplicates))
    for i, (file_name, file_size) in enumerate(duplicates, start=1):
        print("{}) File name: {}\nAppearances:".format(i, file_name))
        for appearance in duplicates[(file_name, file_size)]:
            print(" • {}".format(appearance))

def get_all_files(directory):
    all_files = {}
    for rootdir, dirs, file_names, in os.walk(directory):
        for file_name in file_names:
            path_to_current_file = os.path.join(rootdir, file_name)
            file_size = os.path.getsize(path_to_current_file)
            file_data = (file_name, file_size)
            if file_data not in all_files:
                all_files[file_data] = []
            all_files[file_data].append(path_to_current_file)
    return all_files

def get_duplicates(files):
    duplicates = {}
    for file_data in files:
        file_appearances = files[file_data]
        if len(file_appearances) > 1:
            duplicates[file_data] = file_appearances
    return duplicates
    

def main():
    directory = get_dir_from_terminal()
    if os.path.isdir(directory):
        files = get_all_files(directory)
        duplicates = get_duplicates(files)
        output_duplicates_to_terminal(duplicates)
    else:
        print("Incorrect directory.")

if __name__ == '__main__':
    main()

