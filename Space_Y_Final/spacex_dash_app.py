# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

temp_list = list(spacex_df['Launch Site'].unique())
launch_sites = []
launch_sites.append({'label': 'All Sites', 'value': 'ALL'})
for site in temp_list:
    launch_sites.append({'label': site, 'value': site})
# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown', options=launch_sites, value='ALL', placeholder='Select a Launch Site here', searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000, marks={0: '0 kg', 1000: '1000 kg',
                                                                                                        2000: '2000 kg',3000: '3000 kg',
                                                                                                        4000: '4000 kg',5000: '5000 kg',
                                                                                                        6000: '6000 kg',7000: '7000 kg',
                                                                                                        8000: '8000 kg',9000: '9000 kg',
                                                                                                        10000: '10000 kg'}, 
                                                                                                        value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ]),

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'), Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        data = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(data, values='class', names = 'pie chart names', title='All Successful Launches')
        return fig
    else:
        data  = spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(data, names = 'pie chart names',title = 'Successful Launches at '+site_dropdown)
        return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'), [Input(component_id='site-dropdown', component_property='value'), Input(component_id='payload-slider', component_property='value')])

def update_scatter_chart(site_dropdown, payload_slider):
    if site_dropdown == 'All Sites':
        lo, hi = payload_slider
        data = spacex_df
        mass = (data['Payload Mass (kg)'] > lo) & (data['Payload Mass (kg)'] < hi)
        fig = px.scatter(
            df[mass], x="Payload Mass (kg)", y="class",
            color="Booster Version",
            size='Payload Mass (kg)',
            hover_data=['Payload Mass (kg)'])
    else:
        lo, hi = payload_slider
        data  = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]
        mass = (data['Payload Mass (kg)'] > lo) & (data['Payload Mass (kg)'] < hi)
        fig = px.scatter(
            df[mass], x="Payload Mass (kg)", y="class",
            color="Booster Version",
            size='Payload Mass (kg)',
            hover_data=['Payload Mass (kg)'])
    return fig        
# Run the app
if __name__ == '__main__':
    app.run_server(port=8060)
