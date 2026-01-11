import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv").drop(columns=['Unnamed: 0'])

def add_custom_styles():
    background_image_url = "https://img.freepik.com/free-vector/glowing-musical-pentagram-background-with-sound-notes_1017-31220.jpg?t=st=1737521643~exp=1737525243~hmac=b40f39e7dbcdcea6d5bd8aab4c58ab8fb68f59eaa0da67b4f2fb651d26fdf29f&w=1380"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: top;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white; 
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #08e38f; 
        }}
        .stButton > button {{
            background-color: #08e38f; 
            color: #4b3f73;
        }}
        a {{
            color: #08e38f; 
        }}
        p {{
            color: white; 
            font-size: 1.2rem;
        }}
        .custom-text {{
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
        }}
        .custom-label {{
            color: white;
            font-size: 1.3rem;
            font-weight: bold;
        }}
        .interpretation {{
            color: white;
            font-size: 1.53rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def homepage():
    st.markdown(
        """
        <header style="color:#735bc1; font-weight:bold; font-size:2.54rem;">
                    🎵 Music Analysis Application
        </header>
        <br>
        <span style="color:#08e38f; font-weight:bold; font-size:2rem;">
        Welcome to the Music Analysis App!
        </span>
        <h3 style="color:#00eafb; font-size:1.1rem;">This application helps a music production company explore music styles and characteristics 
        to identify trends and maximize sales.</h3>  
        <br>
        <h3 style="color:#08e38f; font-size:2rem;">Key Features:</h3>
        <ul style="color:#00eafb; font-size:1.3rem;">
            <li>Discover the popularity of different music genres.</li>
            <li>Analyze characteristics like energy, danceability, and tempo by genre.</li>
            <li>Gain insights to make data-driven decisions in the music industry.</li>
        </ul>
        <hr>
        """,
        unsafe_allow_html=True
    )
    if st.button("📊 Go to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

def dashboard(data):
    st.markdown(
        """
        <header style="color:#00eafb; font-weight:bold; font-size:3.57rem;">
                    📊 Musical Dashboard
        </header>

        """,unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Explore key metrics and insights about music styles.</p>', unsafe_allow_html=True)

    # Genre Popularity Viz #
    st.subheader("1️⃣ Favourite Music Genres")
    st.markdown('<p class="custom-label">Select a metric to rank genres:</p>', unsafe_allow_html=True)
    metric = st.selectbox(
        "Select a metric to rank genres:",
        ["popularity", "danceability", "energy", "tempo"],
        index=0,
        label_visibility="collapsed")
    genre_popularity = data.groupby("track_genre")[metric].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        x=genre_popularity.values,
        y=genre_popularity.index,
        hue=genre_popularity.index,
        dodge=False,
        palette="viridis",
        ax=ax,
        legend=False
    )
    ax.set_title(f"Top 10 Popular Music Genres by {metric.capitalize()}", fontsize=16)
    ax.set_xlabel(f"Average {metric.capitalize()}", fontsize=12)
    ax.set_ylabel("Genre", fontsize=12)
    st.pyplot(fig)
    
    st.markdown(
        f"""
        <p class="interpretation">
        <strong>Interpretation:</strong><br>
        This chart shows the **top 10 music genres** ranked by **{metric}**.  
        Use this to identify which genres have the highest {metric.lower()} values.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Danceability vs. Energy vs. Temp vs. Valence by Genre #
    st.subheader("2️⃣ Compare Any Two Features by Genre")
    st.markdown('<p class="custom-label">Select Horizontale-Axis Feature:</p>', unsafe_allow_html=True)
    x_axis = st.selectbox("Select Horizontale-Axis Feature:", ["danceability", "energy", "tempo", "valence"], index=0, label_visibility="collapsed")
    st.markdown('<p class="custom-label">Select Vertical-Axis Feature:</p>', unsafe_allow_html=True)
    y_axis = st.selectbox("Select Vertical-Axis Feature:", ["danceability", "energy", "tempo", "valence"], index=1, label_visibility="collapsed")
    
    st.markdown('<p class="custom-label">Select Genres : </p>', unsafe_allow_html=True)
    selected_genres = st.multiselect(
        "Select Genres :", 
        data['track_genre'].unique(),
        default=data['track_genre'].unique()[:5],
        label_visibility="collapsed"
    )
    
    if selected_genres:
        filtered_data = data[data['track_genre'].isin(selected_genres)]
        fig, ax = plt.subplots(figsize=(8, 5))
        for genre in selected_genres:
            genre_data = filtered_data[filtered_data['track_genre'] == genre]
            ax.scatter(
                genre_data[x_axis],
                genre_data[y_axis],
                label=genre,
                alpha=0.7
            )
        ax.set_title(f"{x_axis.capitalize()} vs. {y_axis.capitalize()} by Genre", fontsize=16)
        ax.set_xlabel(x_axis.capitalize(), fontsize=12)
        ax.set_ylabel(y_axis.capitalize(), fontsize=12)
        ax.legend(title="Genres", loc="upper right")
        st.pyplot(fig)
    
        st.markdown(
            f"""
            <p class="interpretation">
            <strong>Interpretation:</strong><br>
            This scatter plot allows you to **compare {x_axis} and {y_axis}** for different genres.  
            Higher values indicate genres that excel in these attributes.
            </p>
            """,
            unsafe_allow_html=True
        )

    # Distributions by Genre #
    st.subheader("3️⃣ Distribution of Any Feature by Genre")
    st.markdown('<p class="custom-label">Select a feature to analyze:</p>', unsafe_allow_html=True)
    feature = st.selectbox(
        "Select a feature to analyze:",
        ["tempo", "loudness", "speechiness", "instrumentalness"],
        index=0,
        label_visibility="collapsed")
    st.markdown('<p class="custom-label">Select a Genre :</p>', unsafe_allow_html=True)
    genre_for_feature = st.selectbox(
        "Select a Genre", 
        data['track_genre'].unique(),
        label_visibility="collapsed"
    )
    feature_data = data[data['track_genre'] == genre_for_feature][feature]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(feature_data, bins=30, kde=True, color="skyblue", ax=ax)
    ax.set_title(f"{feature.capitalize()} Distribution for {genre_for_feature}", fontsize=16)
    ax.set_xlabel(feature.capitalize(), fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    st.pyplot(fig)
    st.markdown(
        f"""
        <p class="interpretation">
        <strong>Interpretation:</strong><br>
        This chart shows the **distribution of {feature}** for {genre_for_feature}.  
        The spread of values tells you whether a genre typically has high or low {feature}.
        </p>
        """,
        unsafe_allow_html=True
    )
    #AutoscrollButton#
    st.markdown(
        """
        <style>
        .autoscroll-btn {
            position: fixed;
            bottom: 10px;
            right: 10px;
            background-color: #08e38f;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        </style>
        <button class="autoscroll-btn" onclick="window.scrollTo(0, document.body.scrollHeight);">
            ⬇️ Scroll Down
        </button>
        """,
        unsafe_allow_html=True
    )
##the application logic
if 'page' not in st.session_state:
    st.session_state.page = "Home"
data = load_data()
add_custom_styles()
if st.session_state.page == "Home":
    homepage()
elif st.session_state.page == "Dashboard":
    dashboard(data)
    