from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt




# Sidebar com menu personalizado
with st.sidebar:
    selected = option_menu(
        menu_title="ATEX VIII - Home",  # Título opcional
        options=[
            "Introdução",
            "Pesquisa e Gráficos",
            "Panfleto Educativo",
            "Proposta de Atividade Prática",
            "Pontos de coleta"
        ],
        icons=["book", "bar-chart", "file-earmark-text", "clipboard-check", "geo-alt"],
        menu_icon="house",  # Ícone do menu (acima)
        styles={
    "container": {"padding": "5px", "background-color": "#07070700"},
    "nav-link": {"color": "#333"},
    "nav-link-selected": {"background-color": "#092c60", "color": "white"},
}

        
        
    )



if selected == "Introdução":
    # Logo da UNIFENAS
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/SantanaDZ/images-projects/refs/heads/main/atex8_imgs/unifenas.jpg" width="150">
    </div>
    """,
    unsafe_allow_html=True
    )
    # Cabeçalho com informações do aluno
    st.markdown("""
    <div style="background-color: #f0f4f8; padding: 1px; border-radius: 15px; margin-top: 1px; margin-bottom: 10px;text-align: center;">
        <h2 style="color: #1f3b70; margin-bottom: 10px;">ATEX VIII</h2>
        <p style="margin: 0;"><strong>Aluno:</strong> André Santana Martins</p>
        <p style="margin: 0;"><strong>Curso:</strong> Análise e Desenvolvimento de Sistemas</p>
        <p style="margin: 0;"><strong>Período:</strong> 3º Período</p>
    </div>
    """, unsafe_allow_html=True)

    # Título da seção
    st.header("📘 Introdução")

    # Texto da introdução
    st.markdown("""
    Este projeto, desenvolvido no contexto da disciplina ATEX VIII do curso de Análise e Desenvolvimento de Sistemas da UNIFENAS, tem como foco a conscientização sobre os impactos ambientais e sociais causados pelo descarte inadequado de lixo eletrônico. Por meio de uma aplicação interativa desenvolvida com Streamlit, o trabalho apresenta dados estatísticos, análises gráficas, informações legislativas e propostas educativas para estimular o descarte consciente e promover a logística reversa. Além disso, inclui uma atividade prática com coleta real de resíduos eletrônicos e mapeamento de pontos de coleta em Belo Horizonte, reforçando a importância da tecnologia como ferramenta de transformação ambiental e social.

                
    **Para explorar o conteúdo, utilize o menu lateral (ícone no canto superior esquerdo).**            
    
                
    Este projeto foi feito com base na ATEX VII, que tem como objetivos:

    - 📌 Sensibilizar a comunidade sobre os **impactos ambientais e à saúde** do descarte inadequado de lixo eletrônico.  
    - ♻️ Promover a **coleta correta** e o manejo ambientalmente saudável de resíduos eletrônicos.  
    - 🎨 Desenvolver a **criatividade, trabalho em equipe, comunicação e relações interpessoais** dos alunos.  
    - 🌱 Contribuir para a **redução da liberação de substâncias nocivas** ao ar, água e solo.
    """)




elif selected == "Pesquisa e Gráficos":
    st.header("📊 Pesquisa sobre os Impactos do Lixo Eletrônico e Legislação Vigente")
    sub_menu = st.selectbox("Escolha uma seção da Pesquisa:", ["Análises","Dados e Gráficos" ])

    if sub_menu == "Dados e Gráficos":
        st.subheader("📈 Dados e Gráficos sobre Lixo Eletrônico no Brasil")

        # st.markdown()

        # Dados simulados (você pode substituir por dados reais se tiver)
        dados1 = pd.DataFrame({
            "Ano": list(range(2010, 2025)),
            "Milhões de toneladas": [
                0.9, 1.1, 1.3, 1.4, 1.6,
                1.8, 1.9, 2.0, 2.05, 2.1,
                2.2, 2.25, 2.3, 2.35, 2.4
            ]
        })
        
        '''Crescimento Estimado do Lixo Eletrônico no Brasil (2010–2024)'''
            # Gráfico animado de linha
        fig = px.line(
            dados1,
            x="Ano",
            y="Milhões de toneladas",
            title=" ",
            markers=True,
        )

        # Personalização
        fig.update_traces(line=dict(color="#1f77b4", width=2))
        fig.update_layout(
            yaxis_title="Milhões de toneladas",
            xaxis_title="Ano",
            title_x=0.5,
            template="plotly_white"
        )

        # Exibir gráfico
        st.plotly_chart(fig, use_container_width=False)

        st.markdown("Fonte: Global E-Waste Monitor (ONU) e Instituto Akatu")

        # === Dados principais ===
        dados2= pd.DataFrame({
            'Ano': [2019, 2021, 2023],
            'Lixo Eletrônico (milhões toneladas)': [2.1, 2.25, 2.35],
            '% Reciclado': [2, 3, 4]
        })

        # Layout em colunas
        col1, col2 = st.columns(2)

        with col1:
            fig1 = px.bar(
                dados2,
                x='Ano',
                y='Lixo Eletrônico (milhões toneladas)',
                title='📦 Lixo Eletrônico Gerado por Ano',
                color_discrete_sequence=['#1f77b4']
            )
            fig1.update_layout(height=400)
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            fig2 = px.bar(
                dados2,
                x='Ano',
                y='% Reciclado',
                title='♻️ Percentual de Lixo Eletrônico Reciclado',
                color_discrete_sequence=['#2ca02c']
            )
            fig2.update_layout(height=400, yaxis_range=[0, 10])
            st.plotly_chart(fig2, use_container_width=True)

        st.dataframe(dados2, hide_index=True)

        st.markdown("---")
        st.markdown("### 🧩 Composição Média do Lixo Eletrônico no Brasil")

        composicao = pd.DataFrame({
            'Categoria': ['Celulares', 'Computadores', 'Eletrodomésticos', 'Outros'],
            'Porcentagem': [25, 20, 30, 25]
        })

        col3, col4 = st.columns(2)
        with col3:
            ''' ***Composição do Lixo Eletrônico*** '''
            fig3 = px.pie(
                composicao,
                names='Categoria',
                values='Porcentagem',
                title='',
                color_discrete_sequence=px.colors.sequential.RdBu
            )
            fig3.update_traces(textposition='inside', textinfo='percent+label')
            fig3.update_layout(height=500)
            st.plotly_chart(fig3, use_container_width=False)

        st.markdown("---")
        

        percepcao = pd.DataFrame({
            'Região': ['Total Brasil', 'Sudeste', 'Sul', 'Centro-Oeste', 'Nordeste + Belém'],
            'Porcentagem': [87, 87, 89, 84, 85]
        })
        
        with col3:
            st.markdown("### 🧠 Percepção da População Brasileira sobre Lixo Eletrônico")
            ''' **Já ouviu falar em lixo eletrônico (%)** '''
            fig4 = px.bar(
                percepcao,
                x='Região',
                y='Porcentagem',
                text='Porcentagem',
                title='',
                color_discrete_sequence=['#6CA635']
        )
            fig4.update_traces(texttemplate='%{text}%', textposition='outside')
            fig4.update_layout(
                yaxis_title='Porcentagem (%)',
                yaxis_range=[0, 100],
                height=400
            )
            st.plotly_chart(fig4, use_container_width=True)


    

    elif sub_menu == "Análises":
        st.subheader("🧠 Análises")
        st.header("📘 Introdução ao Lixo Eletrônico")

        # Introdução
        st.markdown("""
        > O lixo eletrônico (ou **Resíduos de Equipamentos Elétricos e Eletrônicos - REEE**) é um dos resíduos que mais crescem no mundo devido ao avanço tecnológico e à obsolescência programada.  
        > No Brasil, o descarte inadequado desses materiais gera impactos **ambientais, sociais e econômicos**.
        """)

        # Pesquisa aborda
        st.subheader("🔍 Esta pesquisa aborda:")
        st.markdown("""
        - 🌱 **Impactos do lixo eletrônico**  
        - ⚖️ **Legislação brasileira sobre o tema**  
        - 🔎 **Estudos e Soluções**
        """)

        # Impactos
        st.subheader("💥 Impactos do Lixo Eletrônico")

        st.markdown("### 🌍 Impactos Ambientais")
        st.markdown("""
        - ☠️ **Contaminação do solo e água**: Chumbo, mercúrio e cádmio infiltram-se no solo e atingem lençóis freáticos.  
        - 🌫️ **Poluição do ar**: A queima de componentes eletrônicos libera gases tóxicos.  
        - 🚯 **Acúmulo em aterros**: O Brasil gera **2,1 milhões de toneladas** de lixo eletrônico por ano, mas recicla apenas **3%** (ONU, 2021).
        """)

        st.markdown("### 🏥 Impactos Sociais e à Saúde")
        st.markdown("""
        - ⚠️ Trabalhadores de lixões informais são expostos a **substâncias perigosas**, podendo desenvolver doenças respiratórias e câncer.  
        - 🧬 Comunidades próximas a áreas de descarte sofrem com **contaminações químicas crônicas**.
        """)

        st.markdown("### 💸 Impactos Econômicos")
        st.markdown("""
        - 💰 **Perda de materiais valiosos** (ouro, prata, cobre) que poderiam ser reciclados.  
        - 🏥 **Custos com saúde pública** devido à contaminação ambiental.
        """)

        # Legislação
        st.subheader("📜 Legislação Brasileira sobre Lixo Eletrônico")

        st.markdown("### 🧾 Política Nacional de Resíduos Sólidos (Lei 12.305/2010)")
        st.markdown("""
        - ♻️ Cria a **logística reversa**: fabricantes/importadores devem recolher seus produtos.  
        - 🗑️ Estabelece a obrigatoriedade de pontos de coleta acessíveis à população.
        """)

        st.markdown("### 📊 Decreto 10.240/2020")
        st.markdown("""
        - Regulamenta a logística reversa com metas obrigatórias:  
        - 📅 **2025**: 17% dos produtos devem ser coletados  
        - 📅 **2031**: 50% dos produtos devem ser coletados
        """)

        st.markdown("### 📚 Norma Técnica ABNT NBR 16156:2013")
        st.markdown("""
        Essa norma orienta empresas na **manufatura reversa** de REEE.  
        Ela define:
        - ✅ Identificação e classificação dos resíduos  
        - 🧰 Desmontagem e separação de componentes  
        - 🧪 Armazenamento e transporte seguro  
        - ♻️ Destinação final adequada  

        _Obs: não é obrigatória, mas serve como modelo de boas práticas._
        """)

        # Estudos e soluções
        st.subheader("🔎 Estudos e Soluções")

        st.markdown("### 🏆 Casos de Sucesso")
        st.markdown("""
        - 📦 **Programa "Descarte Certo" (Samsung)**: coletou mais de 5 mil toneladas em 5 anos.  
        - 👥 **Coopermiti (SP)**: recicla mais de **200 toneladas/mês** de lixo eletrônico.
        """)

        st.markdown("### 🚧 Desafios")
        st.markdown("""
        - 📉 Falta de conscientização da população  
        - 🏭 Infraestrutura insuficiente para triagem e reciclagem
        """)

        # Conclusão
        st.subheader("✅ Conclusão")
        st.markdown("""
        O Brasil já tem **legislação robusta**, mas ainda enfrenta desafios para a implementação efetiva da logística reversa.  
        É essencial fortalecer políticas públicas e campanhas de **educação ambiental** para ampliar a conscientização e a reciclagem.
        """)

        # Referências
        st.subheader("📚 Referências")
        st.markdown("""
        - ONU (Global E-Waste Monitor, 2021)  
        - Ministério do Meio Ambiente (PNRS)  
        - ABRELPE (Associação Brasileira de Empresas de Limpeza Pública)
        """)


elif selected == "Panfleto Educativo":
    st.header("📄 Panfleto Educativo")
    '''
    
    '''
    st.image('https://raw.githubusercontent.com/SantanaDZ/images-projects/refs/heads/main/atex8_imgs/PANFLETO1.png', width= 400)

elif selected == "Proposta de Atividade Prática":
    st.header("📝 Proposta de Atividade Prática")     
    # Título do bloco objetivo
    st.markdown("### 🎯 Objetivo")
    st.markdown("""
    Promover a conscientização dos moradores sobre os **impactos ambientais** do descarte inadequado de lixo eletrônico e incentivar **práticas corretas de descarte**, por meio da distribuição de panfletos informativos e da instalação de um ponto de coleta.
    """)

    # Público-alvo
    st.markdown("### 👥 Público-alvo")
    st.markdown("Moradores de um **pequeno condomínio residencial**.")

    # Descrição com colunas e subtítulos
    st.markdown("### 🛠️ Etapas da Atividade")

    st.markdown("#### 1️⃣ Criação dos Panfletos Informativos")
    st.markdown("""
    - ✅ O que é lixo eletrônico  
    - 🧩 Exemplos de itens (pilhas, carregadores, celulares antigos, etc.)  
    - ⚠️ Riscos ambientais e à saúde  
    - 🔁 Importância da reciclagem e descarte consciente  
    - 📍 Local de coleta no condomínio
    """)

    st.markdown("#### 2️⃣ Distribuição dos Panfletos")
    st.markdown("""
    - 📬 Entregar nas caixas de correio ou portas  
    - 📌 Fixar em murais do condomínio (elevadores, portaria)
    """)

    st.markdown("#### 3️⃣ Instalação da Caixa de Coleta")
    st.markdown("""
    - 🗳️ Caixa com identificação: “Descarte de Lixo Eletrônico”  
    - ☔ Proteção contra intempéries  
    - ♻️ Esvaziamento periódico
    """)

    st.markdown("#### 4️⃣ Acompanhamento e Divulgação dos Resultados")
    st.markdown("""
    - 📏 Monitoramento do volume/tipo de materiais  
    - 📣 Divulgação nos murais (ex: quantidade coletada)  
    - 🔁 Reforço mensal da campanha (se necessário)
    """)

    # Duração da campanha
    st.markdown("### 🕒 Duração da Campanha")
    st.markdown("📆 **30 dias**, com possibilidade de extensão conforme a adesão.")

    # Resultado com imagem
    st.markdown("### 📦 Resultado Final")
    st.markdown("""
    **Materiais recolhidos ao fim da campanha:**

    - 1 placa mãe  
    - 1 SSD  
    - 1 slot de memória RAM  
    - 2 pilhas  
    - 1 HD de notebook  
    - 1 HD externo  
    - 3 aparelhos celulares

    """)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://raw.githubusercontent.com/SantanaDZ/images-projects/refs/heads/main/atex8_imgs/ITENS_RECOLHIDOS.jpeg", width=500)
    
    # Gráfico de itens coletados
    # st.subheader("📊 Itens Recolhidos")
    dados = {
        "Item": [
            "Placa mãe", "SSD", "Memória RAM",
            "Pilhas", "HD de notebook", "HD externo",
            "Celulares"
        ],
        "Quantidade": [1, 1, 1, 2, 1, 1, 3]
    }
    with col1:
        fig = px.pie(
            names=dados["Item"],
            values=dados["Quantidade"],
            title="Distribuição dos Itens Coletados",
            color_discrete_sequence=px.colors.sequential.RdBu
            
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""✅ **Todo o material foi corretamente descartado.**
        """)
    

