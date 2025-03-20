# Probability of winning in a mathematically perfect Volley Tournament

## Problem

There are two teams: X, Y. They play a series of rallies each one is worth one point.
They play until one team wins N points (e.g. 100).

In the first rally X is serving. The one who serves inherently has an advantage.
The team X has a probability of P winning a rally if it serves (e.g. 99%).
The team Y has a probability of Q winning a rally if it serves (e.g. 98%).

There are two possible rules for serving:
- winner of the point serves next.
- they alternate serving.

Calculate the probability that X wins in for each rule.

## Usage

Symbolic calculations:
```
$ python calculate_symbolic.py
```

Numeric calculations:
```
$ python calculate_numeric.py
```

Plot:
```
$ python volley_plot.py
```

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


Record interactions with claude:
```
$ script -T ../fantasy.time -a ../fantasy.script
$ . .venv/bin/activate
$ claude
```

Replay interactions:
```
$ scriptreplay -T ../fantasy.time ../fantasy.script --maxdelay 1
```

After setting up the environment, you can run the example script:
```
$ . .venv/bin/activate
python main.py
```
