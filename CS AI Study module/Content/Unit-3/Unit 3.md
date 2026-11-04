# PentaByte — Detailed Learning Content (Version 3.0)

## Algorithms, Data Structures, and Connectionist AI

### A Beginner's Guide to Learning Through Problems

**Unit III:** Connectionist AI: Data, Neurons, and Networks  
**Chapters:** 9–12  
**Team:** PentaByte  
**Based on:** Focused Project Content Outline, 25 October 2026  
**Audience:** Beginning university students with little or no programming experience  
**Example language:** Python 3; an optional scikit-learn dataset demonstration  
**Document type:** Detailed Markdown lesson draft; suitable for reuse in the study guide, PPT, and video demonstrations

---

# Unit III — Connectionist AI: Data, Neurons, and Networks

## Unit Introduction

In Units I and II, we learned to express problems as algorithms, write small Python programs, organize information, and search through structured data. Most of those examples followed **rules designed directly by a programmer**. For example, an algorithm could search a list or compare two scores because we explicitly described the steps.

A different question is: **Can a computer learn useful patterns from examples rather than being given a separate rule for every situation?** This question brings us to machine learning and, more specifically, **connectionist AI**—approaches that use networks of connected artificial neurons.

We will return to a single example throughout the next four chapters: **identifying a type of Iris flower from measurements**. We first contrast hand-written rules and learned patterns, then identify the measurements and labels that a classifier uses. Next, we calculate the output of one artificial neuron. Finally, we connect a few neurons into a small illustrative feedforward network and trace a prediction.

**Unit pathway:**

`Fixed rules versus learned patterns → Samples and features → One artificial neuron → Connected neurons and output scores`

**After completing Unit III, learners should be able to:**

1. Distinguish a hand-written classification rule from a model that learns from labeled examples.  
2. Explain why neural networks are called connectionist systems.  
3. Identify samples, input features, target labels, training data, and held-out test data in the Iris dataset.  
4. Calculate the weighted sum, bias, and ReLU output of one artificial neuron.  
5. Trace a small feedforward network from input values through a hidden layer to class scores.  
6. Explain why an illustrative output score is not automatically a calibrated probability or proof of accurate classification.

**Learning boundary:** We explain **what** a neural network computes, not how to build or train a complete network from scratch. Training, loss, backpropagation, model evaluation, and a working Iris classifier are covered in Unit IV. Python examples in Chapters 9, 11, and 12 require only the standard library; the optional dataset exploration in Chapter 10 uses scikit-learn.

---

# Chapter 9 — AI, Machine Learning, and Connectionism

**Starting problem:** *Can a program recognize a flower from measurements instead of relying on a long list of fixed rules?*

Imagine a student measures a flower's sepal length, sepal width, petal length, and petal width. The student wants a program to predict which Iris species the flower belongs to. There are at least two broad approaches: we could **write the decision rules ourselves**, or we could **provide labeled examples** from which a model learns patterns.

**Learning objective:** Compare these approaches and understand where artificial neural networks fit into machine learning.

## 9.1 Compare fixed, rule-based decisions with systems that learn patterns from examples

A **rule-based program** follows conditions written by a human. These rules might be useful when the decision process is easy to describe. In Unit I, we used the rule `if score >= pass_mark` to decide whether a score met a threshold. The program did not discover that rule: a person supplied it.

For a flower, we could invent a **teaching-only rule**:

> If the petal length is below 2.0 cm, return “setosa-like”; otherwise, return “undetermined.”

This is intentionally limited. It is not a scientifically validated identification procedure and it does **not** recognize all three Iris species.

\# A simplified, hand-written example—not a trained ML model.

def simple\_flower\_rule(petal\_length\_cm):

    if petal\_length\_cm \< 2.0:

        return "setosa-like"

    return "undetermined"

print(simple\_flower\_rule(1.4))

print(simple\_flower\_rule(4.7))

**Expected output:**

setosa-like

undetermined

The rule makes its decision using **one measurement** and a **threshold selected in advance**. Its behavior is easy to explain but limited: the second flower receives no specific species prediction. If a new measurement does not fit our simple expectations, we would need to reconsider the rule.

A **machine-learning model** works differently. During *training*, a learning algorithm uses examples, their features, and—when doing supervised classification—their correct labels to adjust the model's parameters. Later, during *prediction* (also called **inference**), the model receives a new set of features and returns a result using the patterns represented by those learned parameters.

| Question | Hand-written rule | Learned classifier |
| :---- | :---- | :---- |
| Where does the decision process come from? | A programmer explicitly specifies conditions. | A learning algorithm adjusts model parameters using examples. |
| What data is needed to design it? | Rules may come from domain knowledge and testing. | Training requires suitable examples; supervised learning also uses labels. |
| How does the decision change? | A programmer edits the conditions. | Parameters can be updated through training or retraining. |
| Can it make mistakes? | Yes; the rules can be incomplete or wrong. | Yes; the training data or learned patterns can be inadequate. |
| Does it always learn better rules? | Not applicable. | No. Good results must be verified on suitable held-out data. |

