import kagglehub

# Download latest version
path = kagglehub.model_download("metaresearch/llama-3/transformers/8b-hf")

print("Path to model files:", path)