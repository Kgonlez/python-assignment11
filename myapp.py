import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import plotly.express as px

df=px.data.gapminder()

countries = df['country'].unique()

app= dash.Dash(__name__)
server = app.server

#layout
app.layout = html.Div([
    html.H1("GDP Per Capita Over Time"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value = 'Canada'
    ),
    dcc.Graph(id='gdp-growth')
])
#Callback
@app.callback(
    Output('gdp-growth','figure'),
    [Input('country-dropdown','value')]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f"GDP Per Capita Over Time: {selected_country}"
    )
    return fig

#Server run
if __name__ == '__main__':
    app.run(debug=True)