**Important:** Not every problem needs machine learning. If a clear rule solves a simple task reliably, such as checking whether a number is above a specified threshold, the rule may be more appropriate.

### Worked comparison

Suppose a program receives petal length `4.7 cm` and petal width `1.4 cm`. Our hand-written rule only says **“undetermined.”** A *trained* classifier, by contrast, can consider both these and other measurements when assigning one of its learned class labels. We cannot state what a specific trained classifier would output without running and evaluating that classifier.

## 9.2 Introduce machine learning and connectionism: networks of connected artificial neurons

**Artificial intelligence (AI)** is a broad area concerned with computational systems that perform tasks associated with intelligent behavior, such as recognizing patterns, reasoning, planning, or understanding information.

**Machine learning (ML)** is an approach within AI in which models learn patterns from data rather than relying only on rules that programmers write by hand.

**Connectionist AI** emphasizes computation through networks of many connected processing units, commonly called **artificial neurons**. Artificial neural networks are an important example of connectionist systems.

A useful simplified relationship is:

Artificial Intelligence (broad field)

    └── Machine Learning (learning patterns from data)

          └── Artificial Neural Networks (connectionist models)

This is a teaching map, **not** a complete classification of every AI approach: some AI systems are not machine-learning systems, and some machine-learning methods do not use neural networks.

An artificial neuron is a mathematical processing unit. It receives numeric inputs, combines them using **weights** and a **bias**, and often applies an **activation function**. A network connects many such units so that the output of one layer can become the input of another.

Measurements     Connected processing units      Result

     x1  ──┐

     x2  ──┼────► \[ neuron \] ──► \[ neuron \] ──► class scores

     x3  ──┤

     x4  ──┘

This diagram conveys the overall idea. Chapter 11 will calculate one neuron, and Chapter 12 will show how several neurons can be connected.

**Where does learning happen?** In many neural-network systems, the values of weights and biases are adjusted during training. At prediction time, those learned values are used to process new inputs. This unit focuses on **prediction computation**; Unit IV explains how the parameters are adjusted.

## 9.3 Follow a simple classification task from measured features to a predicted label

A **classification task** asks a model to select a category from a known set of possible categories. Here, the categories are the three Iris species in the commonly used dataset: **setosa**, **versicolor**, and **virginica**.

The basic prediction workflow is:

Flower to examine

       ↓

Measure its four features

       ↓

Provide numerical features to a previously trained model

       ↓

Model computes output scores / prediction

       ↓

Map predicted class index to a species name

The flower's **actual species label** is not supplied as an input when predicting its species; it is the answer that the classifier is trying to infer. During supervised training, correct labels are used to evaluate and improve predictions.

### Worked example — From measurements to a category

Consider the numerical measurements of one known Iris example:

| Feature | Measurement |
| :---- | ----: |
| Sepal length | 5.1 cm |
| Sepal width | 3.5 cm |
| Petal length | 1.4 cm |
| Petal width | 0.2 cm |

This is the first example in the standard Iris dataset; its known label is **setosa**. The measurements are the **inputs**. The label is the **target answer** used to check or teach a classifier—not a fifth measurement to feed into it.

**Reader action — Predict and discuss:**

1. Explain who chose the condition in `simple_flower_rule`.  
2. Identify what a trained classifier would need at prediction time for this flower.  
3. What might happen if an unfamiliar flower differs substantially from the examples used in training?

**Answer / hint:** (1) A programmer chose the condition. (2) It needs the numeric measurements in the same feature order and preparation format used for training, plus its already learned parameters. (3) The prediction may be unreliable; a model can make confident-looking errors on unfamiliar data.

**Chapter 9 takeaway:** A rule-based program follows instructions written explicitly by a human, whereas a machine-learning classifier uses patterns learned from examples; neural networks are connectionist models that combine inputs through connected artificial neurons.

---

# Chapter 10 — Learning from Data: Features, Labels, and Examples

**Starting problem:** *What information does a neural network need before it can learn to classify flowers?*

Before we can understand a network's prediction, we must understand **what the input numbers mean**. A dataset is more than a table: its structure determines which values the model may use to make a prediction and which values represent the correct answers for learning and evaluation.

**Learning objective:** Read a simple classification dataset, identify its features and labels, and distinguish data used for training from data reserved for testing.

## 10.1 Identify samples, numerical features, and species labels in the Iris dataset

The commonly used **Iris dataset** contains **150 flower samples**, with **50 samples for each of three species** and **four numerical features per sample**. It is a small, beginner-friendly dataset widely used to demonstrate classification.

| Dataset term | Meaning | Iris example |
| :---- | :---- | :---- |
| Sample / observation | One recorded example | Measurements of one flower |
| Feature | An input variable used to make a prediction | Sepal length (cm) |
| Feature vector | The feature values for one example | `[5.1, 3.5, 1.4, 0.2]` |
| Label / target | The known answer for an example | `setosa` |
| Class | One of the permitted output categories | `setosa`, `versicolor`, `virginica` |
| Dataset | Collection of samples with their recorded information | 150 labeled Iris observations |

