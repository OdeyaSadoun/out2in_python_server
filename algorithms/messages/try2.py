import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from scipy.sparse import csr_matrix

# Read the dataset
df = pd.read_csv("./train/dataset.csv", encoding='latin1')

# Assuming 'message' contains the text data and 'type' contains labels
texts = df['message'].tolist()
labels = df['type']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_sparse = vectorizer.fit_transform(texts)

# Convert SparseTensor to a dense NumPy array
X_dense = csr_matrix.todense(X_sparse)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_dense, labels, test_size=0.25)

# Create the model
model = Sequential([
    Dense(100, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(100, activation='relu'),
    Dropout(0.2),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))


from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Get predictions
y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype("int32")  # Threshold for binary classification

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred_classes)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()


# Assuming 'new_message' is the new message in Hebrew you want to classify
new_message = ["זו הודעה חדשה שאני רוצה לסווג"]

# Preprocess the new message using the same vectorizer used for training
new_message_sparse = vectorizer.transform(new_message)
new_message_dense = new_message_sparse.todense()

# Predict using the trained model
prediction = model.predict(new_message_dense)

# Determine the class label based on the prediction threshold
prediction_label = "Related to Social Boycott" if prediction > 0.5 else "Not Related to Social Boycott"
print(f"The prediction for the new message is: {prediction_label}")
