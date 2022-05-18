class Node:
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head

        # print('string: ', string)
        for char in string:
            # print('char: ', char)
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
                # print('new char: ', char)
            
            curr_node = curr_node.children[char]
            # print('currNode: ', curr_node)
            # print()
        # print('curr_node.key: ', curr_node.key)
        

        curr_node.data = string
        # print('curr_node.data: ', curr_node.data)

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            
            else:
                return False
        
        if curr_node.data != None:

            return True
        else:
            return False

trie = Trie()
strings = ['apple', 'appolo', 'apptite', 'appstore', 'appdulla']

for string in strings:
    trie.insert(string)

print('apple: ', trie.search('apple'))

print('appgujeong: ', trie.search('appgujeong'))

