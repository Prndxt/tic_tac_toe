# Program Design

Before you write any code, we need to plan our program. Programming is mostly about turning an idea into precise steps. Consider your computer being someone unfamiliar with programming at all. Explaining the problem and building a solution is easier when done stepwise. Typing the executable code is only the last part although you might easily be tempted to start coding right ahead.

We use four simple steps:

```
1. What should the program do?  →  2. Formulate pseudocode  →  3. Write skeleton code  →  4. Executable python code
                ↑                                                              |
                └──────────────── test, find problems, improve ────────────────┘
```

You will probably go back and forth between the steps several times until you are satisfied. That is normal.

---

## Step 1: What should the program do?

Write down, in plain words, what your finished program must be able to do. Use the assignment as your starting point and phrase each point so you can tick it off later.

This list is your checklist at the end.

> Tip: Keep it simple. Extra features and enhancements can be introduced later.

---

## Step 2: Pseudocode

Describe the flow of your program step by step in your own words, without worrying about Python syntax. Pseudocode helps you think through the logic: the loops, the decisions, and which information (variables) you need to keep track of.

How to write good pseudocode is explained in [Introduction to Pseudocode](03_intro_to_pseudocode.md).

> Alternative: If you think more visually, you can draw the flow as a **flowchart** instead of (or in addition to) pseudocode. Boxes are steps, diamonds are decisions.

---

## Step 3: Skeleton code

Now translate the big blocks of your pseudocode into **functions**, but leave them empty for now. This shows you if your planned structure makes sense before you write the details.

A skeleton looks like this:

```python
def first_function():
    pass

def second_function():
    pass

def main():
    pass

main()
```

`pass` is a valid python command and means "do nothing yet". The skeleton should already run without errors, even though it does nothing useful.

Ask yourself:

- Does every part of my pseudocode belong to one of my functions?
- Which information does each function need (parameters) and give back (return value)?

---

## Step 4: Code

Fill in the functions one by one. After each function, **test it** before moving on. Small steps lets you find errors much easier.

When everything works, go back to your checklist from Step 1 and tick off each point.

---

## Further reading (optional)

In larger software projects you will meet more planning tools, for example requirements documents, user stories, class diagrams or prototypes. You don't need them for this exercise.

- [Flowchart (Wikipedia)](https://en.wikipedia.org/wiki/Flowchart)
- [User Stories (Atlassian)](https://www.atlassian.com/agile/project-management/user-stories)
- [Class Diagram (Wikipedia)](https://en.wikipedia.org/wiki/Class_diagram)