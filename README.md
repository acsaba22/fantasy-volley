# Probability of winning in a mathematically perfect Volley Tournament

## Problem

There are two teams: X, Y. They play a series of rallies each one is worth one point.
They play until one team wins N points (e.g. 100).

In the first rally X is serving. The one who serves inherently has an advantage.
The team X has a probability of P winning a rally if it serves (e.g. 99%).
The team Y has a probability of Q winning a rally if it serves (e.g. 98%).

In the first example they alternate serving.

Calculate the probability that X wins.

## Setup and Installation

### Prerequisites
- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) - Python package installer and environment manager

### Setting up the environment
1. Clone the repository
   ```
   git clone <repository-url>
   cd fantasy-volley
   ```

2. Create a virtual environment
   ```
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the project and its dependencies
   ```
   uv pip install -e .
   ```

## Running the example
After setting up the environment, you can run the example script:
```
python hello.py
```

This will demonstrate polynomial multiplication using SymPy.