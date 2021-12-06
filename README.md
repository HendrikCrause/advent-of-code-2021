These are the scripts I used to complete the [adventofcode.com/2021](https://adventofcode.com/2021) challenges/puzzles written in [python](https://python.org). 
Each day's challenge is in its own file named `day<n>.py` under the `src` directory. Data used for each challenge was put in `resources` directory. I've included each day's challenge text as a block comment at the bottom of each script in case the original ever gets lost.

## Setup
Create and activate virtual python environment. Then install requirements.
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Running a day's puzzle
From the root directory, execute:
```bash
python src/day<n>.py
```
Each part's solution should be printed to the console. Example output:
```bash
>>> python src/day1.py
Part 1: 1215
Part 2: 1150
```