'''
Documentação
'''
import pandas as pd
import streamlit as st
from movies.service import MovieService
from reviews.service import ReviewService
from st_aggrid import AgGrid


def show_reviews():
    '''
    Documentação função
    '''
    review_service = ReviewService()
    review = review_service.get_reviews()
    
    if review:
        st.write('Lista de Avaliações')
        reviews_df = pd.json_normalize(review)
        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid',
            )
    else:
        st.warning('Nenhuma Avaliação encontrada')

    
    st.title('Cadastrar Avaliação')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comentário sobre o filme', max_chars=50)

    if st.button('Cadastrar Review'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )

        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a avaliação. Verique os campos')

    