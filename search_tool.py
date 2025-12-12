import pickle
import os
from sentence_transformers import SentenceTransformer, util

# ---------------------------------------------------------
# SETUP PATHS
# ---------------------------------------------------------
# Get the folder where this script is running
script_dir = os.path.dirname(os.path.abspath(__file__))

# Path to your local model
model_path = os.path.join(script_dir, 'my_local_model')

# Path to your saved embeddings
pickle_file = os.path.join(script_dir, 'corpus_embeddings.pkl')

# ---------------------------------------------------------
# LOAD RESOURCES
# ---------------------------------------------------------

# 1. Load the Model
print(f"Loading model from: {model_path}...")
try:
    model = SentenceTransformer(model_path)
except Exception as e:
    print("Error loading model. Make sure 'my_local_model' folder is correct.")
    exit()

# 2. Load the Embeddings (The .pkl file)
print(f"Loading database from: {pickle_file}...")
try:
    with open(pickle_file, 'rb') as f:
        data_store = pickle.load(f)
        
    stored_sentences = data_store['sentences']
    stored_embeddings = data_store['embeddings']
    print(f"Loaded {len(stored_sentences)} sentences into memory.")

except FileNotFoundError:
    print("Error: Could not find 'corpus_embeddings.pkl'. Did you run the previous script?")
    exit()

# ---------------------------------------------------------
# SEARCH LOOP
# ---------------------------------------------------------
print("\n" + "="*50)
print(" SEMANTIC SEARCH TOOL IS READY")
print(" Type 'exit' or 'quit' to stop.")
print("="*50 + "\n")

while True:
    # 1. Get User Input
    query = input("Enter your sentence: ")
    
    if query.lower() in ['exit', 'quit']:
        print("Exiting...")
        break
        
    if not query.strip():
        continue

    # 2. Encode the Query (Convert input to numbers)
    query_embedding = model.encode(query, convert_to_tensor=True)

    # 3. Perform Search
    # top_k=5 means "Return the top 5 matches"
    search_results = util.semantic_search(query_embedding, stored_embeddings, top_k=5)
    
    # 4. Print Results
    print(f"\nTop matches for: '{query}'")
    print("-" * 50)
    
    # The results are a list of lists (we only have 1 query, so take index 0)
    hits = search_results[0]
    
    found_any = False
    for hit in hits:
        score = hit['score']
        
        # Threshold: Only show if similarity is > 50%
        if score > 0.5:
            found_any = True
            sentence = stored_sentences[hit['corpus_id']]
            print(f"Score: {score:.4f} | {sentence}")
            
    if not found_any:
        print("No similar sentences found (Score < 0.5)")
        
    print("-" * 50 + "\n")
