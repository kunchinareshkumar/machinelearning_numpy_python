"""Generates lessons/*.md, the notebook, and README.md from one source of truth (topics.py)."""
import io, json, os, contextlib, textwrap
from topics import TOPICS

ROOT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(ROOT, "lessons"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)


def run(code, ns):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, ns)
    return buf.getvalue().rstrip()


ns = {}
nb_cells = []


def md_cell(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(True)}


def code_cell(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": text.splitlines(True)}


nb_cells.append(md_cell(
    "# NumPy: Complete Learning Notebook\n\n"
    "A single notebook covering NumPy from basics to advanced topics, in learning order. "
    "Run the cells top to bottom.\n\n"
    "**Contents**\n\n" + "\n".join(f"{t['n']}. {t['title']}" for t in TOPICS)
))

readme_rows = []
for t in TOPICS:
    out = run(t["code"], ns)
    fname = f"{t['n']:02d}_{t['slug']}.md"
    readme_rows.append(f"| {t['n']:02d} | [{t['title']}](lessons/{fname}) | {t['level']} |")

    ex = "\n".join(f"{i+1}. {e}" for i, e in enumerate(t["exercises"]))
    md = (
        f"# {t['n']:02d}. {t['title']}\n\n"
        f"**Level:** {t['level']}\n\n"
        f"## Definition\n\n{t['definition']}\n\n"
        f"## Explanation\n\n{t['explanation']}\n\n"
        f"## Code\n\n```python\n{t['code'].strip()}\n```\n\n"
        f"## Output\n\n```text\n{out}\n```\n\n"
        f"## Exercises\n\n{ex}\n"
    )
    with open(os.path.join(ROOT, "lessons", fname), "w") as f:
        f.write(md)

    nb_cells.append(md_cell(
        f"---\n## {t['n']}. {t['title']}\n\n**Definition:** {t['definition']}\n\n{t['explanation']}"
    ))
    nb_cells.append(code_cell(t["code"].strip()))
    nb_cells.append(md_cell("**Exercises**\n\n" + ex))

nb = {
    "cells": nb_cells,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
with open(os.path.join(ROOT, "NumPy_Complete_Guide.ipynb"), "w") as f:
    json.dump(nb, f, indent=1)

readme = f"""# NumPy Learning Roadmap

A structured, beginner-to-advanced path through NumPy. Every topic has a definition, explanation,
runnable code with real output, and exercises.

## How to use this repo

1. `pip install -r requirements.txt`
2. Read the lessons in order (`lessons/01_...` to `lessons/{len(TOPICS):02d}_...`), or
3. Open the single notebook: `jupyter notebook NumPy_Complete_Guide.ipynb`

## Roadmap

| # | Topic | Level |
|---|-------|-------|
{chr(10).join(readme_rows)}

## Repo layout

```
numpy-learning-roadmap/
├── README.md
├── requirements.txt
├── NumPy_Complete_Guide.ipynb   # all topics in one notebook
├── lessons/                     # one markdown file per topic
├── data/                        # files created by the I/O lesson
└── build.py, topics.py          # source used to generate the lessons and notebook
```

## Suggested study plan

- Week 1: topics 01-06 (arrays, indexing, reshaping)
- Week 2: topics 07-11 (math, broadcasting, statistics, masking, sorting)
- Week 3: topics 12-16 (linear algebra, random, copies/views, NaN, file I/O)
- Week 4: topics 17-20 (performance, advanced features, projects, cheat sheet)

## Further reading

- Official docs: https://numpy.org/doc/stable/
- NumPy user guide: https://numpy.org/doc/stable/user/index.html
"""
with open(os.path.join(ROOT, "README.md"), "w") as f:
    f.write(readme)
with open(os.path.join(ROOT, "requirements.txt"), "w") as f:
    f.write("numpy\njupyter\n")
print("built", len(TOPICS), "topics")
