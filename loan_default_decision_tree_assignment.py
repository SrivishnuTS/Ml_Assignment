import math

data = [
    ("S1", 1.5, 60, "Fail"),
    ("S2", 2.0, 65, "Fail"),
    ("S3", 2.5, 70, "Pass"),
    ("S4", 3.0, 75, "Pass"),
    ("S5", 3.5, 80, "Pass"),
    ("S6", 4.0, 85, "Pass")
]

print("\n===== Handling Continuous Attributes =====")
print("Decision trees handle continuous attributes by testing threshold splits like Study Hours ≤ value.\n")

def entropy(labels):
    total = len(labels)
    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent

labels = [row[3] for row in data]
dataset_entropy = entropy(labels)

print("Dataset Entropy:", round(dataset_entropy, 4))

hours = sorted([row[1] for row in data])
thresholds = [(hours[i] + hours[i+1]) / 2 for i in range(len(hours)-1)]

print("\nPossible Thresholds:", thresholds)

def info_gain(threshold):
    left = [row for row in data if row[1] <= threshold]
    right = [row for row in data if row[1] > threshold]

    left_labels = [row[3] for row in left]
    right_labels = [row[3] for row in right]

    weighted_entropy = (
        len(left)/len(data) * entropy(left_labels) +
        len(right)/len(data) * entropy(right_labels)
    )

    return dataset_entropy - weighted_entropy

best_threshold = None
best_gain = -1

print("\n===== Information Gain for Each Threshold =====")

for t in thresholds:
    gain = info_gain(t)
    print(f"Threshold {t:.2f} -> Gain {gain:.4f}")

    if gain > best_gain:
        best_gain = gain
        best_threshold = t

print("\nBest Threshold:", best_threshold)
print("Best Information Gain:", round(best_gain, 4))

print("\n===== Decision Tree =====")
print(f"If Study Hours ≤ {best_threshold}: Result = Fail")
print(f"If Study Hours > {best_threshold}: Result = Pass")
