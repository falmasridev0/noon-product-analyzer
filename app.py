import streamlit as st
import extract_reviews
import load_model
import inference
import torch
from wordcloud import WordCloud
import matplotlib.pyplot as plt

torch.classes.__path__ = []

def visualize_wordcloud(reviews):
    wordcloud = WordCloud().generate(" ".join(reviews))
    # Display the generated image:
    fig = plt.figure(figsize=(8,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot(fig)
    

st.write("""
# sentiment analyzer program
enter the url of any noon product to get a general sence about
reviews by see how many positive/negative reviews out there
         
         """)

url = st.text_input("product URL", placeholder="url")
reviews = []
if url:
    reviews = extract_reviews.extract_reviews(url)

    model,tokenizer = load_model.load("./model_checkpoint")

    result = inference.batch_inference(reviews,model,tokenizer).value_counts()

    st.bar_chart(result,x_label="sentiment",y_label="count",)
    visualize_wordcloud(reviews)


    st.write("# FINISHED")

