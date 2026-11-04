# PentaByte — Detailed Learning Content (Version 2.0)

## Algorithms, Data Structures, and Connectionist AI

### A Beginner's Guide to Learning Through Problems

**Unit IV:** Connectionist AI: Learning, Testing, and Applications  
**Chapters:** 13–16  
**Team:** PentaByte  
**Source outline:** Focused Project Content Outline, 25 October 2026  
**Audience:** Beginning university students with little or no programming experience  
**Demonstration language:** Python 3 with scikit-learn  
**Document type:** Detailed Markdown lesson draft for the study guide, PPT, and video tutorials  
**Status:** Draft for team review; experimental outputs verified in a local Python environment, not guaranteed on every machine

---

# Unit IV — Connectionist AI: Learning, Testing, and Applications

## Unit introduction

Unit III explained how a neural network uses input features, weights, biases, and activation functions to **produce a prediction**. However, the small calculations in that unit used hand-selected weights. They showed how prediction works; they did not demonstrate learning from real data.

This unit completes the learning process. First, we learn how to compare a prediction with its correct target and describe the error using a **loss function**. Next, we explain how optimization algorithms use information about the loss to improve a network's weights and biases. We then run a small, supplied **multilayer perceptron (MLP)** classifier on the Iris flower dataset. Finally, we evaluate its predictions on examples that were not used for training and discuss where similar technology might fail or require human oversight.

**Unit pathway:**

`Prediction → Loss → Backpropagation and parameter updates → Train an Iris classifier → Evaluate held-out predictions → Discuss limitations`

**By the end of Unit IV, learners should be able to:**

1. Explain the roles of predicted values, correct targets, prediction errors, and loss functions.  
2. Calculate and compare simple squared errors without confusing them with the loss used by the actual Iris classifier.  
3. Read a learning curve and explain why a smaller *training* loss does not guarantee better results on new data.  
4. Describe gradient descent and backpropagation intuitively, without deriving gradients.  
5. Trace the repeatable training cycle: **forward pass → loss → gradients → weight update**.  
6. Run a prepared scikit-learn MLP with a reproducible data split and training-only feature scaling.  
7. Compare a neural-network model with a majority-class baseline on held-out examples, read a confusion matrix, and recognize a possible error.  
8. Discuss overfitting, unfamiliar data, privacy, unequal performance across groups, and human oversight.

**Learning boundaries:** One dataset (Iris), one small neural-network family (MLP), one final held-out test set, and a few guided modifications. We will **not** derive calculus formulas, write backpropagation from scratch, undertake a model search, or introduce CNN/RNN/transformer implementation. The trained Iris model is an educational example; it is **not** a safety-critical decision system.

**Software note:** The runnable model demonstration uses the same four ordered Iris features and three class labels introduced in Unit III. Python packages required for Chapters 15–16: `scikit-learn`, and optionally `matplotlib` for a learning-curve plot. Example notebooks should install packages through their normal school-approved environment.

---

# Chapter 13 — Prediction Error and Loss Functions

**Starting problem:** *How can a neural network tell whether its prediction needs improvement?*

Imagine that a student estimates tomorrow's classroom attendance as 28 people, but 30 actually attend. The prediction and the answer differ. To improve future predictions, we need a way to describe how far a prediction is from its target. Neural-network training uses a related idea: **measure prediction error**, then adjust the network to reduce an appropriate numerical measure of error.

**Learning objective:** Understand targets, predictions, loss, and the difference between fitting training examples and performing well on unseen examples.

## 13.1 Compare a network's prediction with the correct target or label

In supervised machine learning, a dataset contains both **input features** and **correct targets (labels)**. The training algorithm uses the labels to learn a relationship between inputs and outputs. During prediction on an unknown example, the label is *not* provided to the model.

For the Iris dataset:

- **Features:** four measurements—sepal length, sepal width, petal length, and petal width.  
- **Target/label:** one of three Iris species: setosa, versicolor, or virginica.  
- **Prediction:** a class chosen by a trained model from the input measurements.  
- **Correctness:** determined by comparing the predicted class with the known label of an evaluation example.

Consider three **invented teaching records** (not model measurements):

| Record | Correct species | Predicted species | Correct? |
| :---- | :---- | :---- | :---- |
| A | setosa | setosa | Yes |
| B | versicolor | virginica | No |
| C | virginica | virginica | Yes |

The model correctly classifies two of the three examples. This helps us see whether each final decision was correct, but **accuracy alone does not describe how a model should adjust its parameters during training**. For this reason, learning algorithms generally use a numerical *loss function* that responds to their outputs.

A classifier can be very confident and wrong, or uncertain but right. Many losses make use of output values before, or alongside, the final class decision to distinguish such cases. Different tasks require different loss functions.

**Do not confuse these terms:**

| Term | Beginner-friendly meaning | Iris illustration |
| :---- | :---- | :---- |
| Target or label | Known correct answer | `versicolor` |
| Model output | Numbers produced by the network | Three class-related values |
| Predicted class | Selected category | `virginica` |
| Prediction error | Disagreement with the answer | Predicted class differs from label |
| Loss | Numerical training objective | Cross-entropy for a multi-class MLP classifier |

