import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#Uninstalls Android
df_uninstalls = pd.read_csv('perdas_usuario.csv')
df_uninstalls["Data"] = pd.to_datetime(df_uninstalls["Data"], format="%d/%m/%Y")
columns = {
    'Perda de usuários (Todos os usuários, Todos os eventos, Por intervalo, Diária): Todos os países / todas as regiões': 'Desinstalações'
}
df_uninstalls = df_uninstalls.rename(columns=columns)

#Acquisitions Android
df_acquisitions = pd.read_csv('aquisicoes_por_dia.csv')
df_acquisitions["Data"] = pd.to_datetime(df_acquisitions["Data"], format="%d/%m/%Y")
columns = {
    'Aquisição de usuários (Novos usuários, Todos os eventos, Por intervalo, Diária): Brasil': 'Aquisições por dia'
}
df_acquisitions = df_acquisitions.rename(columns=columns)

#Acquisitions IOS
df_acquisitions_IOS = pd.read_csv('instalacoes_ios.csv')
df_acquisitions_IOS["Data"] = pd.to_datetime(df_acquisitions_IOS["Data"], format="%d/%m/%Y")

#Uninstalls IOS
df_uninstalls_IOS = pd.read_csv('desinstalacoes_ios.csv')
df_uninstalls_IOS["Data"] = pd.to_datetime(df_acquisitions_IOS["Data"], format="%d/%m/%Y")

#Engagement
engagement = pd.read_csv('engajamento.csv')

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Análise dados App Tecknus"


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src=app.get_asset_url('logo2.png'), className="header-emoji"),
                html.P(
                    children="Análise dos dados de instalações e desinstalações no último ano, uso diário,"
                             " e engajamento dos usuários.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="df_acquisitions_android",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": df_acquisitions["Data"],
                                    "y": df_acquisitions["Aquisições por dia"],
                                    "type": "lines",

                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Instalações Android - último ano",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {

                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="df_uninstalls_android",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": df_uninstalls["Data"],
                                    "y": df_uninstalls["Desinstalações"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Desinstalações Android - último ano",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="df_acquisitions_IOS",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": df_acquisitions_IOS["Data"],
                                    "y": df_acquisitions_IOS["Instalações"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Instalações IOS - último ano",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="df_uninstalls_IOS",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": df_uninstalls_IOS["Data"],
                                    "y": df_uninstalls_IOS["Desinstalações"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Desinstalações IOS - último ano",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    dcc.Graph(
                        id='example-graph',
                        figure={
                            'data': [
                                {'x': engagement['tela'], 'y': engagement['engajamento'],'type': 'bar', 'name': 'Engajamento (%)'},
                                {'x': engagement['tela'], 'y': engagement['tempo'], 'type': 'bar', 'name': 'Tempo (%)'},

                            ],
                        'layout': {
                            'title': 'Engajamento dos usuários nas telas do app'
                            }
                        }
                    )
                ),


            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)