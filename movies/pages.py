'''
Documentação
'''
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MovieService



def show_movies():
    '''
    Documentação função
    '''
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de filmes')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado')

    
    st.title('Cadastrar novo filme')

    title = st.text_input('Titulo filme')
    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_name = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_name.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area('Resumo', max_chars=100)

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genre_name[selected_genre_name],
            actors =selected_actors_ids, 
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar filmes. Verifique os campos')