## 13.2 Introduce loss as a numerical measure of prediction error

A **loss function** takes information about a prediction and its target and produces a number that the training process tries to reduce. The precise formula depends on the problem and model.

### Example A — Squared error for a single numerical prediction

For an easily calculated example, suppose the correct numerical target is **1**. Two hypothetical predictors return **0.8** and **0.6**.

A *squared-error* calculation for one example is:

\[ \\text{Squared error} \= (\\text{target} \- \\text{prediction})^2. \]

| Target | Prediction | Calculation | Squared error |
| ----: | ----: | :---- | ----: |
| 1 | 0.8 | `(1 - 0.8)²` | 0.04 |
| 1 | 0.6 | `(1 - 0.6)²` | 0.16 |

The prediction **0.8** is closer to the target, so its squared error is smaller. Squaring ensures that positive and negative differences both contribute nonnegative values and that large differences receive larger penalties.

\# Illustrative one-output example; NOT the Iris MLP loss.

target \= 1.0

predictions \= \[0.8, 0.6\]

for prediction in predictions:

    squared\_error \= (target \- prediction) \*\* 2

    print(f"Prediction: {prediction:.1f}; squared error: {squared\_error:.2f}")

**Expected output:**

Prediction: 0.8; squared error: 0.04

Prediction: 0.6; squared error: 0.16

**Important boundary:** This calculation explains the *idea* of loss. It is **not** the complete loss used by the scikit-learn Iris `MLPClassifier` in Chapter 15\.

### Example B — Classification loss in words

The Iris MLP is a *classification* model. Its training objective is based on **log loss (cross-entropy)**, which considers how the model's predicted class probabilities relate to the correct class. Intuitively:

- Giving relatively high predicted probability to the correct class generally contributes a smaller classification loss.  
- Giving very low predicted probability to the correct class contributes a larger classification loss.  
- These predicted probabilities are model outputs; they are not a guarantee that the model is well calibrated on every kind of real-world input.

There is no need to perform logarithm calculations here. The objective is to recognize why a **numerical learning signal** provides more guidance for training than a simple right/wrong indicator.

### Worked example — Which output is better?

The target is 1\. Model A returns 0.8 and Model B returns 0.6. Use squared error to decide which is closer. **Answer:** A has error 0.04; B has error 0.16; A is better under this illustrative squared-error measure.

## 13.3 Interpret a simple loss curve and explain why smaller training loss is not the only goal

A **loss curve** plots the value of loss against progress through training. A training iteration or epoch is part of the model's process for updating parameters. The exact meaning of an iteration depends on the training algorithm. With stochastic scikit-learn MLP solvers, `max_iter` corresponds to epochs over the data.

Here is an **invented illustration** (these numbers are not from a trained model):

| Training epoch | Illustrative training loss |
| ----: | ----: |
| 1 | 1.20 |
| 2 | 0.93 |
| 3 | 0.71 |
| 4 | 0.52 |
| 5 | 0.39 |

Training loss (illustrative, not measured)

High \| \*

     \|   \*

     \|      \*

     \|         \*

Low  \|            \*

     \+---------------------

       1   2   3   4   5   epoch

The declining values suggest that the model is fitting its training objective more closely. But a low training loss does **not** automatically mean that the model will perform well on unfamiliar flowers.

Why not?

- **Overfitting:** the network may learn details that are particular to its training examples rather than patterns that transfer well.  
- **Data mismatch:** new flowers might have different measurement conditions or characteristics.  
- **Bad labels or insufficient examples:** the training records themselves may be incomplete or incorrect.  
- **Evaluation mistakes:** the model may accidentally benefit from information that should have been held out.

For this reason, Chapter 16 measures performance on a separate **held-out test set**, and Chapter 15 explains how optional settings should be checked using **validation data**, not by repeatedly inspecting the final test set.

**Reader action:** Imagine that a network's training loss decreases while its validation performance gets worse. Does the lower training loss prove that the network is improving on new data? **Hint:** No; this can be a warning sign of overfitting.

**Chapter 13 takeaway:** Loss gives training a numerical signal for improvement, but reliable learning must ultimately be assessed on examples the model has not trained on.

---

# Chapter 14 — How Neural Networks Learn: Gradient Descent and Backpropagation

**Starting problem:** *How can the network adjust its connections after making a wrong prediction?*

In Unit III, a neuron calculated a result from its inputs, weights, and bias. The interesting question is how those values can become useful without someone manually trying every possible combination. Neural-network training uses **optimization** to update the values in response to examples and the losses they produce.

**Learning objective:** Explain the roles of adjustable parameters, gradient descent, and backpropagation and trace the training process at a conceptual level.

## 14.1 Explain weights as adjustable connection strengths and gradient descent as a way to reduce loss

A network contains **parameters**, especially weights and biases. A weight changes how strongly an input contributes to a neuron's calculation. A bias shifts the neuron's input before activation. During training, the learning algorithm adjusts these values.

