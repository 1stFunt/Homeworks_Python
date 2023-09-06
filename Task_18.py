import os
import json
import csv
import pickle


def collect_directory_info(directory_path):
    def get_directory_size(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
        return total_size

    result = []

    for dirpath, dirnames, filenames in os.walk(directory_path):
        for dirname in dirnames:
            dir_info = {
                "name": dirname,
                "type": "directory",
                "size": get_directory_size(os.path.join(dirpath, dirname)),
                "parent_directory": dirpath
            }
            result.append(dir_info)

        for filename in filenames:
            file_info = {
                "name": filename,
                "type": "file",
                "size": os.path.getsize(os.path.join(dirpath, filename)),
                "parent_directory": dirpath
            }
            result.append(file_info)

    # JSON
    with open('directory_info.json', 'w') as json_file:
        json.dump(result, json_file)

    # CSV
    with open('directory_info.csv', 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(
            csv_file, fieldnames=["name", "type", "size", "parent_directory"])
        csv_writer.writeheader()
        csv_writer.writerows(result)

    # Pickle
    with open('directory_info.pickle', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)


directory_path = "Task_18"
collect_directory_info(directory_path)