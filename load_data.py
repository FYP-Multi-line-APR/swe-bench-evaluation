from datasets import load_dataset

dataset_name = "princeton-nlp/SWE-bench"
dataset = load_dataset(dataset_name)
train_dataset = dataset['train']
print(train_dataset)
