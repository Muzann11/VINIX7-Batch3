# ==============================================================
# DASHBOARD ANALISIS AUTO MPG - Track B/2
# Dibuat oleh: Muhammad Fauzan Div Data Sains VINIX7
# Python: 3.11.13
# ==============================================================
# Cara jalankan:
# 1. panel serve dashboard_auto_mpg.py --show
# ==============================================================

import pandas as pd
import hvplot.pandas
import panel as pn
from ucimlrepo import fetch_ucirepo

pn.extension('tabulator')

# ambil dataset dari UCI
auto_mpg = fetch_ucirepo(id=9)
X = auto_mpg.data.features
y = auto_mpg.data.targets
df = pd.concat([X, y], axis=1)

# simple data cleaning 
df.dropna(inplace=True)
df['horsepower'] = df['horsepower'].astype(float)
origin_map = {1: 'USA', 2: 'Europe', 3: 'Japan'}
df['origin'] = df['origin'].map(origin_map)

# widget interaktif 
year_slider = pn.widgets.IntRangeSlider(
    name='Model Year Range',
    start=int(df['model_year'].min()),
    end=int(df['model_year'].max()),
    value=(70, 82),
    step=1
)

origin_select = pn.widgets.CheckBoxGroup(
    name='Select Origin',
    options=list(df['origin'].unique()),
    value=list(df['origin'].unique())
)

# fungsi filter data
@pn.depends(year_slider, origin_select)
def filtered_data(year_slider, origin_select):
    return df[
        (df['model_year'] >= year_slider[0]) &
        (df['model_year'] <= year_slider[1]) &
        (df['origin'].isin(origin_select))
    ]

# visualisasi 1: Distribusi MPG
@pn.depends(year_slider, origin_select)
def plot_distribution(year_slider, origin_select):
    data = filtered_data(year_slider, origin_select)
    return data.hvplot.hist(
        'mpg', bins=20, color='skyblue',
        title='Distribusi Nilai MPG (Miles per Gallon)'
    )

# visualisasi 2: Rata-rata MPG per Cylinders
@pn.depends(year_slider, origin_select)
def plot_avg_mpg_cyl(year_slider, origin_select):
    data = filtered_data(year_slider, origin_select)
    return data.groupby('cylinders')['mpg'].mean().hvplot.bar(
        color='orange',
        ylabel='Rata-rata MPG',
        xlabel='Jumlah Silinder',
        title='Rata-rata MPG Berdasarkan Jumlah Silinder'
    )

# visualisasi 3: Hubungan Weight vs MPG
@pn.depends(year_slider, origin_select)
def plot_weight_mpg(year_slider, origin_select):
    data = filtered_data(year_slider, origin_select)
    return data.hvplot.scatter(
        x='weight', y='mpg', c='cylinders', cmap='viridis',
        size=80, alpha=0.6,
        title='Hubungan Weight vs MPG'
    )

# visualisasi 4: Tren Rata-rata MPG per Tahun
@pn.depends(year_slider, origin_select)
def plot_trend_mpg(year_slider, origin_select):
    data = filtered_data(year_slider, origin_select)
    trend = data.groupby('model_year')['mpg'].mean().reset_index()

    line = trend.hvplot.line(x='model_year', y='mpg', color='green', line_width=2)
    dots = trend.hvplot.scatter(x='model_year', y='mpg', color='darkgreen', size=60)
    return (line * dots).opts(title='Tren Rata-rata MPG per Tahun')

# layout dashboard
dashboard = pn.template.FastListTemplate(
    title='DASHBOARD ANALISIS AUTO MPG',
    sidebar=[
        pn.pane.Markdown("## 🔧 Filter Dashboard"),
        year_slider,
        origin_select,
        pn.pane.Markdown("Gunakan filter di atas untuk eksplorasi data berdasarkan tahun dan asal mobil."),
    ],
    main=[
        pn.Row(
            pn.Card(plot_distribution, title='Distribusi MPG'),
            pn.Card(plot_avg_mpg_cyl, title='Rata-rata MPG per Cylinders')
        ),
        pn.Row(
            pn.Card(plot_weight_mpg, title='Hubungan Weight vs MPG'),
            pn.Card(plot_trend_mpg, title='Tren Rata-rata MPG per Tahun')
        )
    ],
    accent_base_color="#004080",
    header_background="#003366"
)

# jalankan dashboard
dashboard.servable()