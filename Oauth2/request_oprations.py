import requests
import json
import os


def send_requests_by_file(dir_path):

    def _find_all_files(dir_path):
        prefix_path, _, filenames = next(os.walk(dir_path))
        abs_paths = []
        for file_name in filenames:
            prefix_path = os.path.abspath(prefix_path)
            abs_paths.append(os.path.join(prefix_path, file_name))
        return abs_paths

    # Read files and convert to dictionary format.
    def _read_files(file_paths_list):
        file_paths_list.sort(file_paths_list, key=lambda x: int(x[0]))
        output = []
        for path in file_paths_list:
            with open(path, "r") as f:
                output.append(json.load(f))
        return output

    def do_request(content):
        requests
    abs_file_paths = _find_all_files(dir_path=dir_path)
    content_files_list = _read_files(abs_file_paths)
