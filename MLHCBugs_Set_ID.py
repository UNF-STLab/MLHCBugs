#!/usr/bin/env python
#MLHC Bugs testing file.

import os
import argparse
import json

def get_commit_id(repo_name:str):

    commit_id_file = open('Repos/' + repo_name + '/.git/head', 'r')
    commit_id = commit_id_file.read()

def set_id_run_bug(bug_id:str , repo_name:str, commit_id:str):

    current_commit_id = get_commit_id(repo_name)

    if current_commit_id != commit_id:
        os.system('cd Repos/' + repo_name + '; git checkout ' + commit_id)

    os.system('./BugRuns/bug_id_' + bug_id + '.sh')
        
def main():

    # Arguments vector (argv)
    parser = argparse.ArgumentParser(description='Test bugs based on ID')

    parser.add_argument('bug_ids', metavar='B', type=str, nargs='+',
                        help='Bugs to be tested.')

    args = parser.parse_args()

    bug_ids = args.bug_ids

    if bug_ids[0] == 'ALL':
        bug_ids = [str(n+1) for n in range(30)]

    # Load all repos in to map and associate the init function.
    with open('commit_id.json') as json_file:
        bug_dictionary = json.load(json_file)

    bugs = bug_dictionary.keys()

    # Process all args and call the function to init the desired repos.
    for bug_id in bug_ids:
        set_id_run_bug(bug_id, bug_dictionary[bug_id][0], bug_dictionary[bug_id][1])
    
if __name__ == '__main__':

    main()
