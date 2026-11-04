#  PentaByte — Detailed Learning Content (Version 3.0)

## Algorithms, Data Structures, and Connectionist AI

### A Beginner's Guide to Learning Through Problems

**Unit V:** Integration and Practical Project  
**Chapters:** 17–18  
**Team:** PentaByte  
**Source:** *Focused Project Content Outline* (25 October 2026), provided by the team  
**Audience:** Beginning university students with little or no programming experience  
**Demonstration language:** Python 3, using scikit-learn  
**Document type:** Expanded lesson draft for Markdown V2.0, the study guide, PPT, and tutorial videos  
**Status:** Draft for team review; code outputs must be checked in each delivery environment

---

# Unit V — Integration and Practical Project

## Unit introduction

In Units I and II, we turned everyday problems into instructions, wrote Python programs, selected useful data structures, and practiced searching and sorting. Units III and IV introduced connected artificial neurons, explained how their outputs become predictions, and trained and evaluated a small Iris flower classifier.

This final unit answers a new question: **How do all three parts—data structures, algorithms, and connectionist AI—work together in one useful workflow?**

The answer is a single guided notebook called **Flower Prediction Explorer**. It reuses the *same Iris dataset and small multilayer perceptron (MLP) classifier from Units III–IV*. We will organize the classifier's held-out predictions as records, find one record by ID, sort the records by a flower measurement, and explain a prediction and a limitation. We will **not** introduce a new dataset, train a different kind of model, or build a separate web interface.

### Learning pathway

Unit I: Describe and code a problem

           ↓

Unit II: Store data, find records, sort records

           ↓

Units III–IV: Train and evaluate a neural-network classifier

           ↓

Unit V: Connect everything in the Flower Prediction Explorer

### Learning outcomes

After completing Unit V, a student should be able to:

1. Represent one prediction result as a Python dictionary and a collection of results as a list of dictionaries.  
2. Distinguish **raw measurements**, **model output**, **stored record**, and **displayed result**.  
3. Explain which steps are conventional algorithms and which use parameters learned by a neural network.  
4. Find a prediction by a sample ID, including appropriate behavior when that ID is absent.  
5. Sort results by a selected measurement without changing the trained model or original records.  
6. Evaluate held-out predictions using accuracy, a confusion matrix, and a majority-class baseline.  
7. Demonstrate one prediction, one lookup, and one sort and discuss a realistic limitation of the classifier.

**Scope:** One dataset, one classifier, one notebook, one small records explorer. The lessons avoid new implementation topics such as database systems, neural-network training from scratch, advanced search structures, or a graphical application.

---

# Chapter 17 — Connecting Data Structures, Algorithms, and AI

**Starting problem:** *How can we organize, find, and explain the predictions from our flower classifier?*

Imagine that our neural network predicts the species of 30 held-out Iris flowers. The classifier returns an array of predicted class numbers. That is useful for calculating accuracy, but a classmate may ask a different question: *What did the model predict for flower T026?* Another classmate may want to see the flowers with the smallest petal width first.

To answer those questions, we must connect the model's predictions to ordinary data structures and algorithms.

**Chapter goal:** Plan and understand a small workflow before writing the complete notebook in Chapter 18\.

## 17.1 Store sample IDs, measurements, actual labels, and predictions as simple records

### What is a record?

A **record** brings several facts about one item together. Think of a library card that stores a book's ID, title, author, and location. For our flower project, one record should contain:

| Field | Meaning | Example |
| :---- | :---- | :---- |
| `sample_id` | A unique ID within our explorer | `T001` |
| `measurements` | Four flower measurements, in dataset order | `[5.1, 3.5, 1.4, 0.2]` |
| `actual_label` | Known species index (from held-out answers) | `0` |
| `predicted_label` | Species index returned by the MLP | `0` |

The four measurements always have this order: **sepal length, sepal width, petal length, petal width**, measured in centimeters.

**Important distinction:** `T001`, `T002`, and similar values will be **IDs assigned to positions within this project's held-out test split**. They are *not* official or permanent Iris dataset identifiers. The teaching record below is **illustrative**; Chapter 18 generates actual records from the model's held-out predictions.

### Python dictionaries represent individual records