The four features, all measured in **centimeters**, are:

1. **Sepal length** — length of a sepal.  
2. **Sepal width** — width of a sepal.  
3. **Petal length** — length of a petal.  
4. **Petal width** — width of a petal.

A **feature vector** stores the numbers in a specific order. This order matters: if a model expects `[sepal length, sepal width, petal length, petal width]`, swapping the first and third values changes the meaning of the input.

**One sample as a student-friendly record:**

flower \= {

    "sepal\_length\_cm": 5.1,

    "sepal\_width\_cm": 3.5,

    "petal\_length\_cm": 1.4,

    "petal\_width\_cm": 0.2,

    "species": "setosa"  \# Known answer; not an input feature

}

features \= \[

    flower\["sepal\_length\_cm"\],

    flower\["sepal\_width\_cm"\],

    flower\["petal\_length\_cm"\],

    flower\["petal\_width\_cm"\],

\]

label \= flower\["species"\]

print("Features:", features)

print("Label:", label)

**Expected output:**

Features: \[5.1, 3.5, 1.4, 0.2\]

Label: setosa

**Optional prepared-dataset notebook cell (requires scikit-learn):**

from sklearn.datasets import load\_iris

iris \= load\_iris()

X \= iris.data      \# Input features (150 rows × 4 columns)

y \= iris.target    \# Correct class index for each row

print("Samples and features:", X.shape)

print("Labels:", y.shape)

print("Species:", \[str(name) for name in iris.target\_names\])

print("First measurements:", X\[0\].tolist())

print("First label:", iris.target\_names\[y\[0\]\])

**Expected output:**

Samples and features: (150, 4\)

Labels: (150,)

Species: \['setosa', 'versicolor', 'virginica'\]

First measurements: \[5.1, 3.5, 1.4, 0.2\]

First label: setosa

`X` represents the input measurements and `y` contains the known labels. We use a separate target array because **the correct answer must not be smuggled into the model's inputs**.

## 10.2 Explain the difference between training data and held-out test data

When supervised machine learning is used, we normally want a model that works on **new examples**, not one that merely reproduces answers for examples it has already seen. That is why a dataset is often separated into different parts.

- **Training data:** The model learns patterns from these examples and their labels.  
- **Held-out test data:** These examples are kept aside while the model is being trained and tuned. They are used to estimate how the finished model performs on unseen examples.  
- **Validation data (when used):** A separate portion of the training data helps compare settings without using the final test set for those decisions. We use this idea later in Unit IV.

A straightforward introductory demonstration uses **80% training data** and **20% test data**. In the Iris dataset that would be **120 training flowers** and **30 test flowers**. These numbers are illustrative of one chosen split; there is no universal requirement to use 80/20.

**Concept diagram:**

                  150 Iris samples

                         \|

           \+-------------+--------------+

           \|                            \|

       TRAINING DATA                 HELD-OUT TEST DATA

        120 samples                     30 samples

     learn model parameters        assess final performance

           \|                            \|

     used during training       not used to fit/tune the model

**Optional executable split (requires scikit-learn):**

from sklearn.datasets import load\_iris

from sklearn.model\_selection import train\_test\_split

iris \= load\_iris()

X\_train, X\_test, y\_train, y\_test \= train\_test\_split(

    iris.data,

    iris.target,

    test\_size=0.20,

    random\_state=42,

    stratify=iris.target,

)

print("Training samples:", len(X\_train))

print("Test samples:", len(X\_test))

**Expected output:**

Training samples: 120

Test samples: 30

In this example, `random_state=42` makes the selected random split reproducible, while `stratify=iris.target` keeps the class proportions approximately consistent between the subsets. Since the Iris dataset is evenly divided into three classes, each resulting subset has equal representation from the classes in this particular split.

**Avoiding a common mistake — data leakage:** If test answers influence training decisions or settings, the test results are no longer a clean check of performance on unseen data. For example, repeatedly trying different models and picking whichever obtains the best test accuracy is a form of test-set misuse. Another mistake would be including a flower's species label among the numerical input features.

**Preparation reminder:** If later code scales or normalizes input values using learned statistics (such as the mean and standard deviation), compute those statistics **from training data only**, and then apply the same transformation to test data. Chapter 15 will demonstrate that process in a supplied notebook.

## 10.3 Explore why useful measurements, suitable examples, and careful data preparation matter

A model's results depend partly on the quality and suitability of the information it receives.

**Relevant features.** A feature should carry useful information about the classification task. For Iris flowers, sepal and petal measurements are more relevant than an unrelated sample identification number.

**Consistent meaning and units.** Mixing centimeters and millimeters without conversion would produce incompatible numbers. Likewise, inconsistent column order can make correct measurements appear to represent the wrong feature.