Think of a student learning to throw a ball into a basket. If each throw consistently lands too short, the student can change the next attempt. The analogy is not exact—neural networks use numerical optimization rather than human judgment—but it captures the idea of **adjusting behavior using feedback**.

In machine learning, **gradient descent** is a family of optimization approaches that uses information about how the loss changes when parameters change. The gradient indicates a local direction of increasing loss; an update generally takes a step in a direction intended to **decrease** loss.

A **learning rate** controls the size of an update. A very large update may overshoot useful settings. A very small update may make learning slow. Practical optimizers such as **Adam**, used by our prepared MLP, modify the basic gradient-descent approach using information from previous updates.

Adjustable weights and biases

             ↓

Predict with current values

             ↓

Measure training loss

             ↓

Use gradients to guide a parameter update

             ↓

Predict again with updated values

**Key distinction:** A network's numerical weights do not automatically have a simple verbal meaning such as “this weight represents petal size.” Their effects depend on the network as a whole.

## 14.2 Introduce backpropagation visually as passing information about error backward

A **forward pass** moves numerical information from inputs through hidden layers to model outputs. **Backpropagation** is the computational process used to calculate the gradients needed to update the weights and biases. It propagates information about the loss **back through the network's computational connections**.

FORWARD COMPUTATION

Four flower measurements

           │

           ▼

    \[ Hidden neurons \] ─────────► \[ Class outputs \]

                                          │

                                          ▼

                                  Compare with label

                                          │

                                          ▼

                                         Loss

BACKWARD GRADIENT COMPUTATION

                                         Loss

                                          │

                                          ▼

       \[ Hidden-layer parameters \] ◄── \[ Output-layer parameters \]

                gradients                      gradients

                                          │

                                          ▼

                            Optimizer updates parameters

The arrows in the backward portion describe how **gradient information is computed**, not a second pass that replaces the original input data with class labels. The network does not “send the correct class back as a new feature.” The labels are used to calculate loss, and backpropagation determines how the trainable parameters contributed to that loss.

### Why backpropagation matters

Even a small network has multiple connections. If we tried to adjust every weight independently using blind guesses, training would be inefficient. Backpropagation provides an organized way to calculate how changes to different parameters would affect the loss locally.

For this guide, you only need to recognize **the direction and purpose** of the process. Mathematical gradient derivations are outside the agreed project scope.

## 14.3 Trace the training cycle: forward pass → loss → gradients → weight update → repeat

The learning process for one training step can be understood in five stages:

| Stage | What happens | Beginner question |
| :---- | :---- | :---- |
| 1\. Forward pass | Inputs pass through the current network | What did it predict? |
| 2\. Loss | Prediction is compared with the correct target | How poorly did it do? |
| 3\. Backpropagation | Gradients are computed | Which parameter changes could help? |
| 4\. Optimization step | Weights and biases are adjusted | What will change before the next pass? |
| 5\. Repeat | More training steps are performed | Is the loss improving on the training data? |

### Worked example — Follow one update (conceptual)

Assume our model predicts the wrong flower category for a labeled training sample.

1. A forward pass processes the four measurements and outputs a prediction.  
2. The predicted outputs and correct species label are used to calculate training loss.  
3. Backpropagation computes gradients for the network's adjustable parameters.  
4. The optimizer uses those gradients to update weights and biases.  
5. In later passes, the model processes more training data using the updated parameters.

**This is not a claim that the wrong prediction will immediately become correct after one update.** Individual updates may have mixed effects; learning often requires many examples and repeated passes.

A simple learning-cycle diagram for the PPT or video:

\[Training examples with labels\]

                │

                ▼

       \[Forward pass\]

                │

                ▼

        \[Compute loss\]

                │

                ▼

       \[Backpropagation\]

                │

                ▼

       \[Optimizer update\]

                │

                └────────► Repeat training cycle

After training: use the trained network to predict on new inputs.

**Reader action:** Arrange the following stages in order: *weight update; loss computation; forward pass; backpropagation.* **Answer:** Forward pass → loss → backpropagation → weight update.

**Chapter 14 takeaway:** Neural networks learn by repeatedly producing predictions, measuring loss, computing gradients with backpropagation, and updating trainable parameters through an optimizer.

---

# Chapter 15 — Training a Simple Neural Network Classifier

**Starting problem:** *Can a small neural network learn patterns in Iris flower measurements?*

We are ready to use a real learning algorithm rather than hand-selecting weights. This chapter provides a **guided notebook-style demonstration**. Students should run the provided code, inspect the output, and make only a small, controlled modification. They do not need to build an MLP or derive backpropagation themselves.

**Learning objective:** Train an Iris MLP using a careful data split, training-only feature scaling, fixed initial settings, and an optional validation-only comparison.

## 15.1 Open a prepared Iris notebook, create training and held-out test data, and scale features correctly

The Iris dataset contains **150 samples**, **four numerical measurements** per flower, and **three target classes**. Its compact size makes it convenient for a classroom demonstration.

**Training data** helps the model learn. **Validation data** can be used to compare possible settings. **Held-out test data** provides a final check on a trained model that has not been chosen based on those test examples.