In Python, a **dictionary** associates a descriptive key with its value. A **list** groups many items in order. Combining them gives us a *list of dictionaries*:

\# Illustrative record, not yet a prediction produced by a model.

example\_records \= \[

    {

        "sample\_id": "T001",

        "measurements": \[5.1, 3.5, 1.4, 0.2\],

        "actual\_label": 0,

        "predicted\_label": 0,

    },

    {

        "sample\_id": "T002",

        "measurements": \[6.0, 2.7, 5.1, 1.6\],

        "actual\_label": 1,

        "predicted\_label": 2,

    },

\]

print(example\_records\[0\]\["sample\_id"\])

print(example\_records\[0\]\["measurements"\]\[2\])

**Output:**

T001

1.4

The first line accesses the first record's ID. The second accesses the same record's *petal length*, which is element 2 because Python indexes start at zero.

### Why are actual labels and predictions stored separately?

- `actual_label` is the known answer used **only for evaluation or teaching inspection** of the held-out predictions.  
- `predicted_label` is what the trained MLP returned from the four measurements.  
- In a genuinely new unlabeled example, its actual species is **unknown at prediction time**. We must not pass the answer into the classifier.

Keeping the two fields separate prevents a misleading explanation in which the model seems to be given the very answer it is supposed to predict.

### Why use a list of dictionaries?

A list of dictionaries is readable for beginners, can be created directly from a Python notebook, and supports both iteration and sorting. Other storage systems may be more suitable for very large projects, but our aim is to understand the connection—not to build a database.

**Complexity connection:** Looking for an arbitrary ID by scanning all `n` list records can require **O(n)** work in the worst case. Sorting `n` records using Python's built-in `sorted()` typically requires **O(n log n)** time in general and produces a new list. We only need a few dozen records, so clarity matters more than optimization.

### Reader action

Look at the first illustrative dictionary. Predict the result of `example_records[0]["actual_label"]`. **Answer: `0`.** Identify the role of each key before moving on.

## 17.2 Connect record lookup, sorting, and neural-network inference in a workflow diagram

### A single connected workflow

                             MODEL PREPARATION

       Labeled Iris training data ──► Fit scaler \+ MLP

                                            │

                                            ▼

                                      Trained pipeline

                                            │

                                  (kept unchanged)

                                            │

                                            ▼

                             HELD-OUT EXPLORER WORKFLOW

    Four flower measurements ──► Trained pipeline ──► Predicted class

                │                                        │

                └──► Combine with sample ID and actual label for evaluation

                                                         │

                                                         ▼

                                              List of dictionaries

                                                         │

                                      ┌──────────────────┴──────────────┐

                                      ▼                                 ▼

                              Search by sample ID                 Sort by feature

                                      │                                 │

                                      └──────────────────┬──────────────┘

                                                         ▼

                                               Display selected results

**Note:** The held-out *actual* label is stored for checking after predictions are generated. It is not used as an input to the MLP. The trained scaler and network are reused without retraining during the search-and-sort steps.

### Three different kinds of work

| Activity | Main tool | What it does |
| :---- | :---- | :---- |
| Save and organize results | **Data structures**: list, dictionary | Keep each ID, four measurements, true label, and predicted label together |
| Find and order results | **Ordinary algorithms**: linear search, built-in sort | Locate a record or rank records by a chosen measurement |
| Predict a species | **Connectionist AI**: trained MLP | Use learned weights and biases to convert flower measurements into class predictions |

The MLP does not automatically replace data structures or classical algorithms. Instead, **a useful application combines them**.

### Distinguishing inference from training

A model is **trained** when the learning algorithm adjusts its parameters using labeled training data. It performs **inference** when it applies those learned parameters to input measurements to make predictions.

Our explorer performs inference on the reserved test examples; a lookup or sort afterward does **not** train the model. In Chapter 18, the model is fitted once and reused for every exploration step.

### Reader action

Which part of the diagram produces the class prediction? **Answer:** the trained MLP. Which part retrieves a record identified by `T010`? **Answer:** a lookup algorithm applied to the list of dictionaries.

## 17.3 Plan a small results explorer and trace one sample through the workflow

### The explorer's minimum functions

