import os
import streamlit as st
from groq import Groq

# Initialize Groq Client
client = Groq(api_key=st.secrets["api"]["key"])  # Ensure the API key is set in environment variables

def fetch_song_recommendations(song_name):
    """
    Query Groq API to analyze a song and fetch similar song recommendations.
    """
    # Construct query for recommendation based on song analysis
    query = (
        f"Analyze the song '{song_name}' to understand its mood and genre, "
        f"and provide around 10 similar song recommendations."
    )

    try:
        # Sending the query to Groq's chat model
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": query,
                }
            ],
            model="llama-3.2-90b-vision-preview"  # Updated model for enhanced recommendations
        )

        # Parsing the response to get recommendations
        response_content = chat_completion.choices[0].message.content
        recommendations = [line.strip() for line in response_content.splitlines() if line.strip()]

        return recommendations  # Return the recommendations

    except Exception as e:
        st.error(f"Failed to fetch recommendations: {e}")
        return []

# Streamlit UI
st.title("🎶 Song-Based Recommendation App")
st.write("Enter a song name, and our AI will recommend similar songs.")

# Input song name from the user
song_name = st.text_input("Enter a song name")

# Trigger API call and display recommendations
if st.button("Get Recommendations"):
    with st.spinner("Analyzing song and fetching recommendations..."):
        recommendations = fetch_song_recommendations(song_name)

    if recommendations:
        st.success("Here are some similar songs you might enjoy:")
        for song in recommendations:
            st.write(f"- {song}")
    else:
        st.warning("No similar song recommendations found. Try another song.")