For the main demonstration, we reserve **20% of the data (30 flowers)** as a held-out test set. The remaining **120 flowers** form the training set. We use a **stratified split**, which maintains class proportions in each portion for this balanced dataset.

### Notebook cell 1 — Load and split the dataset

from sklearn.datasets import load\_iris

from sklearn.model\_selection import train\_test\_split

iris \= load\_iris()

X \= iris.data             \# Four measurements per flower

Y \= iris.target           \# Correct species indices (0, 1, 2\)

class\_names \= iris.target\_names

X\_train, X\_test, y\_train, y\_test \= train\_test\_split(

    X, Y,

    test\_size=0.20,

    random\_state=42,

    stratify=Y,

)

print("Feature names:", list(iris.feature\_names))

print("Class names:", list(class\_names))

print("Training samples:", len(X\_train))

print("Held-out test samples:", len(X\_test))

**Expected sample counts:** 120 training samples and 30 held-out test samples. The feature order remains **sepal length, sepal width, petal length, petal width**.

### Why scale the measurements?

Neural-network optimization can behave better when input features are on similar numerical scales. **StandardScaler** estimates a mean and standard deviation for each feature and uses these to transform data. The crucial rule is that these statistics must be **learned from training data only**, not from the entire dataset or the held-out test set.

To reduce accidental leakage, we combine scaling and classification into a **scikit-learn pipeline**. Calling `model.fit(X_train, y_train)` fits the scaler on `X_train` and then trains the MLP. Later, `model.predict(X_test)` uses the previously fitted scaler; it does not learn new scaling statistics from `X_test`.

TRAINING

X\_train ──► \[Fit scaler on training data\] ──► \[Train MLP\]

FINAL EVALUATION

X\_test ──► \[Apply saved training scaler\] ──► \[Trained MLP\] ──► predictions

**Avoid:** `StandardScaler().fit_transform(X)` **before** making a train/test split. That would allow information from later test examples to influence preprocessing.

## 15.2 Run a supplied multilayer perceptron classifier and observe training

An **MLPClassifier** is a feedforward neural-network classifier. The configuration below uses just **one hidden layer with eight neurons**, **ReLU activation**, the **Adam** optimizer, and a fixed random seed.

### Notebook cell 2 — Fit a small MLP

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

\# Fit ONLY on training examples. Do not evaluate X\_test yet.

model.fit(X\_train, y\_train)

print("Model training complete.")

**What do the settings mean?**

| Setting | Value | What it controls |
| :---- | :---- | :---- |
| `hidden_layer_sizes` | `(8,)` | One hidden layer with eight neurons |
| `activation` | `"relu"` | The hidden-layer activation function |
| `solver` | `"adam"` | Optimization method |
| `learning_rate_init` | `0.01` | Initial learning-rate setting |
| `alpha` | `0.01` | Strength of L2 regularization |
| `max_iter` | `1200` | Maximum number of training epochs for this solver |
| `random_state` | `42` | Seed for repeatable pseudo-random behavior |

The fixed seed helps reproduce the setup. Results can still differ somewhat across library versions and numerical environments. A maximum number of epochs is an **upper limit**, not a guarantee that training runs exactly that many epochs.

### Notebook cell 3 — Inspect the training process

network \= model.named\_steps\["mlpclassifier"\]

print("Training accuracy:", round(model.score(X\_train, y\_train), 3))

print("Epochs completed:", network.n\_iter\_)

print("First recorded loss:", round(network.loss\_curve\_\[0\], 4))

print("Last recorded loss:", round(network.loss\_curve\_\[-1\], 4))

The list `network.loss_curve_` contains the training loss recorded as the stochastic optimizer runs. Use it to inspect **training**, not final generalization performance.

**Optional visual (requires `matplotlib`):**

import matplotlib.pyplot as plt

plt.plot(network.loss\_curve\_)

plt.xlabel("Training epoch")

plt.ylabel("Recorded training loss")

plt.title("Iris MLP: Training-loss history")

plt.show()

**How to explain the plot:** A general downward trend indicates that the algorithm found parameter updates that reduced the training objective over time. Small fluctuations or plateaus are normal. Do not read a held-out accuracy value from a loss curve.

### Worked example — Interpret the notebook blocks

| Code block | Purpose | Evidence to inspect |
| :---- | :---- | :---- |
| `load_iris()` | Obtain the standard dataset | Four feature names and three species |
| `train_test_split(...)` | Reserve unseen examples | 120 training / 30 test |
| `StandardScaler()` | Scale features using training-derived statistics | Pipeline order |
| `MLPClassifier(...)` | Define the neural network | Hidden layer and optimizer settings |
| `model.fit(...)` | Learn from labeled training examples | Trained model and iterations |
| `network.loss_curve_` | Inspect training optimization | Recorded loss values |

## 15.3 Change one permitted setting in a guided copy; compare using validation data only

An experiment is easiest to interpret when it changes **one thing at a time**. We will compare an MLP with **eight hidden neurons** against one with **twelve hidden neurons**. All other chosen settings stay the same. This is an optional learning activity, not an exhaustive search for the best model.

