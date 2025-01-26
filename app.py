import streamlit as st
from post_generator import *

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Main app layout
def main():
    st.title("🕵️ LinkedIn Content Generator")
    st.markdown(
        """<style>
        .css-1oe6wy4, .css-1y4p8pa {
            background-color: #f8f9fa;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .css-1v0mbdj {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("**The code replicates the writing style of the selected author and generates posts accordingly. You can customize the raw data to match any author of your choice.**")
    st.markdown("**Using llama-3.3-70b-versatile model with groc API and Prompt Engineering**")

    st.markdown("---")

    # Organize UI into sections
    st.header("Choose Post Parameters")

    fs = FewShotPosts()
    tags = fs.get_tags()

    # Create three columns for inputs
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        selected_tag = st.selectbox("Select a Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Select Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Select Language", options=language_options)

    st.markdown("---")

    st.header("Generate Post")

    # Generate Button and Display
    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)

        # Display the generated post
        st.write(post)
    else:
        st.write("Click the button above to generate a LinkedIn post.")

    st.markdown("---")


# Run the app
if __name__ == "__main__":
    main()
