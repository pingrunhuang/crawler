from urllib.request import urlopen
from bs4 import BeautifulSoup

import nltk

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message


def getSubLinks(fromPageId):
    cur.execute()

def constructDict(currentPageId):
    links = getSubLinks(currentPageId)
    if links:
        # this one statement return a dict like this:
        # {'link1':[], 'link2':[], 'link3':[],...}
        return dict(zip(links, [{}]*len(links)))
    else:
        return {}

def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        # stop condition
        return linkTree

    if not linkTree:
        linkTree=constructDict(currentPageId)
        if not linkTree:
            # means there is no sub links inside this page
            return {}
    
    if targetPageId in linkTree.keys():
        # means the target page is found
        print("Target "+str(targetPageId)+" found!")
        raise SolutionFound("Page: "+str(currentPageId))

    # iterate through the whole current page
    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey]=searchDepth(
                targetPageId, branchKey, branchValue, depth-1
            )
        except SolutionFound as e:
            print(e.message)
            # in each iteration, this raise make sure the path get printed
            raise SolutionFound("Page: "+str(currentPageId))

if __name__=='__main__':
    startPageId = '1'
    targetPageId = '1321'
    depth=4
    try:
        searchDepth(targetPageId, startPageId, {}, depth)
        print('No solution found')
    except SolutionFound as e:
        print(e.message)
