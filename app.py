import streamlit as st 
import google.generativeai as genai
import os
import PIL.Image
from dotenv import load_dotenv,find_dotenv


status=load_dotenv(find_dotenv(),override=True)
print(status)
mykey=os.getenv('GOOGLE_GEMINI_API_KEY')
# print('the key is',mykey)
genai.configure(api_key=mykey)
model=genai.GenerativeModel("gemini-3.6-flash")


def analyze_human_image(image):
    prompt = """
    You are an AI trained to analyze human attributes from images with high accuracy. 
    Carefully analyze the given image and return the following structured details:

    You have to return all results as you have the image, don't want any apologize or empty results.

    - *Gender* (Male/Female/Non-binary)
    - *Age Estimate* (e.g., 25 years)
    - *Ethnicity* (e.g., Asian, Caucasian, African, etc.)
    - *Mood* (e.g., Happy, Sad, Neutral, Excited)
    - *Facial Expression* (e.g., Smiling, Frowning, Neutral, etc.)
    - *Glasses* (Yes/No)
    - *Beard* (Yes/No)
    - *Hair Color* (e.g., Black, Blonde, Brown)
    - *Eye Color* (e.g., Blue, Green, Brown)
    - *Headwear* (Yes/No, specify type if applicable)
    - *Emotions Detected* (e.g., Joyful, Focused, Angry, etc.)
    - *Confidence Level* (Accuracy of prediction in percentage)
    """
    response = model.generate_content([prompt, image])
    return response.text.strip()



# now the frontend application 
st.title("human attribute detection project")
st.write('upload an image to detect human attributes with gen ai')


upload_image=st.file_uploader("upload an image",type=['png','jpg','jpeg'])

if upload_image:
    i=PIL.Image.open(upload_image)
    person_info=analyze_human_image(i)

    col1,col2=st.columns(2)
    with col1:
        st.image(i,caption="uploaded image",use_container_width=True)
    with col2:
        st.write(person_info)




    