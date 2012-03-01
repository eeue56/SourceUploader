import requests

from json import dumps, loads

BASE_URL = 'https://api.github.com/'

def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data


def get_files_data(filenames):
    files = {}
    
    for filename in filenames:
        files[filename] = read_file(filename)

    return files

def convert_to_github_data(files):
    new_files = {}
    
    for filename, content in files.iteritems():
        new_files[filename] =  { 'content' : content }

    return new_files

def upload_to_github(filenames):

    payload = {'description' : 'inital commit',
               'public' : 'false',
               'files' : convert_to_github_data(get_files_data(filenames))
               }

    req = requests.post(BASE_URL + 'gists', data=dumps(payload))

    return req

def print_github_response(response):
    data = loads(response.content)

    for file_ in data['files']:
        print '{file} is at {raw_url}'.format(file=file_, raw_url=data['files'][file_]['raw_url'])

    print '\n\ngist located at {url}'.format(url=data['html_url']) 

if __name__ == '__main__':
    durp = upload_to_github(['test.txt'])
    print_github_response(durp)

        