**Complete and reasonable records.** Missing or incorrectly entered measurements need appropriate handling. A blank petal width should not silently be treated as a measured zero.

**Suitable and representative examples.** A model trained only on a narrow set of observations may not work well for flowers with substantially different characteristics or measurement conditions. A small classroom dataset is useful for learning, but does not guarantee reliable real-world deployment.

**Keeping the label separate.** Labels tell us whether predictions were correct during supervised training and evaluation. They must not be presented as inputs when asking the model to infer those same labels.

### Worked example — Which columns belong in the inputs?

| Sample ID | Sepal length | Sepal width | Petal length | Petal width | Species label |
| :---- | ----: | ----: | ----: | ----: | :---- |
| F001 | 5.1 | 3.5 | 1.4 | 0.2 | setosa |
| F002 | 6.0 | 2.9 | 4.5 | 1.5 | versicolor |
| F003 | 6.3 | 3.3 | 6.0 | 2.5 | virginica |

The table uses known-style measurements **for teaching and record organization**, not a newly sampled dataset or evidence of a model's accuracy. The four numeric measurement columns are inputs; the species column is the target. `Sample ID` is for identifying the record in our future results explorer, not for predicting the flower's species.

For **F002**:

Input features: \[6.0, 2.9, 4.5, 1.5\]

Known target:   versicolor

**Reader action — Identify and correct:**

1. Identify the four input features and the target label for F003.  
2. Explain why a class label cannot be supplied as a fifth input feature when we want to predict that label.  
3. A teammate converts petal length from centimeters to millimeters but changes no other units. Why can this create a problem?  
4. Why should the final test examples stay unseen during the training and settings-selection process?

**Answer / hint:** (1) `[6.3, 3.3, 6.0, 2.5]`, target `virginica`. (2) That reveals the answer instead of requiring the model to learn the relationship. (3) The model would receive an inconsistent numerical scale and potentially misinterpret the inputs. (4) To make the test result a more meaningful estimate of performance on new examples.

**Chapter 10 takeaway:** A classification dataset separates **features**, which a model uses as inputs, from **labels**, which are the answers to learn and evaluate; the training/test split helps check whether the resulting model generalizes beyond its training examples.

---

# Chapter 11 — Artificial Neurons: Weights, Bias, and Activation

**Starting problem:** *How can a few measurements be combined into one useful signal?*

A neural network is built from simple calculations that are repeated and connected. Before tracing a complete network, we can understand one **artificial neuron**. The neuron receives numbers, assigns weights to them, adds a bias, and applies an activation function.

**Learning objective:** Identify an artificial neuron's components, calculate its result, and predict how changing a weight or bias affects the output.

## 11.1 Identify the inputs, weights, and bias in a simple artificial neuron

Consider one artificial neuron that receives two numerical inputs:

- `x1`: first input value  
- `x2`: second input value  
- `w1`: weight multiplying `x1`  
- `w2`: weight multiplying `x2`  
- `b`: bias added after combining the weighted inputs

Its weighted sum is:

\[ z \= w\_1x\_1 \+ w\_2x\_2 \+ b \]

The output of the neuron is often written as:

\[ a \= f(z) \]

Here, `f` is an **activation function**. For now, think of the weighted sum as the combined numerical signal and the activation function as a transformation applied to that signal.

  x1 \= 2 ──(w1 \= 0.5)──┐

                       ├──► \[ add weighted inputs \+ bias \] ──► z ──► \[ReLU\] ──► a

  x2 \= 3 ──(w2 \= \-1)───┘                     ↑

                                         b \= 1

**What the parts mean:**

| Part | Function in the calculation | Example |
| :---- | :---- | :---- |
| Input | Number supplied to the neuron | `x1 = 2` |
| Weight | Multiplies an input, changing its contribution | `w1 = 0.5` |
| Bias | Shifts the combined value before activation | `b = 1` |
| Weighted sum | Sum of weighted inputs plus bias | `z = -1` |
| Activation | Converts `z` to neuron output | `ReLU(-1) = 0` |

Positive and negative weights can contribute in different directions to the weighted sum. Their effect depends on the input values and the rest of the computation. **A weight is not itself a probability or a measure of human importance.**

## 11.2 Calculate a weighted sum and apply a simple activation function such as ReLU

For this guide, we use the **Rectified Linear Unit (ReLU)** function:

\[ \\operatorname{ReLU}(z) \= \\max(0, z) \]

It returns `0` when the input is negative and leaves a positive input unchanged. At `z = 0`, the output is also `0`.

| Input to ReLU (`z`) | Output |
| ----: | ----: |
| \-4 | 0 |
| \-1 | 0 |
| 0 | 0 |
| 2 | 2 |
| 5 | 5 |

### Worked calculation — An artificial neuron

Use the values from the project outline:

\[ x\_1=2,\\quad x\_2=3,\\quad w\_1=0.5,\\quad w\_2=-1,\\quad b=1 \]