**Critical rule:** The final held-out test set is not used to compare or select these settings. Instead, we split part of the existing 120 training examples into a smaller fitting subset and a validation subset:

- 90 fitting samples: used to train each comparison model.  
- 30 validation samples: used to compare their performance.  
- 30 original held-out test samples: **untouched** during this comparison.

### Notebook cell 4 — One controlled comparison

X\_fit, X\_val, y\_fit, y\_val \= train\_test\_split(

    X\_train, y\_train,

    test\_size=0.25,

    random\_state=42,

    stratify=y\_train,

)

for neurons in \[8, 12\]:

    candidate \= make\_pipeline(

        StandardScaler(),

        MLPClassifier(

            hidden\_layer\_sizes=(neurons,),  \# Only setting changed

            activation="relu",

            solver="adam",

            learning\_rate\_init=0.01,

            alpha=0.01,

            max\_iter=1200,

            random\_state=42,

        ),

    )

    candidate.fit(X\_fit, y\_fit)

    validation\_accuracy \= candidate.score(X\_val, y\_val)

    last\_loss \= candidate.named\_steps\["mlpclassifier"\].loss\_curve\_\[-1\]

    print(

        f"Hidden neurons: {neurons}; "

        f"validation accuracy: {validation\_accuracy:.3f}; "

        f"last training loss: {last\_loss:.4f}"

    )

**Interpretation:** If one candidate scores higher on validation data, that is a reason to investigate it further, but one small split does not prove that the difference will be consistent. If both candidates tie, a student might prefer the smaller architecture for simplicity. In this prepared lesson, we **keep the original eight-neuron model** from Cell 2 as the fixed model for final evaluation. We do not select a model after seeing test results.

**Reader action:** Change `hidden_layer_sizes=(12,)` to `(16,)` in the optional comparison only. Run the two candidates again, then explain whether the validation result changed. Do not claim the change improved general performance without evidence from proper repeated evaluation.

**Chapter 15 takeaway:** A small neural network can be trained with a prepared notebook when data are split carefully, preprocessing is fitted on training examples only, and optional comparisons use validation rather than the final test set.

---

# Chapter 16 — Evaluating and Using Neural Networks Responsibly

**Starting problem:** *If a network performs well on classroom flower data, can we trust it on every new example?*

Once training is complete and our model settings are fixed, we can examine the original **30 held-out flowers**. These observations were not part of the model's fitting process. They provide a more meaningful check than testing only on the same flowers used for training.

**Learning objective:** Compute interpretable held-out results, compare against a simple baseline, identify limitations, and describe why real-world AI requires more than a good classroom accuracy score.

## 16.1 Evaluate held-out predictions using accuracy, a confusion matrix, and a majority-class baseline

### Accuracy

**Accuracy** is the fraction of predictions that match the known labels:

\[ \\text{Accuracy} \= \\frac{\\text{Number of correct predictions}}{\\text{Total predictions}}. \]

For example, if a model correctly identifies 29 of 30 flowers, its accuracy is `29 / 30 ≈ 0.967`, or about **96.7%**.

### Confusion matrix

A **confusion matrix** is a table that records actual classes against predicted classes. In scikit-learn's `confusion_matrix`, **rows correspond to actual labels** and **columns correspond to predicted labels**. Correct predictions appear along the main diagonal.

### Majority-class baseline

A **baseline** is a deliberately simple comparison method. A `DummyClassifier(strategy="most_frequent")` predicts the most frequent class found in the **training set** regardless of the flower measurements. Our stratified Iris training set contains equal class counts, so a fixed tie-breaking rule selects one of the classes. On the balanced 30-sample test split, predicting that one class produces **10 correct guesses out of 30** (about **33.3%**). The purpose is not to build a useful classifier: it is to show why a model should be compared with something simpler than itself.

### Notebook cell 5 — Evaluate once on the held-out test data

Run this **after** Cells 1–3 (and optionally 4). `model` still refers to the original fixed eight-neuron pipeline trained on all 120 training samples.

from sklearn.dummy import DummyClassifier

from sklearn.metrics import accuracy\_score, confusion\_matrix

\# Final held-out predictions: do not use these to tune the model.

y\_pred \= model.predict(X\_test)

held\_out\_accuracy \= accuracy\_score(y\_test, y\_pred)

baseline \= DummyClassifier(strategy="most\_frequent")

baseline.fit(X\_train, y\_train)

baseline\_pred \= baseline.predict(X\_test)

baseline\_accuracy \= accuracy\_score(y\_test, baseline\_pred)

print("Training accuracy:", round(model.score(X\_train, y\_train), 3))

print("Held-out accuracy:", round(held\_out\_accuracy, 3))

print("Majority-class baseline:", round(baseline\_accuracy, 3))

print("Class order:", list(class\_names))

print("Confusion matrix (actual rows, predicted columns):")

print(confusion\_matrix(y\_test, y\_pred, labels=\[0, 1, 2\]))

### Worked results from a verified reference run

The prepared cells were run using **scikit-learn 1.8.0**, a 120/30 stratified split, seed `42`, and the exact MLP settings shown above. The resulting measurements were:

