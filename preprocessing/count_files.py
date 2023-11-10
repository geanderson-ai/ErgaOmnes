import os

def count_files_in_folder(folder_path):
    try:
        # Get the list of files in the folder
        files = os.listdir(folder_path)

        # Count the number of files
        file_count = len(files)

        print(f'The number of files in the folder "{folder_path}" is: {file_count}')

    except FileNotFoundError:
        print(f'The specified folder "{folder_path}" does not exist.')

# Example usage
folder_path = '/Users/geandersonlenz/Documents/BorealAI/erga-omnes/output_files2'
count_files_in_folder(folder_path)
