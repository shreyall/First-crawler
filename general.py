import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.makedirs(directory)

####create_project_dir('project')

def create_data_files(projectname, baseurl):
    queue=projectname + '/queue.txt' 
    crawled = projectname + '/crawled.txt'
    #if cue file exists, dont create, vice versa
    # it cannot be empty cuz it will not know where to start
    if not os.path.isfile(queue):
        write_file(queue, baseurl)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
create_data_files('project', 'https://typicalmitul.com')

## add data onto an existing file
## call whenever you want to add a new link to the end of the file
def append_to_file(path, data):
    with open(path, 'a') as file:   # a means append
        file.write(data + '\n')

# Delete the contents of the file
def delete_file_contents(path):
    with open(path, 'w'):
        pass 

## Store contents as a 'set' cuz we dont want duplication 

# Read a file and convert each line to set items 
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))

# Iterate through each set, each item will be a new line in the file 
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)


