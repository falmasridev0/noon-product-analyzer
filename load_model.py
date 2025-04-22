from transformers import BertTokenizer,BertForSequenceClassification
def load(path):
    model = BertForSequenceClassification.from_pretrained(path)
    tokenizer = BertTokenizer.from_pretrained(path)
    model.eval()

    return model,tokenizer

