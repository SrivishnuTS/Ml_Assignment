Machine Learning Assignment 1
Overview

This repository contains solutions for three machine learning problems focusing on core concepts such as Concept Learning, Decision Trees with Continuous Attributes, and the ID3 Algorithm. The assignment demonstrates conceptual clarity, algorithm development, and practical experimentation using Python.

Assignment Objectives

Understand basic supervised learning methods.

Use entropy and information gain to build decision trees.

Implement the ID3 algorithm without using external ML libraries.

Work with datasets and generate predictions.

Maintain proper documentation using GitHub and Wiki.

Question 1 — Concept Learning (Student Performance Classification)
Problem Statement

Design a simple machine learning system to classify students as Pass or Fail using labeled training examples and identify patterns in academic features.

Approach

Used the Find-S algorithm to learn the most specific hypothesis from positive examples.

Considered features such as attendance, assignment completion, study hours, and internal assessment marks.

Built a classifier that predicts whether a student will pass or fail.

Key Concepts

Hypothesis representation

Positive and negative training examples

Generalization of rules

Rule-based classification

Outcome

The system successfully learns rules that distinguish passing students from failing students based on common academic characteristics.

Question 2 — Decision Tree with Continuous Attributes (Placement Prediction)
Problem Statement

Predict whether a student will get placed based on continuous attributes such as CGPA and aptitude test score.

Approach

Calculated the entropy of the dataset.

Generated possible threshold splits for CGPA.

Computed information gain for each threshold.

Selected the best split and formed a decision rule.

Key Concepts

Entropy computation

Threshold-based splitting

Information gain

Decision rule generation

Outcome

The optimal split effectively separates placed and not-placed students, resulting in a clear and interpretable decision rule.

Question 3 — ID3 Algorithm (Medical Diagnosis Dataset)
Problem Statement

Build a decision tree using the ID3 algorithm to predict whether a patient has a disease based on symptoms and test results.

Approach

Implemented the ID3 algorithm from scratch.

Calculated entropy and information gain for all attributes.

Recursively constructed the decision tree.

Predicted the class label for a new patient record.

Key Concepts

Recursive decision tree construction

Attribute selection using information gain

Entropy reduction

Classification and prediction

Outcome

The model correctly predicts the disease status for the given patient example using the learned decision tree.

Repository Structure
ML-Assignment-1/
│
├── student_performance_concept_learning.py
├── placement_prediction_decision_tree.py
├── medical_diagnosis_id3.py
├── README.md
└── Wiki (Documentation)

Tools and Technologies

Python

Basic data structures

Mathematical computation (entropy, logarithmic functions)

GitHub for version control

GitHub Wiki for documentation

Learning Outcomes

Through this assignment, the following skills were developed:

Understanding of supervised machine learning fundamentals

Ability to implement learning algorithms manually

Interpretation of decision trees and rule-based models

Analytical thinking for evaluating models

Proper documentation and reproducibility practices

Conclusion

This assignment provides practical exposure to fundamental machine learning techniques. By implementing concept learning and decision tree algorithms and analyzing their behavior, we gain a deeper understanding of how models extract patterns from data and make predictions in real-world applications.