We need only four features in the notebook:

1. **Create records** from held-out measurements, known labels, and predictions.  
2. **Find** a record when given its sample ID; report a missing ID clearly.  
3. **Sort** by one measurement while preserving the connection between each ID and its data.  
4. **Explain** the measured classifier result and one limitation.

No new user interface, new dataset, or second model is necessary.

### Data-flow trace: one example

Consider an **invented example for planning**:

| Stage | Value or action |
| :---- | :---- |
| Input | Measurements `[5.1, 3.5, 1.4, 0.2]` |
| Model inference | MLP returns class index `0` (assumed for this illustration) |
| Store | Save `T001`, measurements, true label `0`, predicted label `0` |
| Lookup | Request `T001` and retrieve that dictionary |
| Sorting | Place the same record according to its petal width, `0.2` |
| Display | Show ID, predicted species, actual species, and measurements |

Sorting changes the **order of displayed records**, not the values in the measurement list and not the neural-network prediction.

### Design checkpoints

Before implementing, ask:

- Are IDs unique inside the explorer?  
- Do all records contain four measurements in the expected order?  
- What happens when a sample ID is not found?  
- Is the requested sort measurement one of the four valid feature indices?  
- Are predictions evaluated on the same held-out set as in Unit IV?  
- Can students tell which example results are hypothetical and which outputs were actually measured?

**Chapter 17 takeaway:** A useful AI workflow combines ordinary storage and algorithms with learned predictions: **organize → predict → record → search/sort → explain**.

---

# Chapter 18 — Guided Project: Flower Prediction Explorer

**One guided project:** Reuse the Iris notebook introduced in Chapters 15–16 and implement the Chapter 17 plan. This is a shared demonstration for the written guide, PPT, and videos, **not an extra independent deliverable**.

**Starting problem:** *Can we build one notebook that stores a flower classifier's held-out predictions, retrieves one prediction by ID, sorts the results, and explains how well the model works?*

**Project deliverable:** One runnable notebook with setup instructions, a small results table, a workflow diagram (the Chapter 17 diagram may be reused), and a short explanation of the contributions of data structures, algorithms, and AI.

## Quick start and notebook rules

This is a guided exercise: students are expected to **run, inspect, explain, and safely modify** prepared code—not implement neural-network learning from scratch.

1. Open a Python 3 notebook (for example, Jupyter or another course-approved notebook environment).  
2. Install `scikit-learn` if it is missing, following your institution's normal package-installation procedure.  
3. Execute the cells **in order**, from Cell 1 to Cell 8\. Each later cell reuses variables produced by earlier cells.  
4. Use the same Iris training/test split and the same eight-neuron MLP configuration as Unit IV.  
5. Do **not** fit scaling on the complete dataset, tune the model on the final test set, or retrain it just to make a sorting result look different.

Package needs: `scikit-learn` plus its standard dependencies. No custom dataset download or extra UI library is needed. The Iris dataset is provided within scikit-learn.

## 18.1 Build: Store results, find a sample by ID, and sort by measurement

### Cell 1 — Load the same Iris dataset and make the held-out split

from sklearn.datasets import load\_iris

from sklearn.model\_selection import train\_test\_split

iris \= load\_iris()

X \= iris.data

Y \= iris.target

class\_names \= iris.target\_names

feature\_names \= iris.feature\_names

X\_train, X\_test, y\_train, y\_test \= train\_test\_split(

    X,

    Y,

    test\_size=0.20,

    random\_state=42,

    stratify=Y,

)

print("Classes:", list(class\_names))

print("Training samples:", len(X\_train))

print("Held-out samples:", len(X\_test))

**Expected split:** 120 training flowers and 30 held-out flowers. The dataset has four ordered numerical features and three known species labels.

**Why this is important:** The split creates an honest division between model learning and final evaluation. We keep the same seed and stratification as Unit IV so the demonstrations agree.

### Cell 2 — Fit the same small MLP pipeline used in Unit IV

from sklearn.pipeline import make\_pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.neural\_network import MLPClassifier

model \= make\_pipeline(

    StandardScaler(),

    MLPClassifier(

        hidden\_layer\_sizes=(8,),

        activation="relu",

        solver="adam",

        learning\_rate\_init=0.01,

        alpha=0.01,

        max\_iter=1200,

        random\_state=42,

    ),

)

