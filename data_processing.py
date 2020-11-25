import pandas as pd


def load_df(add_death_df, add_confirmed_df, add_recovered_df, add_summary_df):
    # TO DO: Lire les bases de données à partir des liens URL reçus en paramètres
    confirmed_df = pd.read_csv(add_confirmed_df, sep=",", delimiter=None, header=0)
    recovered_df = pd.read_csv(add_recovered_df, sep=",", delimiter=None, header=0)
    summary_df = pd.read_csv(add_summary_df, sep=",", delimiter=None, header=0)
    death_df = pd.read_csv(add_death_df, sep=",", delimiter=None, header=0)

    print(death_df.iloc[:, -9:])
    print(recovered_df.iloc[:, -9:])
    print(confirmed_df.iloc[:, -9:])
    print(summary_df.iloc[:, -9:])

    return death_df, confirmed_df, recovered_df, summary_df


def summary_add_col(df, col, value):
    # TO DO: Ajouter une colonne à la base de données df reçue en paramètre (deux lignes)
    # le nom et la valeur de cette colonne se trouvent respectivement dans les variables col et value.
    df[col] = value
    return df


def summary_extract_col(df, cols):
    # TO DO: Extraire les colonnes reçues en paramètre désirer de la base de données df (une seul ligne)
    return df.drop(labels=cols, axis=1)


def summary_by_country(df):
    # TO DO: Grouper le DataFrame par Country_Region (une seule ligne). Utiliser la méthode groupby()
    return df.groupby(by="Country_Region", axis=1)


def creat_dict_df(death_df, confirmed_df, recovered_df):
    # TODO: Créer un dictionnaire avec des bases de données reçues en paramètre (une seule ligne)
    return {"death_df": death_df, "confirmed_df": confirmed_df, "recovered_df": recovered_df}


def dict_remove_col(dict_df, cols):
    # TO DO: Supprimer des colonnes cols du dictionnaire dict_df (une seule ligne) 
    # les colonnes doivent être supprimées de l’ensemble des clés du dictionnaire
    return dict_df.pop(cols)


def dict_by_country(dict_df):
    # TO DO: Grouper le dictionnaire dict_df par Country/Region pour toutes les clés du dictionnaire 
    # et changer les colonnes en datetime, utiliser le lien suivant pour plus d'information
    # https://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.to_datetime.html    
    nouv_dict = {}
    for key in dict_df:
        nouv_dict[key] = dict_df[key].groupby("Country/Region").mean()
        nouv_dict[key].columns = pd.to_datetime(nouv_dict[key].columns)

    return nouv_dict


def dict_add_key(dict_df):
    # TO DO: Ajouter les clés Active case et Closed Case a votre dictionnaire de DataFrame
    # les cles du dictionnaire doivent être triés comme suit:{"Confirmed", "Deaths", "Active", "Closed", "Recovered"}
    dict_tempo = dict_df["Recovered"]
    dict_df.pop("Recovered")
    dict_df["Active"] = dict_df["Confirmed"]-dict_tempo-dict_df["Deaths"]
    dict_df["Closed"] = dict_tempo+dict_df["Deaths"]
    dict_df["Recovered"] = dict_tempo
    return dict_df


def dict_by_day(dict_df):
    # TO DO: Grouper le dictionnaire de DataFrame par date (une seule ligne)
    # Utiliser le lien suivant: 
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html
    return dict_df.transpose()


def basic_inf_summary(summary_df):
    # TO DO: Afficher les informations suivantes: Somme des nombres de cas confirmé,
    # active, fermée, mort et rétabli dans le monde.
    # colonne 5, 8, 7, 6, 9
    somme_confirmed = 0
    somme_active = 0
    somme_fermee = 0
    somme_mort = 0
    somme_retabli = 0
    for indice, ligne in enumerate(summary_df):
        if indice == 0:
            continue
        else:
            somme_confirmed += ligne[5]
            somme_active += ligne[8]
            somme_fermee += ligne[9]
            somme_mort += ligne[6]
            somme_retabli += ligne[7]
    sommes = [somme_confirmed, somme_active, somme_fermee, somme_mort, somme_retabli]
    for elem in sommes:
        print(elem)
    return sommes
