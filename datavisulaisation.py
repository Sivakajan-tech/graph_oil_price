from h2o_wave import site, ui, Q, app, main, data
import pandas as pd


@app('/hello')
async def serve(q):
    # Grab a reference to the page at route '/hello'
    # page = site['/hello']
    if not q.client.intialized:
        set_up_ui_for_new_user(q)
        plot_view(q)
    elif q.args.table:
        table_view(q)
    elif q.args.plot:
        plot_view(q)
    elif (q.args.x_variable is not None) or (q.args.y_variable is not None):
        q.client.x_variable = q.args.x_variable
        q.client.y_variable = q.args.y_variable
        plot_view(q)
    # Finally, save the page.
    await q.page.save()


def set_up_ui_for_new_user(q):
    # insted of using site to give a page name, we use app

    q.page['meta'] = ui.meta_card(
        # make the window responsive, and arrnge the every card
        box='',
        layouts=[
            ui.layout(breakpoint='xs', zones=[
                ui.zone('header'),
                ui.zone('navigation'),
                ui.zone('content'),
            ]),
        ])

    q.page['header'] = ui.header_card(
        subtitle="My first Wave App",
        box='header',  # in top left corner with 2 unit height and width
        title='''Wave App!! Looking Awesome''',
    )

    q.page['navigation'] = ui.tab_card(
        box='navigation',
        items=[
            ui.tab(name='table', label="Table View"),
            ui.tab(name='plot', label="Plot View"),
        ]
    )
    q.client.intialized = True
    q.client.x_variable = "c1"
    q.client.y_variable = "c2"


def table_view(q):
    del q.page['plot_view']
    df = aggregated_data()
    q.page['table_view'] = ui.form_card(
        box='content',
        items=[
            ui.text_xl(content='Table View'),
            ui.table(
                name="aggregated_data_table",
                columns=[ui.table_column(name=col, label=col)
                         for col in df.columns.values],
                rows=[
                    ui.table_row(
                        name=str(i),
                        cells=[
                            str(df[col].values[i]) for col in df.columns.values
                        ]) for i in range(len(df))
                ],
                downloadable=True
            )
        ]
    )


def plot_view(q):
    del q.page['table_view']

    df = aggregated_data()

    q.page['plot_view'] = ui.form_card(
        box='content',
        items=[
            ui.text_xl(
                f'Relationship between {q.client.x_variable} and {q.client.y_variable}'),
            ui.inline(items=[
                ui.dropdown(
                    name='x_variable',
                    label="X Variable",
                    choices=[
                        ui.choice(name=col, label=col) for col in df.columns.values
                    ],
                    trigger=True,
                    value=q.client.x_variable,
                ),
                ui.dropdown(
                    name='y_variable',
                    label="Y Variable",
                    choices=[
                        ui.choice(name=col, label=col) for col in df.columns.values
                    ],
                    trigger=True,
                    value=q.client.y_variable,
                ),
            ]),
            ui.visualization(
                data=data(
                    fields=df.columns.tolist(),
                    rows=df.values.tolist(),
                    pack=True,
                ),
                plot=ui.plot(marks=[ui.mark(
                    type='point',
                    x=f'={q.client.x_variable}', x_title='',
                    y=f'={q.client.y_variable}', y_title='',
                    shape='circle', size='=counts'
                )])
            )
        ]
    )

def aggregated_data():
    df = pd.DataFrame(
        dict(
            c1=range(0, 100),
            c2=range(1, 101),
            counts=range(2, 102)
        ))
    print(df.head())
    return df
# def aggregated_data():
#     df = pd.read_csv('./oil.csv')
#     df.dcoilwtico = df.dcoilwtico.interpolate(method='linear', limit_direction='forward', axis=0)
#     df.dcoilwtico = df.dcoilwtico.fillna(method='bfill')
#     print(df.head())
#     return df