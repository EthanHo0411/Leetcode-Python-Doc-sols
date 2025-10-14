"""
LeetCode Repository Structure Setup Script
Creates a simple topic-organized structure for LeetCode problems and solutions
"""

import os
from datetime import datetime

# Define topics based on LeetCode patterns
TOPICS = [
    "arrays-hashing", "two-pointers", "stack", "binary-search",
    "sliding-window", "linked-list", "trees", "tries",
    "heap-priority-queue", "backtracking", "intervals", "greedy",
    "graphs", "advanced-graphs", "1d-dp", "2d-dp",
    "bit-manipulation", "math-geometry"
]

def create_directories():
    """Create main directory structure"""
    print("🚀 Setting up LeetCode Solutions Repository Structure...")
    
    os.makedirs("docs", exist_ok=True)
    
    for topic in TOPICS:
        os.makedirs(f"problems/{topic}", exist_ok=True)
    
    print("✅ Directories created!")

def create_readme():
    """Create main README.md"""
    date = datetime.now().strftime("%B %d, %Y")
    
    readme_content = f"""# LeetCode Solutions

A collection of my LeetCode problem solutions in Python, organized by topic and pattern.

## 📊 Progress

![Problems Solved](https://img.shields.io/badge/solved-0-brightgreen)

## 📁 Repository Structure

```
.
├── problems/              # Problems organized by topic
│   ├── arrays-hashing/
│   │   ├── 1-two-sum.md
│   │   └── 1-two-sum.py
│   ├── two-pointers/
│   ├── stack/
│   └── ...
└── docs/                  # Additional documentation
```

## 🗂️ Problems by Topic

### Arrays & Hashing
<!-- Problems will be listed here -->

### Two Pointers
<!-- Problems will be listed here -->

### Stack
<!-- Problems will be listed here -->

### Binary Search
<!-- Problems will be listed here -->

### Sliding Window
<!-- Problems will be listed here -->

### Linked List
<!-- Problems will be listed here -->

### Trees
<!-- Problems will be listed here -->

### Tries
<!-- Problems will be listed here -->

### Heap / Priority Queue
<!-- Problems will be listed here -->

### Backtracking
<!-- Problems will be listed here -->

### Intervals
<!-- Problems will be listed here -->

### Greedy
<!-- Problems will be listed here -->

### Graphs
<!-- Problems will be listed here -->

### Advanced Graphs
<!-- Problems will be listed here -->

### 1-D Dynamic Programming
<!-- Problems will be listed here -->

### 2-D Dynamic Programming
<!-- Problems will be listed here -->

### Bit Manipulation
<!-- Problems will be listed here -->

### Math & Geometry
<!-- Problems will be listed here -->

## 🛠️ Language

All solutions are written in **Python 3**

## 📖 How to Use

Each problem includes:
- Problem description in markdown (.md file)
- Python solution (.py file)
- Time and space complexity analysis
- Explanation of approach

---

Last Updated: {date}
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✅ README.md created!")

def create_add_problem_script():
    """Create helper script for adding problems"""
    script_content = """\"\"\"
Add a new LeetCode problem to the repository
Usage: python add_problem.py <problem_number> <topic> <problem_name> [difficulty]
Example: python add_problem.py 1 arrays-hashing two-sum easy
\"\"\"

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
        difficulty_line = f"**Difficulty:** {difficulty.capitalize()}\\\\n\\\\n"
    
    # Create problem markdown file
    md_filename = f"problems/{topic}/{problem_number}-{problem_name}.md"
    problem_markdown = f\"\"\"# {problem_number}. {problem_title}

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
\"\"\"
    
    with open(md_filename, "w", encoding="utf-8") as f:
        f.write(problem_markdown)
    
    # Create Python solution file
    py_filename = f"problems/{topic}/{problem_number}-{problem_name}.py"
    python_solution = f\\\"\\\"\\\"\\\"\\\"\\\"
LeetCode Problem {problem_number}: {problem_name}
Topic: {topic}

Solution approach:
TODO: Add description

Time Complexity: O(?)
Space Complexity: O(?)
\\\"\\\"\\\"

