import dash
import dash_bootstrap_components as dbc
from dash import html
#importa librerías

navegador= dbc.Container([ #Crea la variable navegador y en ella un Container
    dbc.Row([#crea una fila
        html.Hr(),#añade un espacio
        dbc.Col(html.H1("Medición de asentamientos por tuneladora"), md=12, style={'color':'white', 'background-color':'#17242d'}),
        #Crea una columna con titulo, espacio 6, define color de letra y fondo
        html.Hr(), #añade un espacio
    ])
])