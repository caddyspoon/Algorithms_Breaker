// class Node {
//   constructor(key, data = null) {
//     this.key = key;
//     this.data = data;
//     this.children = {};
//   }
// }

// class Trie {
//   constructor() {
//     this.head = new Node(null);
//   }

//   insert(string) {
//     let currNode = this.head;

//     for (const char of string) {
//       if (!(char in currNode.children)) {
//         currNode.children[char] = new Node(char);
//       }

//       currNode = currNode.children[char];
//     }

//     currNode.data = string;
//   }

//   search(string) {
//     let currNode = this.head;

//     for (const char of string) {
//       if (char in currNode.children) {
//         currNode = currNode.children[char];
//       } else {
//         return false;
//       }
//     }

//     if (currNode.data === string) {
//       return true;
//     } else {
//       return false;
//     }
//   }
// }


// const trie = Trie();
// const stringArr = ['apple', 'appolo', 'apptite', 'appstore', 'appdulla'];

// for (const string in stringArr) {
//   trie.insert(string);
// }
  
// console.log('apple: ', trie.search('apple'));
// console.log('appgujeong: ', trie.search('apgujeong'));


const Node = function(key, data = null) {
  this.key = key;
  this.data = data;
  this.children = {};
}

const Trie = function() {
  this.head = new Node(null);

  this.insert = function(string) {
    let currNode = this.head;

    for (const char of string) {
      if (!(char in currNode.children)) {
        currNode.children[char] = new Node(char);
      }
    
      currNode = currNode.children[char];
    }
    
    currNode.data = string;
  }

  this.search = function(string) {
    let currNode = this.head;

    for (const char of string) {
      if (char in currNode.children) {
        currNode = currNode.children[char];
      } else {
        return false;
      }
    }

    if (currNode.data === string) {
      return true;
    } else {
      return false;
    }
  }
}

const trie = new Trie();
const stringArr = ['apple', 'appolo', 'apptite', 'appstore', 'appdulla'];

stringArr.forEach(string => {
  trie.insert(string);
})
  
console.log('apple: ', trie.search('apple'));
console.log('apple: ', trie.search('appolo'));
console.log('appgujeong: ', trie.search('apgujeong'));