elif selected == "Pontos de coleta":
    st.header("📍Pontos de Coleta de **lixo eletrônico** em Belo Horizonte") 

    '''
    ---
### MG Recicla Reciclagem de Lixo Eletrônico 
- 📞 Telefone: (31) 3565-5294 
- 🌐 Site: https://www.mgrecicla.com/  
- 📍 Endereço: Rua Sararé, 47 - Jardinópolis, Belo Horizonte - MG, 30512-010   
   
    '''
    df1 = pd.DataFrame({
    'latitude': [-19.9408320319223],
    'longitude': [-44.00157405899103]
    })
    st.map(df1, use_container_width=False, width=300, height=300)
    '''
    ---
### BH Recycle Electronic Waste Recycling and Other scraps.    
- 📞 Telefone: (31) 3063-0688  
- 🌐 Site: http://www.bhrecicla.com.br/  
- 📍 Endereço: Av. General David Sarnoff, 2690 - Cidade Industrial, Contagem - MG, 32210-110   
    '''

    df2 = pd.DataFrame({
    'latitude': [-19.95710236328602],
    'longitude': [-44.03497269263149]
    })
    st.map(df2, use_container_width=False, width=300, height=300)

    '''
    ---
### Ponto de Coleta de Lixo Eletrônico - PROPAM
- 📞 Telefone: (31) 3277-7422 
- 🌐 Site: http://www.emile.net.br/  
- 📍 Endereço: R. Rad. Ubaldo Ferreira, 20 - Castelo, Belo Horizonte - MG, 31330-294   
    '''
    df3 = pd.DataFrame({
    'latitude': [-19.8766631711202],
    'longitude': [-43.99402519593448]
    })
    st.map(df3, use_container_width=False, width=300, height=300)






   