model.fit(X\_train, y\_train)

print("Trained MLP ready.")

**Pipeline reminder:** The scaler learns its parameters from training data inside `fit`. When the pipeline later predicts on the test set, it uses those same learned scaling parameters. **Never fit a scaler on `X_test` or on all `X` before splitting.**

### Cell 3 — Generate held-out predictions and a majority-class baseline

from sklearn.dummy import DummyClassifier

from sklearn.metrics import accuracy\_score, confusion\_matrix

y\_pred \= model.predict(X\_test)

baseline \= DummyClassifier(strategy="most\_frequent")

baseline.fit(X\_train, y\_train)

baseline\_pred \= baseline.predict(X\_test)

mlp\_accuracy \= accuracy\_score(y\_test, y\_pred)

baseline\_accuracy \= accuracy\_score(y\_test, baseline\_pred)

print("MLP accuracy:", round(mlp\_accuracy, 3))

print("Baseline accuracy:", round(baseline\_accuracy, 3))

print("Confusion matrix (actual rows, predicted columns):")

print(confusion\_matrix(y\_test, y\_pred, labels=\[0, 1, 2\]))

The MLP uses the four measurements to predict classes. The majority-class baseline always predicts the most frequent training label, ignoring the measurements. Both are evaluated on the **same held-out 30 flowers**.

**Important:** The correct test labels are used **after prediction** to measure accuracy. They do not go into `model.predict`.

### Cell 4 — Convert predictions into a list of dictionaries

records \= \[\]

for i, (measurements, actual, predicted) in enumerate(

    zip(X\_test, y\_test, y\_pred), start=1

):

    records.append({

        "sample\_id": f"T{i:03d}",

        "measurements": measurements.tolist(),

        "actual\_label": int(actual),

        "predicted\_label": int(predicted),

    })

print("Number of prediction records:", len(records))

for record in records\[:3\]:

    print(

        record\["sample\_id"\],

        "actual:", class\_names\[record\["actual\_label"\]\],

        "predicted:", class\_names\[record\["predicted\_label"\]\],

        "petal width (cm):", record\["measurements"\]\[3\],

    )

**Expected count:** 30 prediction records. Every record represents one held-out example. The `sample_id` identifies its *position within this test split*, not a permanent Iris dataset row ID.

**How the code connects the subjects:**

- The predictions come from the previously trained **AI model**.  
- Each prediction is stored in a **dictionary**.  
- Dictionaries are grouped in a Python **list**.  
- A normal Python **loop** builds the records and prints them.

### Cell 5 — Find one sample using its ID

def find\_record(records, requested\_id):

    """Return the matching dictionary, or None if the ID is unknown."""

    for record in records:

        if record\["sample\_id"\] \== requested\_id:

            return record

    return None

found \= find\_record(records, "T001")

missing \= find\_record(records, "T999")

print("T001 found:", found is not None)

print("T999 found:", missing is not None)

if found is not None:

    print("T001 prediction:", class\_names\[found\["predicted\_label"\]\])

A **linear search** checks records until it finds the requested ID. The ID `T999` is not among `T001` through `T030`, so our function returns `None` instead of crashing. The worst-case search time is **O(n)** for `n` records.

### Cell 6 — Sort the records by one Iris measurement

def sort\_by\_feature(records, feature\_index):

    """Return a new list, ordered by the selected measurement."""

    if feature\_index not in range(4):

        raise ValueError("feature\_index must be 0, 1, 2, or 3")

    return sorted(

        records,

        key=lambda record: record\["measurements"\]\[feature\_index\],

    )

\# Feature index 2 means petal length (in centimeters).

sorted\_records \= sort\_by\_feature(records, 2\)

print("Sorted by:", feature\_names\[2\])

for record in sorted\_records\[:5\]:

    print(record\["sample\_id"\], record\["measurements"\]\[2\])

`sorted()` creates a new ordered list. The original `records` list and the trained MLP are not changed. Each dictionary keeps its own ID, actual label, predicted label, and four measurements together as a single item.

