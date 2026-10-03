"""
Alien Dictionary
There is a new alien language that uses the English alphabet, but the order of the letters is unknown.

You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.

Example 1:

Input: words = ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".


Example 2:

Input: words = ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know 'r' < 'n'
from "enn" and "rfnn" we know 'e' < 'r'
so one possible solution is "hernf"

Example 3:

Input: words = ["abc","ab"]

Output: ""
Explanation:
The second word is a prefix of the first word, but the first word appears before the second. This is impossible in a valid lexicographical ordering, so return "".
"""

from collections import defaultdict, deque


def foreign_dictionary(words: list[str]) -> str:
    if not words:
        return ""  # No data

    length = len(words)
    if length == 1:
        return words[0]

    graph = defaultdict(list[str])  # Graph for the letters we find
    full_chars: set[str] = set()
    indegree = defaultdict(int)  # In- Degree for every node
    for right in range(1, length):
        word_a = words[right - 1]
        word_b = words[right]
        for i in word_a:
            full_chars.add(i)
        for i in word_b:
            full_chars.add(i)

        if len(word_a) != len(word_b) and word_b in word_a:
            return ""  # Second word is prefix of previous one

        i = 0
        while i < len(word_a) and i < len(word_b) and word_a[i] == word_b[i]:
            i += 1
        # Here we have the different char, so we can create a dependency
        char_a = word_a[i] if i < len(word_a) else None
        char_b = word_b[i] if i < len(word_b) else None
        if char_a and char_b and char_a != char_b:
            graph[char_a].append(char_b)
            indegree[char_b] += 1
            indegree[char_a] = indegree[char_a] if indegree[char_a] else 0
    # Now let’s run the kahnn algorithm to find the dependency
    order: list[str] = []
    queue: list[str] = deque([node for node, deg in indegree.items() if deg == 0])
    while queue:
        top = queue.popleft()
        order.append(top)

        # Update and check nighbors
        for neighbour in graph[top]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    # Check for cycle,
    if len(order) != len(graph):
        return ""  # Cycle here, lol
    for c in order:
        full_chars.remove(c)

    return "".join(order + list(full_chars))


if __name__ == "__main__":
    print(f"Result for {['z','o']}: {foreign_dictionary(['z','o'])}")
    print(
        f"Result for {['hrn','hrf','er','enn','rfnn']}: {foreign_dictionary(['hrn','hrf','er','enn','rfnn'])}"
    )
    print(f"Result for {['abc','ab']}: {foreign_dictionary(['abc','ab'])}")
