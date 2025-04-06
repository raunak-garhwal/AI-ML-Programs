# Import required libraries
import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Start time measurement
start_time = time.time()

# Step 1: Load dataset from CSV file
# Make sure to replace 'data.csv' with your actual file path
data = pd.read_csv('ML-Programs/Raunak-ML/Feature_based_classification.csv')

# Separate features and target
X = data.iloc[:, :-1].values  # All columns except last
y = data.iloc[:, -1].values   # Last column as target

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Apply k-NN Algorithm
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Step 4: Make Predictions
y_pred = knn.predict(X_test)

# Step 5: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Print confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 6: Simple Visualization (Plotting first two features only)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", edgecolors='k')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Feature Visualization (First 2 Features)")
plt.colorbar(label="Class")
plt.show()

# End time measurement
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.4f} seconds")
