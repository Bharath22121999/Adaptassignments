import pickle
import pandas as pd
import os
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------
# SETUP
# ---------------------------------------------------------

# 1. Path to your CSV file
# Since it is in the same folder, we just use the filename
csv_file_path = 'my_dataset.csv'

# 2. The exact name of the column containing the sentences
column_name = 'utterance' 

# 3. Path to your local model
# We assume the folder 'my_local_model' is sitting next to this script.
# If you took the files OUT of the folder and they are loose 
# in the current directory, change this to: model_path = '.'
model_path = 'my_local_model'

# ---------------------------------------------------------
# PROCESSING
# ---------------------------------------------------------

# Check if model folder exists before starting
if not os.path.exists(model_path):
    print(f"ERROR: Could not find the model folder at: {os.path.abspath(model_path)}")
    print("Make sure the folder 'my_local_model' is in the same directory as this script.")
    exit()

# 1. Load the Model
print(f"Loading model from folder: {model_path}...")
model = SentenceTransformer(model_path)

# 2. Load the Dataset from CSV
print(f"Reading {csv_file_path}...")
try:
    df = pd.read_csv(csv_file_path)
    
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found. Found: {df.columns.tolist()}")

    dataset = df[column_name].dropna().tolist()
    print(f"Successfully loaded {len(dataset)} sentences.")

except FileNotFoundError:
    print(f"ERROR: Could not find the file '{csv_file_path}' in this folder.")
    exit()
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit()

# 3. Encode (Create Vectors)
print("Encoding dataset... this may take a minute...")
embeddings = model.encode(dataset, convert_to_tensor=True)

# 4. Store data
data_store = {
    'sentences': dataset,
    'embeddings': embeddings
}

# 5. Save to Pickle
output_file = 'corpus_embeddings.pkl'
with open(output_file, 'wb') as f:
    pickle.dump(data_store, f)

print(f"Done! Saved to {output_file}")