**Step 1 — Multiply each input by its weight.**

\[ w\_1x\_1 \= 0.5\\times2=1 \]

\[ w\_2x\_2 \= \-1\\times3=-3 \]

**Step 2 — Add the weighted contributions and the bias.**

\[ z=1+(-3)+1=-1 \]

**Step 3 — Apply ReLU.**

\[ a=\\operatorname{ReLU}(-1)=\\max(0,-1)=\\boxed{0} \]

**Runnable Python demonstration:**

def relu(value):

    return max(0.0, value)

x1, x2 \= 2, 3

w1, w2 \= 0.5, \-1.0

bias \= 1.0

weighted\_sum \= x1 \* w1 \+ x2 \* w2 \+ bias

output \= relu(weighted\_sum)

print("Weighted sum:", weighted\_sum)

print("Neuron output:", output)

**Expected output:**

Weighted sum: \-1.0

Neuron output: 0.0

This result does not mean the inputs contain no information. It means the selected weighted sum is negative, and ReLU maps this particular sum to zero.

## 11.3 Change one weight or bias and explain how the output changes

The **bias** shifts the weighted sum. If we keep the inputs and weights unchanged but change the bias from `1` to `3`, the calculation becomes:

\[ z=0.5(2)+(-1)(3)+3=1-3+3=1 \]

\[ a=\\operatorname{ReLU}(1)=\\boxed{1} \]

Thus, changing just the bias changes the output from `0` to `1`.

**Trace table:**

| Experiment | `w1` | `w2` | Bias | Weighted sum `z` | ReLU output |
| :---- | ----: | ----: | ----: | ----: | ----: |
| Original | 0.5 | \-1.0 | 1 | \-1.0 | 0.0 |
| Higher bias | 0.5 | \-1.0 | 3 | 1.0 | 1.0 |
| Changed second weight | 0.5 | \-0.5 | 1 | 0.5 | 0.5 |

**Runnable comparison:**

def relu(value):

    return max(0.0, value)

def neuron(x1, x2, w1, w2, bias):

    z \= x1 \* w1 \+ x2 \* w2 \+ bias

    return z, relu(z)

experiments \= \[

    ("Original", 0.5, \-1.0, 1.0),

    ("Higher bias", 0.5, \-1.0, 3.0),

    ("Changed weight", 0.5, \-0.5, 1.0),

\]

for name, w1, w2, bias in experiments:

    z, result \= neuron(2, 3, w1, w2, bias)

    print(f"{name}: z={z:.1f}, output={result:.1f}")

**Expected output:**

Original: z=-1.0, output=0.0

Higher bias: z=1.0, output=1.0

Changed weight: z=0.5, output=0.5

In a trained network, the values of weights and biases are usually obtained through a learning process rather than chosen by hand. Our calculations use **illustrative values** to show the mechanics. Unit IV will explain parameter updates conceptually, without requiring calculus derivations.

**Reader action — Modify one number:**

1. Keep all original values but change the bias to `2`. Calculate `z` and ReLU output before running any code.  
2. Keep the original bias of `1`, but change `w2` to `0`. Calculate the new output.  
3. Why can two different negative weighted sums produce the same ReLU output?

**Answer / hint:** (1) `z = 1 - 3 + 2 = 0`; output `0`. (2) `z = 1 + 0 + 1 = 2`; output `2`. (3) ReLU maps **every** negative input to zero.

**Chapter 11 takeaway:** An artificial neuron combines numerical inputs through weights and a bias, then passes the result through an activation function; changing its parameters can change the final output.

---

# Chapter 12 — Neural Network Layers and Forward Propagation

**Starting problem:** *How do several artificial neurons work together to make a prediction?*

An individual neuron produces only one output value. A **neural network** connects neurons so that several numerical signals can be transformed into a set of useful outputs. A simple feedforward network takes data at its input layer, processes it through one or more hidden layers, and computes an output.

**Learning objective:** Recognize a small network's layers, trace an example forward pass, and interpret class scores carefully.

## 12.1 Identify input, hidden, and output layers in a small feedforward neural network

A beginner-friendly network might have:

- **Input layer:** Holds the input features. In a full Iris example, there would be four input values corresponding to the four flower measurements.  
- **Hidden layer:** Contains artificial neurons that combine input values using weights, biases, and activation functions. Hidden layers perform intermediate calculations.  
- **Output layer:** Produces values interpreted according to the prediction task, such as one score for each species class.

For a compact arithmetic demonstration, we will use **two abstract inputs**, **two hidden neurons**, and **three output scores**. This is a *toy forward-pass diagram*, not a full trained Iris classifier. We reduce the number of inputs solely to make the arithmetic easy to follow.

            INPUTS                HIDDEN LAYER              OUTPUT SCORES

         x1 \= 2 ───────┬──────► \[ h1 \] ─────────┬──────► \[ setosa score \]

                      │                        ├──────► \[ versicolor score \]

         x2 \= 3 ───────┴──────► \[ h2 \] ─────────┴──────► \[ virginica score \]

                      Values flow LEFT → RIGHT