| Measurement | Observed result in this reference run |
| :---- | ----: |
| Training samples | 120 |
| Held-out test samples | 30 |
| Training accuracy | 118/120 \= **98.3%** |
| Held-out accuracy | 29/30 \= **96.7%** |
| Majority-class baseline accuracy | 10/30 \= **33.3%** |
| Completed training epochs | **288** |
| First recorded training loss | **1.1974** |
| Last recorded training loss | **0.0451** |

Confusion matrix from the same run, with class order `setosa`, `versicolor`, `virginica`:

| Actual ↓ / Predicted → | setosa | versicolor | virginica |
| :---- | ----: | ----: | ----: |
| setosa | 10 | 0 | 0 |
| versicolor | 0 | 9 | 1 |
| virginica | 0 | 0 | 10 |

**What does the matrix tell us?** Twenty-nine predictions lie on the diagonal. One example whose actual species is *versicolor* was classified as *virginica*. On this particular split the neural network performed better than the majority-class baseline. However, a small educational dataset and a single favorable split are **not** evidence of dependable performance in unrelated settings.

**Reproducibility note:** These are **measured outputs for the stated environment**, not universal promised results. Your machine's results should be recorded from your own run; software and numerical-environment differences can affect details.

### Notebook cell 6 — Inspect a misclassified flower if there is one

mistake\_indices \= \[

    i for i, (actual, predicted) in enumerate(zip(y\_test, y\_pred))

    if actual \!= predicted

\]

if mistake\_indices:

    i \= mistake\_indices\[0\]

    print("Test-set position:", i)

    print("Measurements:", X\_test\[i\].tolist())

    print("Actual:", class\_names\[y\_test\[i\]\])

    print("Predicted:", class\_names\[y\_pred\[i\]\])

else:

    print("No mistakes in this held-out split.")

In the verified reference run, the mistaken flower appeared at position `25` of `X_test`, with measurements `[6.7, 3.0, 5.0, 1.7]` (centimeters). Its true class was **versicolor** and the model predicted **virginica**. This is an observation from the actual run—not a made-up sample. If a different run makes no error, explain that outcome instead of manufacturing a misclassification.

## 16.2 Compare training and held-out results to explain overfitting and unfamiliar data

The **training score** describes performance on examples the model used to learn. The **held-out score** describes performance on reserved examples that the model did not use during fitting or parameter selection.

In the verified run, training accuracy was **98.3%**, while held-out accuracy was **96.7%**. The small difference by itself does not establish problematic overfitting. It is simply a comparison from one split. A **much larger and persistent** gap—with strong training results but weak validation or test results—can be a sign of overfitting.

### Common risks to generalization

| Risk | Meaning | Why it matters |
| :---- | :---- | :---- |
| Overfitting | Model captures training-specific details that do not generalize | Training results can look deceptively strong |
| Underfitting | Model has not captured useful relationships | Both training and new-data predictions can be poor |
| Data leakage | Information from evaluation data influences model fitting or selection | Performance may look artificially optimistic |
| Distribution shift | Real-world inputs differ from training examples | The model may encounter patterns it never learned |
| Small evaluation set | Too few examples to establish stable performance | Accuracy can change greatly after only one different prediction |

For our 30-example held-out set, one additional wrong prediction changes accuracy by about **3.33 percentage points**. This is a useful reminder to interpret a single number carefully.

**An important distinction:** Holding out a test set improves the evaluation process, but it does not make a model automatically representative of every situation. Before deploying a model for a consequential decision, developers need more representative evidence and domain-specific testing.

### Reader exercise — Is this overfitting?

A hypothetical model has 99% accuracy on its training data and 62% accuracy on a properly separated validation set. What might be happening? **Answer:** A large training–validation gap could indicate overfitting, but we should also investigate possible data mismatch, data problems, and the reliability of the validation sample.

## 16.3 Explore applications and responsible use of neural networks

Neural networks are used to process patterns in many settings, including some kinds of image analysis and driver-assistance software. The broad connection is that models use learned patterns to transform input information into predictions or decisions. But different applications have very different levels of risk, and a classroom Iris classifier provides **no evidence** that a model would be suitable for safety-critical use.

### Example A — Image recognition

Suppose a system is trained to classify objects in photos. If most training photos are taken under bright lighting, its performance might degrade in dim lighting. It might also be less reliable for objects that are rarely represented in its training data. Improving it may require better and more varied data, systematic evaluation, and documentation of what the model can and cannot recognize.

### Example B — Driving assistance in fog

Imagine a driver-assistance system trained mainly on clear-weather road images. In heavy fog, the image may be much less informative. The system could have difficulty recognizing lane markings or road users. A responsible evaluation process would investigate such conditions **before** any safety-related deployment, rather than assuming clear-weather performance carries over.

This example is about **limitations and safety**, not instructions for operating or testing vehicles. Actual driving-assistance systems must be assessed through rigorous, domain-specific safety processes and appropriate human oversight.

### What does responsible use involve?