class Solution:
    def solve(self):
        \\\"\\\"\\\"
        TODO: Implement solution
        \\\"\\\"\\\"
        pass


def main():
    solution = Solution()
    
    # Test case 1
    # result = solution.solve()
    # print(f"Test 1: {result}")
    
    pass


if __name__ == "__main__":
    main()
\\\"\\\"\\\"
    
    with open(py_filename, "w", encoding="utf-8") as f:
        f.write(python_solution)
    
    print(f"✅ Problem {problem_number} ({problem_name}) added successfully!")
    print(f"📁 Topic: {topic_display}")
    print(f"📝 Markdown: {md_filename}")
    print(f"💻 Solution: {py_filename}")

if __name__ == "__main__":
    main()
"""
    
    with open("add_problem.py", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    print("✅ add_problem.py created!")

def create_gitignore():
    """Create .gitignore file"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*.class
*.so
.Python
env/
venv/
ENV/

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db
"""
    
    with open(".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    
    print("✅ .gitignore created!")

def create_topics_guide():
    """Create topics reference guide"""
    topics_content = """# LeetCode Topics & Patterns

This repository organizes problems based on common LeetCode patterns and topics.

## Topic Hierarchy

### Foundation
1. **Arrays & Hashing** - Hash maps, sets, array manipulation
2. **Two Pointers** - Fast/slow pointers, opposite ends
3. **Stack** - LIFO operations, monotonic stacks
4. **Binary Search** - Sorted array search, search space reduction
5. **Sliding Window** - Subarray/substring problems
6. **Linked List** - Pointer manipulation, reversal

### Intermediate
7. **Trees** - Binary trees, BST, tree traversal
8. **Tries** - Prefix trees, autocomplete
9. **Heap / Priority Queue** - K-th element, merge K sorted
10. **Backtracking** - Permutations, combinations, subsets
11. **Intervals** - Merge intervals, scheduling
12. **Greedy** - Locally optimal choices

### Advanced
13. **Graphs** - BFS, DFS, topological sort
14. **Advanced Graphs** - Dijkstra, union find, MST
15. **1-D DP** - Linear dynamic programming
16. **2-D DP** - Grid-based dynamic programming
17. **Bit Manipulation** - XOR tricks, bit masking
18. **Math & Geometry** - Mathematical formulas, coordinate geometry

## Common Patterns

- **Fast & Slow Pointers** (Linked List)
- **Sliding Window** (Arrays)
- **Two Heaps** (Heap / Priority Queue)
- **Top K Elements** (Heap / Priority Queue)
- **Merge Intervals** (Intervals)
- **Cyclic Sort** (Arrays & Hashing)
- **In-place Reversal** (Linked List)
- **Tree BFS/DFS** (Trees)
- **Graph Traversal** (Graphs)
- **Subset/Permutation** (Backtracking)
- **Modified Binary Search** (Binary Search)
- **Knapsack** (1-D DP / 2-D DP)
"""
    
    with open("docs/TOPICS.md", "w", encoding="utf-8") as f:
        f.write(topics_content)
    
    print("✅ docs/TOPICS.md created!")

def main():
    create_directories()
    create_readme()
    create_add_problem_script()
    create_gitignore()
    create_topics_guide()
    
    print("\n" + "="*60)
    print("✅ Repository structure created successfully!")
    print("="*60)
    print("\n📂 Structure:")
    print("  problems/      # Problem markdown + Python solutions")
    print("  docs/          # Documentation")
    
    print("\n🎯 Next steps:")
    print("1. Initialize git: git init")
    print("2. Add a problem: python add_problem.py 1 arrays-hashing two-sum easy")
    print("3. Start solving problems!")
    
    print("\n💡 Available topics:")
    print("   arrays-hashing, two-pointers, stack, binary-search, sliding-window,")
    print("   linked-list, trees, tries, heap-priority-queue, backtracking,")
    print("   intervals, greedy, graphs, advanced-graphs, 1d-dp, 2d-dp,")
    print("   bit-manipulation, math-geometry")
    
    print("\nHappy coding! 🚀\n")

if __name__ == "__main__":
    main()