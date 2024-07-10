import streamlit as st
import wikipedia as ai
import google.generativeai as genai
import time
GOOGLE_API_KEY = "AIzaSyCrUCzO2suUkeiwLR3NYXG85Erw1X4Zh00"
genai.configure(api_key=GOOGLE_API_KEY)
geminiModel = genai.GenerativeModel("gemini-pro")
chat = geminiModel.start_chat(history=[])
st.title("iShiksha")
add_selectbox = st.sidebar.selectbox(
    "choose the Interaction method",
    ("Google API","Wikipedia","iShiksha")
)
prompt = ""
if prompt == "":
    pass

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Do you want to ask me somthing?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if 'created' in prompt and 'you' in prompt:
    st.chat_message('ai').write('I am created by Ispark under the supervision of EPM Mr.Jerocin')
    exit()
if 'about' in prompt and 'you' in prompt:
    st.chat_message('ai').write('I am a test bot by Ispark')
    exit()
def home():
    global prompt
    prompt = st.chat_input("ask something", key="question")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        try:
            x = ai.summary(prompt)
            st.chat_message('ai').write(x)
        except:
            st.chat_message('ai').write("Sorry i can't able to say that right now")
        finally:
            prompt = ""
def google():
    global prompt,y
    prompt = st.chat_input("ask something", key="question")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    def get_gemini_response(query):
        instantResponse = chat.send_message(query, stream=False)
        return instantResponse
    if prompt:
        output = get_gemini_response(prompt)
        for outputChunk in output:
            y=outputChunk.text
        st.chat_message('ai').write(y)
    exit()
def book():
    st.write('Inbuilt')
    st.chat_message('ai').write("running")

if add_selectbox == "Google API":
    google()
    exit()
elif add_selectbox == "Wikipedia":
    home()
    exit()
elif add_selectbox == "book":
    book()
    exit()
else:
    pass