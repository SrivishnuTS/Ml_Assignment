dataset = [
    ["High",   "Stable", "Good",  "Yes", "Approve"],
    ["High",   "Stable", "Good",  "No",  "Approve"],
    ["Low",    "Unstable","Poor", "No",  "Reject"],
    ["Medium", "Stable", "Good",  "Yes", "Approve"],
    ["Low",    "Stable", "Poor",  "No",  "Reject"]
]

attributes = ["Income", "Job Stability", "Credit Score", "Has Collateral"]

positive_examples = [row[:-1] for row in dataset if row[-1] == "Approve"]

hypothesis = positive_examples[0].copy()

for example in positive_examples[1:]:
    for i in range(len(hypothesis)):
        if hypothesis[i] != example[i]:
            hypothesis[i] = "?"

print("\n===== Learned Hypothesis =====")
for attr, val in zip(attributes, hypothesis):
    print(f"{attr}: {val}")

def classify(application):
    for i in range(len(hypothesis)):
        if hypothesis[i] != "?" and hypothesis[i] != application[i]:
            return "Reject"
    return "Approve"

correct = 0

print("\n===== Predictions on Dataset =====")

for row in dataset:
    features = row[:-1]
    actual = row[-1]
    prediction = classify(features)

    print(f"Application {features} -> Predicted: {prediction} | Actual: {actual}")

    if prediction == actual:
        correct += 1

accuracy = correct / len(dataset) * 100
print(f"\nModel Accuracy: {accuracy:.2f}%")

print("\n===== Test New Loan Application =====")

test_application = []

for attr in attributes:
    value = input(f"Enter {attr}: ")
    test_application.append(value)

result = classify(test_application)

print("\nPrediction for new application:", result)