**Note about arrows:** The picture is conceptual: individual weighted connections and biases are specified in the worked example below. It is not a wiring diagram showing every connection separately.

A network with one hidden layer is a useful starting point. A network with **multiple hidden layers** is often called a **deep neural network**. Our guide does not explore specialized deep-learning architectures; that would be beyond the scope of the project.

One hidden layer:    Input → Hidden → Output

Three hidden layers: Input → Hidden 1 → Hidden 2 → Hidden 3 → Output

The word **feedforward** means information is computed from earlier layers toward later layers during a prediction pass, without feedback loops in that forward computation.

## 12.2 Trace forward propagation as values move from one layer to the next

**Forward propagation**, or a **forward pass**, is the sequence of calculations through which a network turns an input into output values. Each neuron takes numerical values from an earlier layer, computes a weighted sum plus a bias, applies the chosen activation, and passes its output forward.

### Worked example — Two inputs and two hidden neurons

Use input values:

\[ x\_1=2,\\qquad x\_2=3 \]

Choose two illustrative hidden neurons, each using ReLU:

- **Hidden neuron 1:** weight `1` for `x1`, weight `0` for `x2`, bias `0`.  
- **Hidden neuron 2:** weight `0` for `x1`, weight `1` for `x2`, bias `−1`.

**Hidden neuron 1:**

\[ z\_{h1}=1(2)+0(3)+0=2 \]

\[ h\_1=\\operatorname{ReLU}(2)=2 \]

**Hidden neuron 2:**

\[ z\_{h2}=0(2)+1(3)-1=2 \]

\[ h\_2=\\operatorname{ReLU}(2)=2 \]

Both hidden neurons have now produced an output of `2`.

**Intermediate results:**

| Hidden neuron | Weighted-sum calculation | Activation | Output |
| :---- | :---- | :---- | ----: |
| `h1` | `1(2) + 0(3) + 0 = 2` | ReLU | 2 |
| `h2` | `0(2) + 1(3) − 1 = 2` | ReLU | 2 |

Next, the **output layer** combines `h1` and `h2` to produce three **raw class scores**. To make the arithmetic transparent, choose the following output-layer weights and zero biases:

| Output class | Weight from `h1` | Weight from `h2` | Bias |
| :---- | ----: | ----: | ----: |
| setosa | 0.10 | 0.00 | 0 |
| versicolor | 0.10 | 0.25 | 0 |
| virginica | 0.00 | 0.05 | 0 |

Compute the scores:

\[ s\_{\\mathrm{setosa}}=0.10(2)+0.00(2)+0=\\boxed{0.2} \]

\[ s\_{\\mathrm{versicolor}}=0.10(2)+0.25(2)+0=\\boxed{0.7} \]

\[ s\_{\\mathrm{virginica}}=0.00(2)+0.05(2)+0=\\boxed{0.1} \]

The final score vector is:

\[ \\boxed{\[0.2,\\ 0.7,\\ 0.1\]} \]

This is exactly the illustrative score pattern described in the team outline. **These weights were chosen for teaching, not learned by training**, and the abstract input pair `(2, 3)` does not represent the full four-feature Iris record. We therefore must not report the result as an experimentally validated prediction for a real flower.

**Runnable Python forward pass (standard library only):**

def relu(value):

    return max(0.0, value)

\# Two abstract inputs for a toy numerical demonstration.

x1, x2 \= 2.0, 3.0

\# Hidden layer: two neurons.

h1 \= relu(1.0 \* x1 \+ 0.0 \* x2 \+ 0.0)

h2 \= relu(0.0 \* x1 \+ 1.0 \* x2 \- 1.0)

\# Output layer: raw scores, not automatically probabilities.

scores \= \[

    0.10 \* h1 \+ 0.00 \* h2,  \# setosa

    0.10 \* h1 \+ 0.25 \* h2,  \# versicolor

    0.00 \* h1 \+ 0.05 \* h2,  \# virginica

\]

print("Hidden outputs:", \[h1, h2\])

print("Class scores:", \[round(s, 1\) for s in scores\])

**Expected output:**

Hidden outputs: \[2.0, 2.0\]

Class scores: \[0.2, 0.7, 0.1\]

**What this demonstrates:** The outputs of the hidden neurons become inputs to the output calculations. Each output score is produced through an explicit, traceable sequence of numerical operations.

## 12.3 Read a small output-score example and identify the predicted class

A classifier can use the largest output score to choose a class. For our illustrative output scores:

| Class index | Species name | Raw score |
| ----: | :---- | ----: |
| 0 | setosa | 0.2 |
| 1 | versicolor | **0.7** |
| 2 | virginica | 0.1 |

The highest score is **0.7**, which occurs at index **1**. Mapping that index to the class names gives **versicolor** as the toy network's chosen label.

