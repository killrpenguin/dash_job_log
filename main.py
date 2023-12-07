from dash import Dash, html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children="David's Job Log", className='header-title'),
    html.Tr(children=[
        html.Td([
            html.H4(children="Company Name:", className="form_names")
        ]),
        html.Td(children=[
            dcc.Input(
                id="comp_name",
                type="text",
                placeholder="",
                value=" "
            ),
        ]),
    ],
        className='table_row'),
    html.Tr(children=[
        html.Td([
            html.H4(children="Job Title:", className="form_names")
        ]),
        html.Td(children=[
            dcc.Input(
                id="job_title",
                type="text",
                placeholder="",
                value=""
            )
        ])
    ],
        className='table_row'),
    html.Tr(children=[
        html.Td([
            html.H4(children="Web Link:", className="form_names")
        ]),
        html.Td(children=[
            dcc.Input(
                id="web_link",
                type="text",
                placeholder="",
                value=""
            )
        ])
    ],
        className='table_row'),
    html.Tr(children=[
        html.Td([
            html.H4(children="Contact Type:", className="form_names")
        ]),
        html.Td(children=[
            dcc.Dropdown(options=['Website', 'Paper Application', 'Other'],
                         placeholder="Contact Type",
                         id="how_contacted",
                         value=""
                         )
        ]),
    ],
        className='table_row'),
    html.Tr(children=[
        html.Td(children=[
            html.H4("Response Type:", className="form_names")
        ]),
        html.Td(children=[
            dcc.Dropdown(options=['No Response', 'Return Call', 'Interview'],
                         placeholder="Enter Response",
                         id='contacted_result',
                         value=""
                         )
        ])
    ], className='table_row'),
    html.Button('Submit', id='submit_button', formNoValidate=True, className='button', n_clicks=0)
],
    className='form_element', id='job_log_form'
)


@app.callback(
    Output(component_id='job_log_form', component_property='children'),
    Input(component_id='submit_button', component_property='value'),
    State(component_id='comp_name', component_property='value')

)
def update_output(other, value):
    raise PreventUpdate


if __name__ == '__main__':
    app.run_server(debug=True)
