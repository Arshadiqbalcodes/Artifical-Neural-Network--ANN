# 🧠 Artificial Neural Network (ANN)

## 1. What is ANN?

**ANN = Artificial Neural Network**

An Artificial Neural Network is a **Machine Learning / Deep Learning model** inspired by the working of the human brain.

ANN learns patterns from data and uses those patterns to make predictions or classifications.

### Basic Flow

```text
Input → Neurons → Output
```

### Example

If we want to predict whether a student will **Pass or Fail**:

```text
Study Hours ─────┐
                 │
Attendance ──────┼──> ANN ───> Pass / Fail
                 │
Assignments ────┘
```

---

## 2. Basic Neuron

A neuron receives inputs and processes them using **weights, bias, and an activation function**.

```text
x₁ ── weight w₁ ──┐
x₂ ── weight w₂ ──┼──> Neuron ──> Output
x₃ ── weight w₃ ──┘
          +
         Bias
```

The basic formula is:

```text
Output = Activation(x₁w₁ + x₂w₂ + x₃w₃ + Bias)
```

---

## 3. Small Numerical Example

Suppose:

```text
x₁ = 2
x₂ = 3

w₁ = 0.5
w₂ = 0.2

Bias = 1
```

First, calculate the weighted sum:

```text
(2 × 0.5) + (3 × 0.2) + 1
```

```text
= 1 + 0.6 + 1
```

```text
= 2.6
```

So, the neuron receives:

```text
Weighted Sum = 2.6
```

Then an **activation function** is applied to produce the final output.

---

## 4. Four Important Concepts

### 1. Input

The data/features provided to the neural network.

### 2. Weight

A weight represents the **importance of an input**.

### 3. Bias

Bias provides an additional adjustment to the neuron's calculation.

### 4. Activation Function

The activation function determines the neuron's final output and helps the neural network learn complex patterns.

---

## 5. Important ANN Concepts

The main concepts we need to understand are:

* Input Layer
* Hidden Layers
* Output Layer
* Neurons
* Weights
* Bias
* Activation Functions
* Forward Propagation
* Loss Function
* Backpropagation
* Gradient Descent
* Model Training
* Prediction

---

## 6. ANN Architecture

A basic ANN can be represented as:

```text
Input Layer       Hidden Layer        Output Layer

   x₁  ──────────>  ○
                    │
   x₂  ──────────>  ○ ──────────>  ○
                    │
   x₃  ──────────>  ○
```

The **Input Layer** receives data.

The **Hidden Layer(s)** learn patterns from the data.

The **Output Layer** produces the final prediction.

---

## 7. ANN Learning Process

The general ANN learning process is:

```text
Input Data
    ↓
Forward Propagation
    ↓
Prediction
    ↓
Calculate Loss
    ↓
Backpropagation
    ↓
Update Weights
    ↓
Repeat
    ↓
Better Prediction
```

---

## 8. Key Formula

A neuron basically calculates:

```text
z = x₁w₁ + x₂w₂ + ... + xₙwₙ + b
```

Then:

```text
Output = Activation(z)
```

Where:

* `x` = Input
* `w` = Weight
* `b` = Bias
* `z` = Weighted Sum
* `Activation()` = Activation Function

---

## 9. Summary

**ANN is a neural-network-based model that learns patterns from data.**

The basic idea is:

```text
Inputs
   ↓
Weights + Bias
   ↓
Activation Function
   ↓
Output
```

The most important components to understand are:

**Input → Weight → Bias → Activation → Output**

These concepts form the foundation of Artificial Neural Networks.