**Runnable prediction step:** This cell can run on its own; it uses the illustrative scores rather than relying on the previous code cell.

species \= \["setosa", "versicolor", "virginica"\]

scores \= \[0.2, 0.7, 0.1\]

best\_index \= max(range(len(scores)), key=lambda i: scores\[i\])

predicted\_label \= species\[best\_index\]

print("Highest-score class:", predicted\_label)

print("Highest raw score:", scores\[best\_index\])

**Expected output:**

Highest-score class: versicolor

Highest raw score: 0.7

### Are these probabilities?

**Not automatically.** The numbers are **raw illustrative scores**. They happen to add to `1.0` in this particular example, but **summing to 1 alone does not prove that they are valid or well-calibrated probabilities**. A network might use a suitable output transformation, such as softmax, to obtain values interpreted as class probabilities, and real-world probability calibration requires additional checking. Those details are beyond the current unit.

Similarly, the largest score does not guarantee that the chosen label is correct. The network used in this chapter has **not been trained**, and we have not tested it against held-out Iris samples. Unit IV will address training, evaluation, and limitations.

### Reader action — Predict and change

1. From `[0.2, 0.7, 0.1]`, identify the winning class and index.  
2. Change the scores to `[0.6, 0.3, 0.1]`. Which class would be selected?  
3. Keeping the original hidden outputs `h1 = h2 = 2`, change the output weight for **virginica** from `h2` to `0.40`, leaving its other weight and bias unchanged. What is the new virginica score, and which class now has the largest score?  
4. Explain why the winner in this toy example is **not evidence** that the network can correctly classify actual flowers.

**Answer / hint:** (1) Index `1`, `versicolor`. (2) Index `0`, `setosa`. (3) Virginica becomes `0.40 × 2 = 0.8`; it is now the highest score, so `virginica` is selected. (4) The weights were chosen by hand and the network was not trained or evaluated on the dataset.

**Chapter 12 takeaway:** A feedforward neural network processes inputs through layers using weighted sums and activation functions, then produces output scores from which a class can be selected; those scores do not by themselves establish probabilities or accuracy.

---

# Unit III — Consolidated Learning Review

## How the four chapters connect

| Chapter | Core idea | Shared example | Skill gained |
| :---- | :---- | :---- | :---- |
| 9 | Fixed rules versus learned patterns | Classifying Iris flowers | Explain the role of machine learning and connectionism |
| 10 | Samples, measurements, and correct labels | Four Iris measurements and three species | Separate input features from labels and hold out test data |
| 11 | Mathematical operation inside one neuron | Inputs `2, 3`; weights `0.5, −1`; bias `1` | Calculate a weighted sum and ReLU output |
| 12 | Connected neuron layers and a forward pass | Two-input, two-hidden-neuron toy network | Trace class scores and select the highest-scoring class |

Together, these chapters build a progression:

`Identify a pattern-recognition task → Organize labeled examples → Understand one neuron → Combine neurons to produce scores`

The **Iris examples** in Chapters 9 and 10 describe the dataset and model inputs. The **two-input calculations** in Chapters 11 and 12 are deliberately simplified mathematics examples. They show how neurons compute but are **not trained Iris predictions**.

## Unit III quick self-check

**Q1 — Rules versus learning:** Who selects the threshold in a hand-written flower rule? How is that different from how parameters in a supervised classifier are obtained?

**Q2 — Connectionism:** What are the main computational elements in an artificial neural network, and what connects them?

**Q3 — Features and labels:** For the record `[5.1, 3.5, 1.4, 0.2] → setosa`, identify the feature vector and the known label.

**Q4 — Train/test:** Why is it a mistake to use final test-set accuracy repeatedly to choose a model's settings?

**Q5 — ReLU:** What does ReLU return for `−2`, `0`, and `4`?

**Q6 — Neuron calculation:** With `x1=2`, `x2=3`, `w1=0.5`, `w2=−1`, and bias `3`, calculate the weighted sum and ReLU output.

**Q7 — Network layers:** What is the job of an input layer, a hidden layer, and an output layer?

**Q8 — Interpreting results:** If raw class scores are `[0.2, 0.7, 0.1]`, which class index wins? Why must we avoid treating the values as automatically calibrated probabilities?

### Answers and explanations

1. A programmer specifies a hand-written threshold. In supervised learning, an algorithm adjusts model parameters using labeled examples.  
2. Artificial neurons carry out numerical calculations, while weighted connections pass information among them.  
3. Feature vector: `[5.1, 3.5, 1.4, 0.2]`; label: `setosa`.  
4. It lets test information influence decisions, weakening the test's independence as an estimate of performance on unseen data.  
5. `0`, `0`, and `4`, respectively.  
6. `z = 0.5(2) + (−1)(3) + 3 = 1`; ReLU output `1`.  
7. The input layer holds features, hidden neurons transform the values, and the output layer produces the final task-dependent scores or values.  
8. Index `1` wins (versicolor in our label order). Raw scores alone do not show how probabilities were computed or whether the model's numerical confidence is calibrated.

