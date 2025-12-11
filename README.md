## 🐍 LeetCode Journey: Notebooks & Deep Dives

This repository documents my systematic approach to solving LeetCode problems, organized into manageable sets of **10 problems per Jupyter Notebook**. Each notebook serves as a dedicated study session, featuring not only the final, optimized code but also detailed explanations, complexity analysis, and solution exploration.

-----

### 📚 Repository Structure

The core of this repository is the `notebooks/` directory, which groups the problems sequentially for focused learning and review.

| Folder/File | Description |
| :--- | :--- |
| `notebooks/` | Contains all Jupyter Notebooks (`.ipynb`) where the problems are solved and explained. |
| `notebooks/Set_01_Problems_1_10.ipynb` | Solutions and detailed analysis for LeetCode Problems 1 through 10. |
| `notebooks/Set_02_Problems_11_20.ipynb` | Solutions and detailed analysis for LeetCode Problems 11 through 20. |
| `README.md` | This file. |

### 💡 Notebook Philosophy

Every Jupyter Notebook follows a consistent, structured format to maximize learning retention:

1.  **Problem Statement:** A clear, concise restatement of the LeetCode problem.
2.  **Brute-Force (Initial) Approach:** A demonstration and analysis of the simplest, often least efficient, solution.
3.  **Optimal Algorithm:** The final, accepted solution with the best time complexity.
4.  **Complexity Analysis:** Detailed breakdown of the Time ($O$) and Space ($\Omega$) complexity for both approaches.

[Image of Big O complexity chart]

5.  **Code Implementation:** The clean, runnable Python code.
6.  **Example Usage:** Inline test cases to confirm correctness.

### 🛠️ Technology Stack

  * **Primary Language:** Python 3.x
  * **Environment:** Jupyter Notebook (using the standard Python kernel)
  * **Libraries:** Primarily standard library tools, occasionally `collections` (e.g., `defaultdict` or `deque`) for data structure optimization.

### 🚀 Getting Started with the Notebooks

To explore the solutions and explanations interactively, you will need to set up a Python environment with Jupyter support.

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repository URL]
    cd [Your Repository Name]
    ```
2.  **Install Required Dependencies (Recommended):**
    ```bash
    pip install jupyter pandas numpy
    ```
3.  **Launch Jupyter Lab/Notebook:**
    ```bash
    jupyter notebook
    # OR
    jupyter lab
    ```
4.  Navigate to the `notebooks/` directory and open any `Set_XX_Problems_YY_ZZ.ipynb` file to begin reviewing.

### ⭐ Highlighted Concepts

As the notebooks progress, focus shifts to mastering key algorithmic concepts:

| Concept | Example Notebooks | Essential Techniques Covered |
| :--- | :--- | :--- |
| **Arrays & Hashing** | Set 01, Set 02 | Hash Maps for $O(N)$ lookup, Two Pointers, Sliding Window |
| **Linked Lists** | Set 03, Set 04 | Dummy Nodes, Slow/Fast Pointers (Tortoise and Hare), In-Place Reversal |
| **Dynamic Programming** | Set 05, Set 06 | Memoization (Top-Down), Tabulation (Bottom-Up), State Transitions  |
| **Trees & Graphs** | Set 07, Set 08 | Depth-First Search (DFS), Breadth-First Search (BFS), Recursive Traversal |

-----

### 🤝 Contribution & Feedback

While this is a personal learning log, feel free to use the code and explanations for your own studies. If you spot a critical error or a significant optimization opportunity, please open an issue or submit a pull request\!