"""
Add a new LeetCode problem to the repository
Usage: python add_problem.py <problem_number> <topic> <problem_name> [difficulty]
Example: python add_problem.py 1 arrays-hashing two-sum easy
"""

import os
import sys

VALID_TOPICS = [
    'arrays-hashing', 'two-pointers', 'stack', 'binary-search',
    'sliding-window', 'linked-list', 'trees', 'tries',
    'heap-priority-queue', 'backtracking', 'intervals', 'greedy',
    'graphs', 'advanced-graphs', '1d-dp', '2d-dp',
    'bit-manipulation', 'math-geometry'
]

def main():
    if len(sys.argv) < 4:
        print("Usage: python add_problem.py <problem_number> <topic> <problem_name> [difficulty]")
        print("Example: python add_problem.py 1 arrays-hashing two-sum easy")
        sys.exit(1)
    
    problem_number = sys.argv[1]
    topic = sys.argv[2]
    problem_name = sys.argv[3]
    difficulty = sys.argv[4] if len(sys.argv) > 4 else ""
    
    if topic not in VALID_TOPICS:
        print(f"Error: Invalid topic '{topic}'")
        print("Valid topics are:")
        for t in VALID_TOPICS:
            print(f"  - {t}")
        sys.exit(1)
    
    if difficulty and difficulty not in ['easy', 'medium', 'hard']:
        print("Error: Difficulty must be 'easy', 'medium', or 'hard'")
        sys.exit(1)
    
    # Convert names to title case
    problem_title = ' '.join(word.capitalize() for word in problem_name.split('-'))
    topic_display = ' '.join(word.capitalize() for word in topic.split('-'))
    
    difficulty_line = ""
    if difficulty:
        difficulty_line = f"**Difficulty:** {difficulty.capitalize()}\\n\\n"
    
    # Create problem markdown file
    md_filename = f"problems/{topic}/{problem_number}-{problem_name}.md"
    problem_markdown = f"""# {problem_number}. {problem_title}

{difficulty_line}**Topic:** {topic_display}

## Problem Description

[Link to LeetCode Problem](https://leetcode.com/problems/{problem_name}/)

<!-- Add problem description here -->

## Solution

### Approach

<!-- Explain your approach here -->

### Complexity Analysis

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

## Code

See: [{problem_number}-{problem_name}.py](./{problem_number}-{problem_name}.py)
"""
    
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(problem_markdown)
    
    # Create Python solution file
    py_filename = f"problems/{topic}/{problem_number}-{problem_name}.py"
    python_solution = f\"\"\"\"\"\"
LeetCode Problem {problem_number}: {problem_name}
Topic: {topic}

Solution approach:
TODO: Add description

Time Complexity: O(?)
Space Complexity: O(?)
\"\"\"

class Solution:
    def solve(self):
        \"\"\"
        TODO: Implement solution
        \"\"\"
        pass


def main():
    solution = Solution()
    
    # Test case 1
    # result = solution.solve()
    # print(f"Test 1: {result}")
    
    pass


if __name__ == "__main__":
    main()
\"\"\"
    
    with open(py_filename, "w", encoding="utf-8") as f:
        f.write(python_solution)
    
    print(f"✅ Problem {problem_number} ({problem_name}) added successfully!")
    print(f"📁 Topic: {topic_display}")
    print(f"📝 Markdown: {md_filename}")
    print(f"💻 Solution: {py_filename}")

if __name__ == "__main__":
    main()