1. **Representative evaluation:** Test on data and conditions relevant to the intended application, including less common but important cases.  
2. **Fairness and unequal error rates:** Check whether errors are concentrated in particular groups or conditions when applicable to the task.  
3. **Privacy and permission:** Collect and use personal or sensitive data only with suitable justification, safeguards, and authorization.  
4. **Transparency:** Explain the model's intended use, limitations, and the evidence supporting performance claims.  
5. **Human oversight:** Ensure people can recognize, question, and appropriately respond to unreliable outputs, especially for consequential uses.  
6. **Careful communication:** Distinguish a classroom example, an illustrative number, and a result observed in a real experiment.

### Worked discussion — What further evidence is needed?

A team reports that a classifier works well on a clear, small dataset and proposes using a similar approach for real-world driving assistance. What questions should the team answer before claiming safety?

**Discussion prompts:** Are the examples representative of fog, darkness, unusual road layouts, and other operating conditions? What happens when the model is uncertain or wrong? How were evaluation data kept independent? What tests, monitoring, system safeguards, and human-control provisions are required by the specific application?

**Answer / key insight:** A single accuracy value from the Iris task cannot answer these questions. Testing must match the risks of the application, and appropriate oversight remains essential.

**Chapter 16 takeaway:** Evaluate neural networks with genuinely held-out data, meaningful baselines, and interpretable errors; do not mistake good classroom results for guaranteed reliability in unfamiliar or high-stakes environments.

---

# Unit IV — Consolidated Learning Review

## How the four chapters connect

| Chapter | Main question | Demonstration | Learner skill |
| :---- | :---- | :---- | :---- |
| 13 | How do we measure error? | Target `1`; predictions `0.8`, `0.6` | Compare squared errors; interpret a loss curve |
| 14 | How can a network learn? | Forward/loss/backward/update diagram | Explain gradient descent and backpropagation |
| 15 | How do we train a classifier? | Iris MLP with scaling pipeline | Run a prepared model; keep test data untouched |
| 16 | How do we check and use results responsibly? | Held-out accuracy, confusion matrix, baseline | Evaluate errors and discuss limitations |

**One connected workflow:**

Four Iris measurements \+ labeled training examples

                     │

                     ▼

           Fit training-only scaler

                     │

                     ▼

          MLP learns its parameters

      (prediction → loss → gradients → update)

                     │

                     ▼

        Apply trained pipeline to held-out data

                     │

                     ▼

   Predictions → accuracy → confusion matrix → compare baseline

                     │

                     ▼

          Interpret limitations responsibly

## Unit IV self-check questions

**Q1.** What is the difference between a predicted class and a correct label?  
**Q2.** If the target is 1 and the prediction is 0.6, what is the squared error?  
**Q3.** Why is squared error in Chapter 13 called an *illustration* instead of the exact Iris MLP training loss?  
**Q4.** What information does a training loss curve provide, and what does it **not** prove?  
**Q5.** Put these in order: backpropagation, weight update, forward pass, loss computation.  
**Q6.** Why is a learning rate needed?  
**Q7.** What is the purpose of a training-only `StandardScaler` inside a pipeline?  
**Q8.** Which set should be used for a one-setting comparison: validation or final test? Why?  
**Q9.** What does a confusion-matrix cell outside the main diagonal represent?  
**Q10.** If 29 out of 30 test predictions are correct, what is the accuracy?  
**Q11.** What might a large training-versus-validation performance gap indicate?  
**Q12.** Why can't Iris accuracy establish the safety of a driving-assistance system?

### Answer key

1. A predicted class is the model's selected category; a correct label is the known answer used for training or evaluation.  
2. `(1 - 0.6)² = 0.16`.  
3. The actual classification MLP uses a classification objective based on cross-entropy/log loss, not the teaching-only one-output squared-error calculation.  
4. It shows how the recorded training objective changes. By itself, it does not establish performance on unseen examples.  
5. Forward pass → loss → backpropagation → weight update.  
6. It controls update size and influences learning behavior.  
7. It learns scaling statistics from training examples and reuses them consistently, helping prevent test-data leakage.  
8. Validation data; reserving the final test set protects its independence for final evaluation.  
9. A misclassification: a prediction of one class for an example whose actual label is another class.  
10. `29 / 30 ≈ 96.7%`.  
11. Possible overfitting, data mismatch, or another evaluation/data issue.  
12. It is a different dataset and task with much lower stakes; road conditions and safety requirements need separate evidence and safeguards.

## Short glossary