**Watch out:** Sorting `measurements` alone would detach values from their proper IDs. The project sorts **records**, not separate columns.

## 18.2 Check: Verify lookup, sorting, and classifier evaluation

Working code is not the same as verified code. We should deliberately test ordinary and unusual cases.

### Check 1 — Successful and missing-ID lookup

The program should find `T001` and return `None` for `T999`. If the lookup function silently returns a different record for a missing ID, it is incorrect.

### Check 2 — Sorted output really is ordered

A correct ascending sort should produce measurements that do not decrease from one record to the next.

### Check 3 — The classifier was evaluated on held-out data

The 30 predictions and 30 true labels must line up. The confusion matrix should contain exactly 30 samples when its entries are added together. Both classifier and baseline accuracy should lie between `0` and `1`.

### Cell 7 — Run the checks

assert len(records) \== len(X\_test) \== len(y\_test) \== len(y\_pred) \== 30

assert len({record\["sample\_id"\] for record in records}) \== len(records)

assert all(len(record\["measurements"\]) \== 4 for record in records)

assert find\_record(records, "T001") is not None

assert find\_record(records, "T999") is None

petal\_lengths \= \[record\["measurements"\]\[2\] for record in sorted\_records\]

assert petal\_lengths \== sorted(petal\_lengths)

assert {r\["sample\_id"\] for r in sorted\_records} \== {

    r\["sample\_id"\] for r in records

}

matrix \= confusion\_matrix(y\_test, y\_pred, labels=\[0, 1, 2\])

assert matrix.sum() \== len(y\_test)

assert 0 \<= mlp\_accuracy \<= 1

assert 0 \<= baseline\_accuracy \<= 1

print("All record, search, sorting, and evaluation checks passed.")

These tests detect common implementation mistakes such as losing records during sorting, assigning duplicate IDs, or misaligning prediction lengths. They do **not** prove that a classifier will perform well on every unfamiliar flower.

### Example evaluation (reference run, not an invented result)

Running the Unit IV configuration on the same split in **scikit-learn 1.8.0** produced the following reference measurements:

| Measurement | Reference output |
| :---- | ----: |
| Training examples | 120 |
| Held-out examples | 30 |
| MLP held-out accuracy | 29/30 \= **96.7%** |
| Majority-class baseline | 10/30 \= **33.3%** |
| Correctly classified held-out flowers | 29 |
| Incorrectly classified held-out flowers | 1 |

Reference confusion matrix; **rows are actual species**, **columns are predictions**:

| Actual ↓ / Predicted → | setosa | versicolor | virginica |
| :---- | ----: | ----: | ----: |
| setosa | 10 | 0 | 0 |
| versicolor | 0 | 9 | 1 |
| virginica | 0 | 0 | 10 |

If a local run gives slightly different outcomes, **report the observed values** rather than copying the reference numbers as though they were measured on that computer. The reference results describe one particular software/data configuration, not a universal accuracy guarantee.

**Interpretation:** The MLP does better than the simple baseline on this split, but the sample is small. We should not generalize this accuracy to other flower datasets, images, or safety-critical applications.

## 18.3 Explain: Demonstrate a prediction, search, sort, and limitation

A complete educational demonstration should show the **meaning** of the program, not just its printed numbers.

### Cell 8 — Change the sorting measurement without retraining

\# Reader challenge: change sorting from petal length (2)

\# to petal width (3); keep the trained model unchanged.

by\_petal\_width \= sort\_by\_feature(records, 3\)

print("Sorted by:", feature\_names\[3\])

for record in by\_petal\_width\[:5\]:

    print(record\["sample\_id"\], record\["measurements"\]\[3\])

\# Find and explain one real record from this run.

sample \= find\_record(records, "T001")

if sample is not None:

    print("Sample ID:", sample\["sample\_id"\])

    print("Measurements (cm):", sample\["measurements"\])

    print("Model prediction:", class\_names\[sample\["predicted\_label"\]\])

    print("Known actual class:", class\_names\[sample\["actual\_label"\]\])

\# This check verifies that the predictions were not changed by sorting.

assert all(

    find\_record(by\_petal\_width, r\["sample\_id"\])\["predicted\_label"\]

    \== r\["predicted\_label"\]

    for r in records

)

