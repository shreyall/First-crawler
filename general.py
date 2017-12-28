import os
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating prtoject' + directory)
        os.makedirs(directory)

 # create_project_dir('First Project!')
def create_data_files(projectname, baseurl):
    queue=projectname + '/queue.txt' 
    crawled = projectname + '/crawled.txt'
    #if cue file exists, dont create, vice versa
    # it cannot be empty cuz it will not know where to start
    if not os.path.isfile(queue):
        write_file(queue, baseurl)
    if not os.path.isfile(crawled):
        write_file(crawled, ' ')

## create a new file
def write_file(path,data):
    f=open(path, 'w')
    f.write(data)
    f.close()