| Term | Definition |
| :---- | :---- |
| Prediction | Output generated by a model for an input |
| Target / label | Known correct answer in supervised learning |
| Loss function | Numerical objective that training attempts to reduce |
| Squared error | Square of the difference between a numerical target and prediction |
| Cross-entropy / log loss | Classification loss based on the model's assigned probability to the true class |
| Gradient descent | Optimization approach using gradients to guide parameter updates |
| Learning rate | Setting that influences update step size |
| Backpropagation | Efficient computation of gradients through a neural network |
| Epoch | One pass over training data in the relevant stochastic-training setup |
| Multilayer perceptron (MLP) | Feedforward neural network made of connected layers |
| StandardScaler | Transformer that standardizes each feature using fitted statistics |
| Pipeline | Ordered combination of preprocessing and estimator operations |
| Validation set | Data used to compare decisions about model settings |
| Held-out test set | Reserved data used to evaluate the finalized model |
| Accuracy | Proportion of correct predictions |
| Confusion matrix | Counts of actual versus predicted classes |
| Baseline | Simple reference method used for comparison |
| Overfitting | Fitting training-specific detail that does not transfer well |
| Data leakage | Unintended use of evaluation information during model fitting or selection |
| Distribution shift | Difference between conditions represented in training and later inputs |

## Suggested PPT and video demonstrations

**Demonstration A — Loss (Chapter 13):** Ask two students to calculate `(1 - 0.8)²` and `(1 - 0.6)²`. Show why a smaller error corresponds to the closer numerical answer. Clearly caption this as an illustrative one-output example, not MLP classification loss.

**Demonstration B — Training loop (Chapter 14):** Present the forward pass → loss → backpropagation → update diagram. Ask learners which stage makes the network's next computations potentially different.

**Demonstration C — Notebook (Chapters 15–16):** Run the Iris notebook, show the training-loss curve, then reveal held-out accuracy, the majority-class baseline, and the confusion matrix. Explain the one error found in the reference run, if reproduced.

The video tutorials may demonstrate **selected ideas** rather than narrating every line of the study guide. The PPT should summarize the same definitions, sample counts, and verified outputs.

## Bridge to Unit V — Integration and Guided Project

Unit II introduced data structures and core algorithms. Unit III explained how neural networks compute outputs. Unit IV showed how those networks learn from examples and how we evaluate predictions. **Unit V now brings these ideas together in one Flower Prediction Explorer.** We will store measurement records and model predictions, find a sample by ID, sort results using a chosen feature, and demonstrate how ordinary algorithms work alongside a learned classifier.

**Next chapters:** Chapter 17 — Connecting Data Structures, Algorithms, and AI; Chapter 18 — Guided Project: Flower Prediction Explorer.

---

# Instructor / Team Production Notes

- **Outline alignment:** Chapters 13–16 and exactly **three numbered subtopics per chapter** follow PentaByte's supplied 25 October 2026 focused project outline. Content follows **problem → essential idea → worked example → reader action → takeaway**.  
- **Scope:** No neural-network implementation from scratch, no matrix-calculus derivations, no advanced architecture survey, and no unrelated dataset. The Iris task is the shared example that connects Units III–V.  
- **Train/test discipline:** Cells 1–3 fit on only the 120 training examples. Cell 4 is an **optional** validation comparison using subsets of those 120 training examples. Only Cell 5 evaluates the fixed original model on the untouched 30 examples. Do not report the 30 validation samples as the final test samples.  
- **Reference outputs:** The observed results table was computed using scikit-learn **1.8.0**. Rerun the notebook in the team's own environment and label any changed outputs before publication.  
- **Interpretation:** The one-output squared-error examples and the early loss curve are **illustrative**; the classifier results in Chapter 16 are **measured** from the stated local run. The two should not be mixed in a single graphic without captions.  
- **Reader support:** Place larger runnable cells in a shared Python notebook if possible. Keep a compact version of the core lessons in the final study guide and reuse the same sample counts, confusion-matrix orientation, and species names in slides and videos.  
- **Quality assurance:** A teammate should run all notebook cells from a fresh environment, check the answer key, inspect the held-out-results table, and confirm that no step fits preprocessing on test data.  
- **Source credits:** Credit the Iris dataset and scikit-learn documentation in the final repository and include any course-required AI-use disclosure.

## References and additional reading

1. scikit-learn. **MLPClassifier API reference** — parameters, loss history, and optimization behavior: [https\://scikit-learn.org/stable/modules/generated/sklearn.neural\_network.MLPClassifier.html](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)  
2. scikit-learn. **Neural network models (supervised)** — MLP classification and backpropagation: [https\://scikit-learn.org/stable/modules/neural\_networks\_supervised.html](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)  
3. scikit-learn. **Common pitfalls** — data leakage, consistent preprocessing, and proper evaluation: [https\://scikit-learn.org/stable/common\_pitfalls.html](https://scikit-learn.org/stable/common_pitfalls.html)  
4. scikit-learn. **Pipeline** — combining a transformer and an estimator: [https\://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)  
5. scikit-learn. **Iris dataset** — feature names and target labels: [https\://scikit-learn.org/stable/modules/generated/sklearn.datasets.load\_iris.html](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)  
6. scikit-learn. **train\_test\_split** — reproducible and stratified train/test splitting: [https\://scikit-learn.org/stable/modules/generated/sklearn.model\_selection.train\_test\_split.html](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)  
7. scikit-learn. **confusion\_matrix** — actual/predicted axis conventions: [https\://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion\_matrix.html](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)  
8. scikit-learn. **DummyClassifier** — simple baseline predictions: [https\://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)

**End of Unit IV — Connectionist AI: Learning, Testing, and Applications**