### How to narrate the demonstration

**Step A — One prediction.** Select `T001`. Explain that four numerical measurements go through the trained preprocessing-and-MLP pipeline. The model generates a species prediction, which is stored in the record. Read the **actual output from the notebook** rather than guessing the predicted species.

**Step B — One search.** Find `T001` with `find_record`. Explain that a standard linear search loops through the list of dictionaries and checks their IDs. Next, try `T999` to demonstrate safe handling of an unknown ID.

**Step C — One sort.** Sort by petal length (index `2`), display five small values, then change to petal width (index `3`) and observe the new order. Explain that sorting is an ordinary algorithm and does not recalculate the model's predictions.

**Step D — One evaluation.** Show held-out MLP accuracy, the baseline accuracy, and the confusion matrix. State the actual number of correct and incorrect examples from the program.

**Step E — One limitation.** Explain that the model was trained on a small, structured Iris dataset using four accurate measurements. Its performance on unfamiliar species, incorrect measurements, or substantially different data has not been established. A strong result on this classroom test set does not justify relying on the model for unrelated or high-stakes decisions.

### Compact results table for a team demonstration

Students can prepare a 5-row table with the first five entries in `records`:

| Sample ID | Sepal length | Petal width | Actual species | Predicted species |
| :---- | ----: | ----: | :---- | :---- |
| Fill from notebook | Fill from notebook | Fill from notebook | Fill from notebook | Fill from notebook |

**Do not invent the table's model outputs.** Copy measured results from Cell 4 or a short reporting cell.

### Optional reporting cell — Print the first five actual records neatly

print("ID   Sepal length  Petal width  Actual       Predicted")

for record in records\[:5\]:

    m \= record\["measurements"\]

    actual\_name \= class\_names\[record\["actual\_label"\]\]

    predicted\_name \= class\_names\[record\["predicted\_label"\]\]

    print(

        f'{record\["sample\_id"\]:\<4} {m\[0\]:\>12.1f} {m\[3\]:\>12.1f}  '

        f'{actual\_name:\<12} {predicted\_name}'

    )

### Project completion checklist

- [ ] Run the Iris data split and train the same MLP pipeline as Unit IV.  
- [ ] Produce 30 held-out prediction records containing four measurements and both labels.  
- [ ] Find `T001`; handle `T999` without an exception.  
- [ ] Sort by petal length, then by petal width, preserving each complete record.  
- [ ] Record actual held-out accuracy, baseline accuracy, and confusion matrix.  
- [ ] Demonstrate one prediction, one search, one sorting result, and one limitation.  
- [ ] Include the Chapter 17 workflow diagram and short setup instructions.  
- [ ] Credit the dataset/library sources and disclose any AI assistance as required by the course.

**Chapter 18 takeaway:** The Flower Prediction Explorer integrates **lists and dictionaries for storage**, **search and sort algorithms for organization**, and a **trained neural network for predictions** into one clear and reproducible learning experience.

---

# Unit V Review and Practice

The questions below test whether students can explain the workflow; students do not need to write a new AI training system.

1. What is the difference between `actual_label` and `predicted_label`?  
2. Why does our explorer use a list of dictionaries rather than a list of isolated species names?  
3. Does `sorted(records, ...)` retrain the neural network? Why or why not?  
4. What should `find_record(records, "T999")` return, and why?  
5. Which feature does index `2` represent in the Iris measurement list? Which feature is index `3`?  
6. Why is a majority-class baseline useful when reporting MLP accuracy?  
7. How many entries should a confusion matrix represent for the 20% held-out split?  
8. Why must the scaler be fitted on training data only?  
9. Give one reason not to assume that accuracy on Iris generalizes to every real-world classification problem.  
10. Identify one data-structure operation, one ordinary algorithm, and one connectionist-AI operation in the notebook.

## Short answer key

