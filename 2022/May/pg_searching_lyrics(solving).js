class Node {
    constructor(key, data = null) {
        this.key = key;
        this.data = data;
        this.children = {};
        this.cnt = 0;
    }
}

class Trie {
    constructor() {
        this.head = new Node(null);
    }

    insert(string) {
        let currNode = this.head;

        for (let i = 0; i < string.length; i++) {
            const char = string[i];
            if (!(char in currNode.children)) {
                currNode.children[char] = new Node(char);
            }

            currNode.cnt += 1;
            currNode = currNode.children[char];
        }

        // currNode.data = string
    }

    search(string) {
        let currNode = this.head;

        for (let i = 0; i < string.length; i++) {
            const char = string[i];
            if (char in currNode.children) {
                currNode = currNode.children[char];
            } else if (char === "?") {
                return currNode.cnt
            } else {
                return 0;
            }
        }

    }
}

function solution(words, queries) {
    const answer = [];

    const trieObj = {};


    for (const word of words) {
        const len = word.length;
        if (!(len in trieObj)) {
            trieObj[len] = [new Trie(), new Trie()]
        }
        trieObj[len][0].insert(word);
        trieObj[len][1].insert(word.split("").reverse().join(""));
    }

    for (let query of queries) {
        try{
            if (query[0] === "?") {
                query = query.split("").reverse().join("");
                answer.push(trieObj[query.length][1].search(query));
            } else {
                answer.push(trieObj[query.length][0].search(query));
            }
        } catch {
            answer.push(0)
        }
    }

    return answer;
}

const words = ["frodo", "front", "frost", "frozen", "frame", "kakao"];
const queries = ["fro??", "????o", "fr???", "fro???", "pro?"];
const answer = [3, 2, 4, 1, 0];

console.log(solution(words, queries) === answer);