## Short glossary

| Term | Beginner-friendly definition |
| :---- | :---- |
| Artificial intelligence | Broad field involving computational systems that perform tasks associated with intelligent behavior |
| Machine learning | Methods that learn useful patterns from data |
| Connectionist AI | Approaches emphasizing networks of connected processing units |
| Neural network | Model made of connected artificial neurons |
| Classification | Predicting one of several categories |
| Sample | One observed example in a dataset |
| Feature | Input value used to make a prediction |
| Label | Known target answer in supervised learning |
| Training set | Examples used to learn model parameters |
| Held-out test set | Examples reserved for evaluating the finished model |
| Weight | Value that scales a neuron's input contribution |
| Bias | Value added to a weighted sum before activation |
| ReLU | Function that returns the larger of `0` and its input |
| Hidden layer | Intermediate layer that transforms numerical values |
| Forward propagation | Computing an output by passing values through network layers |
| Raw class score | Number used to compare classes; not necessarily a probability |

## Suggested teaching demonstrations

**Demonstration A (Chapter 9):** Give classmates a hand-written petal-length rule, then ask what it can and cannot identify. Contrast the fixed threshold with the idea of a trained classifier.

**Demonstration B (Chapter 10):** Display one flower record. Ask learners to separate its four measurements from the correct species label. Then show the 120/30 example split and explain why a held-out set is useful.

**Demonstration C (Chapters 11–12):** Let one student calculate a neuron's weighted sum, another apply ReLU, and a third use the two hidden outputs to compute the final class scores.

These are optional ways to demonstrate existing material—not extra chapters or new deliverables. The team's videos may select representative concepts instead of narrating every subtopic.

## Bridge to Unit IV — Connectionist AI: Learning, Testing, and Applications

In Unit III, we assumed that a neural network already had weights and biases and traced **how it computes** a result. But our toy network's parameters were **selected by hand**, so its class scores do not show that it has learned useful flower patterns.

Unit IV asks the natural next question: **How can a network improve those parameters, and how do we judge whether its predictions are trustworthy?** Chapters 13–16 will introduce prediction error and loss, the intuition behind gradient descent and backpropagation, a supplied Iris classifier notebook, and evaluation using held-out examples.

**Next chapters:** 13–16 — Prediction Error and Loss Functions; How Neural Networks Learn; Training a Simple Neural Network Classifier; and Evaluating and Using Neural Networks Responsibly.

---

# Instructor / Team Production Notes

- **Source alignment:** This draft expands the provided PentaByte focused outline's Chapters 9–12, preserving exactly three numbered subtopics per chapter, the flower-classification example, and the specified worked calculations.  
- **Scope:** Chapters 9 and 10 introduce the task and data; Chapters 11 and 12 explain numerical prediction computations. No backpropagation derivations, matrix calculus, full network implementation, or extra AI architecture survey have been added.  
- **Not actual model performance:** The rules in Chapter 9 and the two-input network in Chapter 12 are teaching examples, not trained or experimentally validated classifiers. Do not cite their outputs as classifier accuracy or predictive evidence.  
- **Data preparation:** Always retain a consistent feature order, keep the known label out of input features, and prevent test-data leakage. A prepared, properly evaluated Iris classifier belongs in Chapters 15–16.  
- **Code environments:** Standard-library examples run in Python 3\. Chapter 10's optional dataset-loading and train/test split cells require `scikit-learn`; they are demonstrations, not full model training. If scikit-learn is not installed, learners can still follow the standalone record examples.  
- **Visuals:** All text-based network diagrams in this draft are original simplified instructional schematics. In slides, add an explicit caption such as “Illustrative untrained network; not to scale.”  
- **PPT/video reuse:** Chapter 9 offers a rule-versus-model discussion; Chapter 10 offers a labeled-data table; Chapter 11 offers the worked ReLU calculation; Chapter 12 offers the step-by-step two-neuron forward pass.  
- **Reference and credit:** Attribute the Iris dataset appropriately and include relevant software/documentation credits when submitting. Suggested authoritative references:  
  - scikit-learn, `load_iris`: [https\://scikit-learn.org/stable/modules/generated/sklearn.datasets.load\_iris.html](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)  
  - scikit-learn, `train_test_split`: [https\://scikit-learn.org/stable/modules/generated/sklearn.model\_selection.train\_test\_split.html](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)  
  - scikit-learn, Iris dataset description: [https\://github.com/scikit-learn/scikit-learn/blob/main/sklearn/datasets/descr/iris.rst](https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/datasets/descr/iris.rst)  
- **Before submission:** Have another teammate follow the example calculations and runnable cells; confirm the PPT, video narration, and any provided notebooks use the same four-feature order and class-name mapping. Add any course-required AI-use disclosure to the project records.

**End of Unit III — Connectionist AI: Data, Neurons, and Networks**