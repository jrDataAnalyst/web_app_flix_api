'''
Coração do projeto
'''
from time import sleep
import streamlit as st
from home.page import show_home
from genres.pages import show_genres
from actors.pages import show_actors
from movies.pages import show_movies
from reviews.pages import show_reviews
from login.page import show_login


def main():
    '''
    Função principal do projeto
    '''

    if 'token' not in st.session_state:
        show_login()
    else:
        menu_options = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Inicio', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
        )
        if menu_options == 'Inicio':
            show_home()
        if menu_options == 'Gêneros':
            show_genres()
        if menu_options == 'Atores/Atrizes':
            show_actors()
        if menu_options == 'Filmes':
            show_movies()
        if menu_options == 'Avaliações':
            show_reviews()
        if st.sidebar.button("Sair"):
            # Ação ao clicar no botão "Sair"
            st.session_state.clear()  # Limpa o estado da sessão
            st.sidebar.success("Sessão encerrada")  # Mensagem de confirmação
            sleep(3)
            st.rerun()


if __name__ == '__main__':
    main()





