import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get llama2 model

def getllamaresponse(input_text,no_words,blog_style):
    # calling llama model
    llm = CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    # prompt template
    template = """
      write a blog for {blog_style} job profile for a topic {input_text}
      within {no_words} words.
          """
    
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                   template=template)
    
    # generate response from llama model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response






#setting streamlit page config
st.set_page_config(page_title = "Generate Blogs",
                   page_icon = "🖊️",
                   layout="centered",
                   initial_sidebar_state="collapsed")



#heading of the page
st.header("Generate Blogs 🖊️")

input_text = st.text_input("Enter the blog topic")

#creating 2 colums for no of words and category of people
col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words")

with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers','DataScientists','Common People'),index=None)

submit = st.button("Generate blog")

#final response
if submit:
    st.write(getllamaresponse(input_text,no_words,blog_style))