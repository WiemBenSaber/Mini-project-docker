# Step 1: Import the necessary libraries
import base64
import joblib
import librosa as librosa
import numpy as np
import pandas as pd
from flask import jsonify
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Step 2: Load the CSV file containing features and labels
data = pd.read_csv('/Users/wiem/Desktop/Data/features_30_sec.csv')

# Step 3: Data Preprocessing
X = data.drop(columns=['label','filename'])  # Features
y = data['label']  # Labels

# Step 4: Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Concatenate training and testing data for PCA
X_combined = np.vstack((X_train, X_test))

# Initialize the scaler
scaler = StandardScaler()

# Fit and transform the scaler on the combined data
X_combined_scaled = scaler.fit_transform(X_combined)

# Apply PCA to the combined data
pca = PCA(n_components=57)  # Set n_components to a lower value, e.g., 10
X_combined_reduced = pca.fit_transform(X_combined_scaled)

# Print debug information
print(f"Original data shape: {X_combined.shape}")
print(f"Scaled data shape: {X_combined_scaled.shape}")
print(f"Reduced data shape: {X_combined_reduced.shape}")
print(f"Explained variance ratios: {pca.explained_variance_ratio_}")

# Split the data back into training and testing sets
X_train_reduced = X_combined_reduced[:len(X_train)]
X_test_reduced = X_combined_reduced[len(X_train):]

# Initialize the SVM model
svm_model = SVC(kernel='linear', C=1.0)

# Train the SVM model on the reduced training data
svm_model.fit(X_train_reduced, y_train)

# Predict on the reduced test data
y_pred = svm_model.predict(X_test_reduced)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
joblib.dump(svm_model, '../../../Desktop/scripts/modeltest.pkl')
joblib.dump(scaler, '../../../Desktop/scripts/scalertest.pkl')
print(f'Accuracy: {accuracy}')

