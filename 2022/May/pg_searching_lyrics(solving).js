class Node {
    constructor(key, data = null) {
        this.key = key
        this.data = data
        this.children = {}
    }
}

class Trie {
    constructor() {
        this.head = new Node(null)
    }

    insert(string) {
        let currNode = this.head

        for (const char of string) {
            if (!(char in currNode.children)) {
                currNode.children[char] = new Node(char)
            }

            currNode = currNode.children[char]
        }

        currNode.data = string
    }

    search(string) {
        let currNode = this.head

        for (const char of string) {
            if (char in currNode.children) {
                currNode = currNode.children[char]
            } else if (char === '?') {
                for (const elm in currNode.children) {
                    currNode = currNode.children[elm]
                    // FIXME
                }
            } else {
                return false
            }
        }

        if (currNode.data !== null) {
            return true
        } else {
            return false
        }
    }
}

function solution(words, queries) {
    const answer = []

    // for (const word of words) {
    //     trie.insert(word)
    // }


    for (const query of queries) {
        let answerCnt = 0

        for (const word of words) {
            if (word.length !== query.length) {
                continue
            }
            const trie = new Trie()
            trie.insert(word)
            if (trie.search(query)) {
                answerCnt += 1
            }
        }
        answer.push(answerCnt)
    }

    return answer
}