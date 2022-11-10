from h2o_wave import ui, app, main, data
import pandas as pd
import sys


def fileHandler():
    fileName = './DataSheet.csv'
    try:
        f = open(fileName, 'r')
    except FileNotFoundError:
        print(f"File {fileName} not found.  Aborting")
        sys.exit(1)
    except OSError:
        print(f"OS error occurred trying to open {fileName}")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected error opening {fileName} is", repr(err))
        sys.exit(1)  # or replace this with "raise" ?
    else:
        with f:
            return pd.read_csv(fileName)


def contentTaker():
    file = fileHandler()
    file.date = file.date.interpolate(
        method='linear',
        limit_direction='forward',
        axis=0
    )
    file.date = file.date.fillna(method='bfill')
    listOfData = list(file.itertuples(index=False, name=None))
    return listOfData[:1100]


dataSet = contentTaker()


def stringifyContent(intList):
    return [list(map(str, i)) for i in intList]


@app('/plot')
async def controller(q):
    # Grab a reference to the page at route '/hello'
    # page = site['/hello']
    if not q.client.intialized:
        mainApp(q)
        table_view(q)
        # footer(q)
    elif q.args.table:
        table_view(q)
    elif q.args.plot:
        plot_view(q)

    # Finally, save the page.
    await q.page.save()


def mainApp(q):
    # insted of using site to give a page name, we use app

    q.page['activePageController'] = ui.meta_card(
        # make the window responsive, and arrnge the every card
        theme='benext',
        box='activePageController',
        layouts=[
            ui.layout(
                # Breakpoints suits to device range
                breakpoint='l',
                zones=[
                    ui.zone('header'),
                    ui.zone('navigator'),
                    ui.zone('content'),
                    ui.zone('footer'),
                ]),
        ])

    q.page['navigator'] = ui.tab_card(
        box='navigator',
        items=[
            ui.tab(name='table', label="Table View"),
            ui.tab(name='plot', label="Plot View"),
        ]
    )
    q.page['header'] = ui.header_card(
        box='header',  # in top left corner with 2 unit height and width
        subtitle="My first Wave App",
        icon='BarChartVerticalFilterSolid',
        title='''Wave App!! Looking Awesome''',
    )

    q.page['footer'] = ui.footer_card(
        box='footer',
        caption='''
        A Try On Wave for the First Time!!!

        Made with 💛 by Sivakajan Sivaparan!.'''
    )
    q.client.intialized = True


def table_view(q):
    del q.page['plot_view']
    stringDataSet = stringifyContent(dataSet)
    q.page['table_view'] = ui.form_card(
        box='content',
        items=[
            ui.text_xl(content='Table View'),
            ui.table(
                name="data_table",
                columns=[
                    ui.table_column(
                        name='date', label='Date', sortable=True, searchable=True, max_width='400'),
                    ui.table_column(
                        name='price', label='Price', sortable=True, ),
                ],
                rows=[
                    ui.table_row(
                        name=str(1),
                        cells=stringDataSet[i]
                    ) for i in range(len(stringDataSet))
                ],
                downloadable=True,
                width="700px",
                height='600px',
                resettable=True,
            ),
        ],
    )


def plot_view(q):
    del q.page['table_view']
    q.page['plot_view'] = ui.form_card(
        box='content',
        items=[

            ui.text_xl(
                f'Oil Price between 2013 to 2017 -> A Sample Data Set'),
            ui.visualization(
                data=data(
                    fields=['date', 'price'],
                    size=8,
                    rows=dataSet,
                    pack=True,
                ),
                height='600px',
                plot=ui.plot(marks=[
                    ui.mark(type='line', x='=date', y='=price',
                            x_title="Date", y_title="LKR", color='yellow'),
                    ui.mark(type='area', x_scale='time-category',
                            x='=date', y='=price', y_min=0, size='',)
                ])
            )
        ]
    )
