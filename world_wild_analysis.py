import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

def summary_analyse_data(df):
    # TO DO: plot the 10 countries with the highest number of confirmed, deaths, active, closed, recovered,
    # and mortality rate
    # Étape 1: Créer des subfigure de 3 lignes et 2 colonnes de dimension 15*15 en utilisant la bibliothèque matplotlib
    # https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html
    dimensions = 15
    fig, axes = plt.subplots(3, 2)
    axes[0, 0].set_title("Top 10 countries as per number of Confirmed cases")
    axes[0, 1].set_title("Top 10 countries as per number of Deaths cases")
    axes[1, 0].set_title("Top 10 countries as per number of Active cases")
    axes[1, 1].set_title("Top 10 countries as per number of Closed cases")
    axes[2, 0].set_title("Top 10 countries as per number of Recovered cases")
    axes[2, 1].set_title("Top 10 countries as per number of Mortality rate")
    # Étape 2:  dessiner sur chaque subplot les 10 pays les plus toucher par la Covid_19 selon le nombre de cas confirmés,
    # mort, actif, fermé et rétabli ainsi que le taux de mortalité en utilisant la bibliothèque seaborn.
    # https://seaborn.pydata.org/generated/seaborn.barplot.html
    confirmed = [df.sort_values("Confirmed"), df.sort_values("Confirmed")["Country"]]
    deaths = [df.sort_values("Deaths"), df.sort_values("Deaths")["Country"]]
    active = [df.sort_values("Active"), df.sort_values("Active")["Country"]]
    closed = [df.sort_values("Closed"), df.sort_values("Closed")["Country"]]
    recovered = [df.sort_values("Recovered"), df.sort_values("Recovered")["Country"]]
    mortality = [df.sort_values("Mortality"), df.sort_values("Mortality")["Country"]]

    del confirmed[11:]
    del deaths[11:]
    del active[11:]
    del closed[11:]
    del recovered[11:]
    del mortality[11:]
# on enlève le nom des axes
    del confirmed[0]
    del deaths[0]
    del active[0]
    del closed[0]
    del recovered[0]
    del mortality[0]

    axes[0, 0].plot(confirmed[1], confirmed[0])
    axes[0, 1].plot(deaths[1], deaths[0])
    axes[1, 0].plot(active[1], active[0])
    axes[1, 1].plot(closed[1], closed[0])
    axes[2, 0].plot(recovered[1], recovered[0])
    axes[2, 1].plot(mortality[1], mortality[0])

    liste_de_titres = ["Confirmed", "Deaths", "Active", "Closed", "Recovered", "Mortality"]
    for index, axe in enumerate(axes.flat):
        axe.set(xlabel=str("Number of "+liste_de_titres[index]+" cases"), ylabel="Country_Region")

    fig.tight_layout(pad=3.0)
    fig.show()
    plt.savefig('Image/fig_01.png', dpi=600, format='png')


def summary_secteur(df):
    # TO DO: Plot le pourcentage mondial des cas confirmés par pays
    # Étape 1: Créer une base de données avec les pays qui ont un pourcentage de cas confirmé 
    # supérieur ou égale à 2% des nombres de cas confirmé dans le monde.
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
    donnees = df["Confirmed"]
    somme = 0
    for data in donnees:
        somme += data

    nouv_df = [df["Country"], df["Confirmed"]]
    dict_de_pays = {}
    other = [[], []]
    for index, elem in enumerate(nouv_df[1]):
        if round((elem/somme)*100) >= 2:
            dict_de_pays[nouv_df[index]] = 100 * elem/somme
    # Étape 2: Créer une base de données avec les pays qui ont un pourcentage de cas confirmé 
    # inférieur à 2% des nombres de cas confirmé dans le monde. 
    # Cette base de données doit contenir une seule ligne représentant la somme de tous les cas
    # dans les pays ayant un pourcentage de cas confirmé inférieur à 2% dont le nom sera "Others"
    # https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/
        else:
            other[0].append(nouv_df[0][index])
            other[1].append(elem)
    somme2 = (sum(other[1])/somme) * 100
    pays = pd.DataFrame(dict_de_pays, index=["Pourcentage"])
    others = pd.DataFrame({"Others": somme2}, index=["Pourcentage"])

    # Étape 3: Concaténer les deux bases de données créées précédemment
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
    frames = [pays, others]
    database = pd.concat(frames)
    # Étape 4: Dessiner le pourcentage mondial des cas confirmés par pays en utilisant la bibliothèque plotly.express
    # https://plotly.com/python/pie-charts/

    fig = px.pie(database, values="Pourcentage", tips="Countries")

    fig.update_traces(textposition="inside")
    fig.show()
    pio.write_image(fig, 'Image/fig_02.png', width=1000, height=500)

def countries_bar(df, countries):
    # TO DO: plot pour certains pays le nombre de cas confirmés, morts, actifs, fermés et rétablis
    # Étape 1: soustraire les données des pays reçus en paramètre
    new_df = df[countries]
    # Étape 2: TO DO: Retirer la colonne "Mortality_Rate"
    new_df.drop(columns=["Mortality_Rate"])
    # Étape 3: Créer une figure en utilisant la bibliothèque plotly.graph_objects
    # https://plotly.com/python/subplots/

    fig = make_subplots(rows=1, cols=2, shared_yaxes=True)

    fig.add_trace(go.Bar(x=new_df("Countries"), y=new_df.columns[0:]))

    fig.update_layout(yaxis=dict(title='Cases', titlefont_size=16, tickfont_size=14), xaxis_tickfont_size=14,
                      barmode='group', bargap=0.15, bargroupgap=0.1, legend=dict(x=0.01, y=0.99),
                      legend_orientation="h")
    fig.show()
    pio.write_image(fig, 'Image/fig_03.png', width=1000, height=500)
    
