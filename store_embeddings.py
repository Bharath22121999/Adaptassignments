import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------
# SETUP
# ---------------------------------------------------------
# 1. Path to your CSV file
csv_file_path = 'my_dataset.csv'

# 2. The exact name of the column containing the sentences
#    (Open your CSV to check the header row)
column_name = 'utterance' 

# 3. Path to your local model
model_path = r'C:\Users\ZKDWJIQ\Desktop\my_local_model'

# ---------------------------------------------------------
# PROCESSING
# ---------------------------------------------------------

# 1. Load the Model
print(f"Loading model from {model_path}...")
model = SentenceTransformer(model_path)

# 2. Load the Dataset from CSV
print(f"Reading {csv_file_path}...")
try:
    df = pd.read_csv(csv_file_path)
    
    # Check if column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in CSV. Found: {df.columns.tolist()}")

    # Convert column to a clean list
    # dropna() removes empty rows which would crash the model
    dataset = df[column_name].dropna().tolist()
    
    print(f"Successfully loaded {len(dataset)} sentences.")

except Exception as e:
    print(f"Error reading CSV: {e}")
    exit()

# 3. Encode (Create Vectors)
print("Encoding dataset... this may take a minute...")
embeddings = model.encode(dataset, convert_to_tensor=True)

# 4. Store data in a dictionary
data_store = {
    'sentences': dataset,
    'embeddings': embeddings
}

# 5. Save to Pickle
output_file = 'corpus_embeddings.pkl'
with open(output_file, 'wb') as f:
    pickle.dump(data_store, f)

print(f"Done! Saved to {output_file}")
