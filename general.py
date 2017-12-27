import os
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating prtoject' + directory)
        os.makedirs(directory)

create_project_dir('First Project!')