1. `actual_label` stores the known correct species for evaluation; `predicted_label` stores the model's output.  
2. Each dictionary keeps the ID, measurements, actual label, and prediction together so searching and sorting retain their relationship.  
3. No. It only creates an ordered list of existing records; the MLP parameters remain unchanged.  
4. `None`, because that ID is absent. This allows the program to handle missing records clearly.  
5. Index `2` is petal length; index `3` is petal width.  
6. It provides a simple comparison, helping us judge whether the trained model adds value beyond always guessing a common class.  
7. Thirty held-out examples in total (the confusion-matrix entries sum to 30).  
8. To prevent information from the held-out examples leaking into the training process.  
9. The dataset is small, clean, and limited to three Iris species with four numerical measurements; real-world conditions may differ.  
10. Example: dictionary/list storage; linear search or sorting; neural-network inference from four measurements.

## Glossary

| Term | Meaning |
| :---- | :---- |
| **Record** | One grouped collection of fields describing an item |
| **Dictionary** | Python mapping between keys and values |
| **List** | Ordered collection of items |
| **Sample ID** | Identifier assigned to one held-out record in this explorer |
| **Linear search** | Check items one by one until a match is found or the list ends |
| **Sorting** | Arrange records by a chosen comparison key |
| **Inference** | Apply a trained model to input measurements to produce a prediction |
| **Held-out data** | Data reserved from model fitting for final evaluation |
| **Accuracy** | Fraction of examples whose predicted classes match true labels |
| **Confusion matrix** | Counts of actual classes versus predicted classes |
| **Baseline** | A simple method used as a reference for model performance |
| **Data leakage** | Allowing information from evaluation data to influence model preparation or training improperly |

---

# Teaching and Presentation Notes for PentaByte

This section supports the **same single project**, not a new task.

- **Markdown / study guide:** Explain Chapter 17 with its workflow diagram and one example record. For Chapter 18, feature key notebook cells, an actual results table, and a short evaluation. Condense the final study-guide layout as needed to match the team outline's preferred 1–2 pages per chapter.  
- **PPT:** Use a clear pipeline diagram, one list-of-dictionaries example, one lookup result, one sorting result, and the measured classifier evaluation. Avoid copying full code cells onto slides.  
- **Video tutorial:** Run the prepared notebook and explain what changed when the user searches or sorts. Demonstrate a limitation. The outline proposes focused videos covering selected ideas; it does not require narrating all 18 chapters line-by-line.  
- **Team review:** Check code execution in order, ensure diagrams match variable names, verify that results tables reflect actual runs, and cite sources for reused diagrams and data. Keep project-specific AI-use disclosures consistent with team policy.

## Unit V bridge and final project conclusion

The five units form one learning story:

**Algorithms define steps. Data structures organize information. Connectionist AI learns patterns and produces predictions.** Our Flower Prediction Explorer brings the three together: it receives measurements, uses a trained network for a species prediction, stores that result, and then searches and sorts records for inspection.

Completing this notebook demonstrates the **relationship among the subjects**, not expertise in advanced neural-network engineering. The next step for the PentaByte team is to review and combine the five unit drafts, verify demonstration outputs, and reuse the same project example consistently in the study guide, slides, and video tutorials.

---

# References and attribution

The scope, chapter numbering, guiding problems, and main examples follow the team-provided *PentaByte Focused Project Content Outline* (25 October 2026). This document expands that outline into educational prose, guided notebook code, and self-check exercises; illustrative records are labeled as such. The classifier configuration is intentionally reused from PentaByte Unit IV.

1. scikit-learn, **Iris dataset**: [https\://scikit-learn.org/stable/datasets/toy\_dataset.html\#iris-dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset)  
2. scikit-learn, **MLPClassifier**: [https\://scikit-learn.org/stable/modules/generated/sklearn.neural\_network.MLPClassifier.html](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)  
3. scikit-learn, **Pipeline / make\_pipeline**: [https\://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make\_pipeline.html](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html)  
4. scikit-learn, **train\_test\_split**: [https\://scikit-learn.org/stable/modules/generated/sklearn.model\_selection.train\_test\_split.html](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)  
5. scikit-learn, **StandardScaler**: [https\://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)  
6. scikit-learn, **confusion\_matrix**: [https\://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion\_matrix.html](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)  
7. scikit-learn, **DummyClassifier**: [https\://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)

**AI-use note:** This draft was prepared with AI writing and coding assistance. Before submission, team members should review claims, execute the code in the target environment, correct errors, and document AI use in the format required by the professor.