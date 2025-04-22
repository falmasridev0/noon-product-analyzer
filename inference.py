from pandas import Series
def batch_inference(user_inputs,model,tokenizer):
    pre_processing = tokenizer(user_inputs,return_tensors="pt",padding=True, truncation=True)
    output = model(**pre_processing).logits.argmax(dim=1)
    return Series(output)