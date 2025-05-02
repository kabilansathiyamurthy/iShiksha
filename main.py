import streamlit as st
import wikipedia as ai
import google.generativeai as genai

# Replace with your actual Google API key
GOOGLE_API_KEY = "AIzaSyDIFVkmrFRjyh8M9-JyCPI6i0FAXmn5O-U"  # IMPORTANT: Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
geminiModel = genai.GenerativeModel("gemini-pro")
chat = geminiModel.start_chat(history=[])
st.title("iShiksha")
add_selectbox = st.sidebar.selectbox(
    "choose the Interaction method",
    ("Google API", "Wikipedia", "iShiksha")
)
prompt = ""
if prompt == "":
    pass

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! Do you want to ask me something?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if 'created' in prompt and 'you' in prompt:
    st.chat_message('ai').write('I am created by Ispark under the supervision of EPM Mr.Jerocin')

if 'about' in prompt and 'you' in prompt:
    st.chat_message('ai').write('I am a test bot by Ispark')


def home():
    """Handles user input and fetches information from Wikipedia."""
    global prompt
    prompt = st.chat_input("ask something", key="question")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        try:
            x = ai.summary(prompt)
            st.chat_message('ai').write(x)
        except Exception as e:  # Catch specific exceptions, not all.
            st.chat_message('ai').write(f"Sorry, I can't find that right now.  Error: {e}")
        finally:
            prompt = ""


def google():
    """Handles user input and fetches information from Google's Gemini API."""
    global prompt, y
    prompt = st.chat_input("ask something", key="question")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        def get_gemini_response(query):
            """Gets a response from the Gemini model."""
            try:
                instantResponse = chat.send_message(query, stream=False)
                return instantResponse
            except Exception as e:
                st.error(f"Error while getting response from Google API: {e}")
                return None

        output = get_gemini_response(prompt)
        if output: # check if output is not None
            for outputChunk in output:
                y = outputChunk.text
            st.chat_message('ai').write(y)
    #Removed the exit() here.  The program should continue to run.

def book():
    """Placeholder function for a "book" feature."""
    st.write('Inbuilt')
    st.chat_message('ai').write("running")
    #Removed the exit() here.  The program should continue to run.

# Main execution block
if add_selectbox == "Google API":
    google()

elif add_selectbox == "Wikipedia":
    home()

elif add_selectbox == "iShiksha":  # Changed "book" to "iShiksha" to match the selectbox option
    book()

if prompt: # added this condition, otherwise it will show error
    st.session_state.messages.append({"role": "assistant", "content": prompt})
