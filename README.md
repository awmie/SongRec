
# 🎶 Song-Based Recommendation App

A web application that provides song recommendations based on user input, using the Groq API for mood and genre analysis. Enter a song name, and the app will suggest similar songs, detailing each song's mood and genre.

## 🚀 Features
- Enter a song name to get recommendations.
- Shows mood and genre analysis of the input song.
- Provides a list of similar songs with detailed descriptions.
- Built using Streamlit for an interactive UI.

## 🛠 Future Enhancements
- Integrate Chain of Thought (CoT) prompting for better recommendation accuracy.

## 🧠 Model
- Works on the **Llama 3.2-90b text preview model** for generating recommendations.

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/song-rec-app.git
   ```
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Groq API key in the environment variables.

## 🧩 Usage
1. Run the app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser and enter a song name to get recommendations.

## 📚 How It Works
- The app takes a song name as input and uses Groq’s API to analyze the song.
- It identifies mood and genre and fetches 10 similar song recommendations based on these attributes.

## 🛠️ Tech Stack
- **Python**
- **Streamlit** - For the user interface
- **Groq API** - For song analysis and recommendation generation

## 🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.
