'''
Documentação arquivos pages.py
'''
from time import sleep
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from genres.service import GenreService



def show_genres():
    '''
    Documentação função
    '''
    
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de generos')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid',
            )
    else:
        st.warning('Nenhum genero encontrado')
    
    st.title('Cadastrar novo genero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(
            name=name,
        )
        if new_genre:
            st.success(f'Genero {name} cadastrado com sucesso')
            sleep(3)
            st.rerun()
        else:
            st.error('Erro ao cadastrar genero, verique os campos')

    