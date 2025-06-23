import streamlit as st
import requests
import json
import os

# ---------- Config ----------
st.set_page_config(page_title="AI Recipe Chatbot", layout="wide")
st.title("🍳 :red[AI Recipe Assistant]")

HISTORY_FILE = "chat_history.json"
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

# ---------- Utility Functions ----------
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def extract_title(response):
    lines = response.splitlines()
    for line in lines:
        if line.strip().lower().startswith("title") or "recipe title" in line.lower():
            return line.strip().replace("**", "").replace("Recipe Title:", "").strip()
    return "Untitled Recipe"

# ---------- Session State ----------
if "selected_chat" not in st.session_state:
    st.session_state.selected_chat = None
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

# ---------- Load Chat History ----------
history = load_history()

# ---------- Sidebar ----------
st.sidebar.title("🍽️ AI Recipe Chatbot")

# Styled Create Button
if st.sidebar.button("➕ Create New Recipe", type="primary"):
    st.session_state.selected_chat = None
    st.session_state.form_submitted = False

# Display History
st.sidebar.markdown("## 🕘 Recipe History")
for i, chat in enumerate(reversed(history)):
    title = chat.get("title", f"Recipe {i+1}")
    if st.sidebar.button(title):
        st.session_state.selected_chat = len(history) - 1 - i

# ---------- Main Area ----------
if st.session_state.selected_chat is not None:
    selected = history[st.session_state.selected_chat]
    st.subheader(selected.get("title", "Saved Recipe"))
    st.markdown("### 🧾 Prompt")
    st.code(selected["prompt"])
    st.markdown("### 🍲 Response")
    st.write(selected["response"])

else:
    st.subheader("🥕 Create a New Recipe")
    with st.form("recipe_form"):
        ingredient = st.text_input("Main Ingredient (e.g., Tomato, Egg, Mango)")
        cuisine = st.selectbox("Cuisine Style", ["Indian", "Italian", "Chinese", "Mexican", "American"])
        generate_button = st.form_submit_button(
            "Generate Recipe", disabled=st.session_state.form_submitted
        )

    if generate_button and ingredient:
        st.session_state.form_submitted = True
        prompt = f"""You are a creative recipe assistant. Make a recipe using: {ingredient}.
Use {cuisine} cuisine style.
Respond with:
- A creative recipe title
- Ingredients list
- Step-by-step instructions
- Estimated time"""

        st.markdown("### 🍳 Generating Recipe...")
        response_container = st.empty()
        full_response = ""

        try:
            res = requests.post(
                OLLAMA_URL,
                json={"model": MODEL_NAME, "prompt": prompt, "stream": True},
                stream=True,
            )
            for line in res.iter_lines():
                if line:
                    json_data = json.loads(line.decode("utf-8"))
                    delta = json_data.get("response", "")
                    full_response += delta
                    response_container.markdown(full_response)
        except Exception as e:
            st.error(f"Error: {e}")

        # Save result
        title = extract_title(full_response)
        new_entry = {"prompt": prompt, "response": full_response, "title": title}
        history.append(new_entry)
        save_history(history)

        # Select the newly added recipe
        st.session_state.selected_chat = len(history) - 1
        st.session_state.form_submitted = False  # Optionally reset form submitted flag

        st.rerun()
