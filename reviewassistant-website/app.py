import streamlit as st
from streamlit import session_state
import requests

API_URL = 'http://127.0.0.1:8000/'
RATINGS_EXPLAINED = ["Very bad", "Bad", "Acceptable", "Good", "Excellent"]

if 'criteria_clicked' not in session_state:
    session_state.criteria_clicked = False
if 'reviews_clicked' not in session_state:
    session_state.reviews_clicked = False


def click_criteria_button():
    session_state.criteria_clicked = True
    session_state.reviews_clicked = False


def click_reviews_button():
    session_state.reviews_clicked = True


@st.cache_data()
def get_criteria():
    # res = requests.get(API_URL + 'criteria', product=product)
    # if res.status_code == 200:
    if True:
        # criteria = res.json()
        criteria = ["Coverage", "Longevity", "Application", "Shade range",
                    "Packaging", "Skincare benefits"]
    return criteria


@st.cache_data()
def get_reviews():
    # res = requests.get(API_URL + 'reviews', product=product, rated_criteria=rated_criteria)
    # if res.status_code == 200:
    if True:
        # reviews = res.json()
        reviews = [
            "asdiub aosdubfqeriuobv opubqdfipuerbfipvberq",
            "asdiufbiqer rfiuqbaucewq432q coijqhweofih oqwehfouqeh ohuiou",
            "qoedfi pqoiehfoqh pqiewhfpqierhf ewpifh    [weofjojhh]"
        ]
    return reviews


def rate_criteria(criteria: list[str]):

    '''How would you rate the following?'''
    rated_criteria = {}
    for i, criterium in enumerate(criteria):
        with st.container():  # Creates a row
            col1, col2 = st.columns([1,3])
            # Label
            col1.text(criterium.title())
            # Slider for the rating
            rated_criteria[criterium] = col2.slider(
                criterium.title(),
                min_value=1,
                max_value=len(RATINGS_EXPLAINED),
                # captions=RATINGS_EXPLAINED if i == 0 else None,
                value=3,
                key=f'criterium_{i}',
                # horizontal=True
                label_visibility='collapsed'
            )
    st.button("Go!", key='go_reviews', on_click=click_reviews_button)


def show_reviews(reviews: list[str]):
    '''Here are some reviews you could use.'''
    for i, review in enumerate(reviews):
        st.text_area(f"Review #{i+1}", review, key=f'review_{i}')


'''# Review Writing Assistant'''

product = st.text_area(label="Which product do you want to review?",
                       value="Maybelline Instant Age Rewind Eraser Dark Circles Treatment Concealer",
                       max_chars=100)

go_criteria = st.button("Go!", key='go_criteria', on_click=click_criteria_button)

if session_state.criteria_clicked:
    session_state.show_criteria = True
    criteria = get_criteria()
    if criteria:
        rate_criteria(criteria)
    else:
        st.error("Uh oh... something went wrong 😵")

if session_state.reviews_clicked:
    reviews = get_reviews()
    if reviews:
        show_reviews(reviews)
    else:
        st.error("Uh oh... something went wrong 😵")
