from transformers import AutoTokenizer, AutoModelForQuestionAnswering,pipeline

# Specify the model name you want to use
model_name = "Intel/dynamic_tinybert"

# Load the tokenizer associated with the specified model
tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True, truncation=True, max_length=512)

# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# Define a question-answering pipeline using the model and tokenizer
qa_pipe = pipeline(
    "question-answering", 
    tokenizer=tokenizer,
    model=model_name, 
    return_tensors='pt',
    device=-1
)
