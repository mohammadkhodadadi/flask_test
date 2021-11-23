import requests


def send_requests_by_file(dir_path):
    import os
    prefix_path, _, filenames = next(os.walk(dir_path))

    abs_paths = []
    for file_name in filenames:
        prefix_path = os.path.abspath(prefix_path)
        abs_paths.append(os.path.join(prefix_path, file_name))

    return abs_paths
