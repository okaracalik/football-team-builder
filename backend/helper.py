from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pulp
import pandas as pd
import numpy as np

def init_mysql_engine(user, pwd, host, port, db):
  return create_engine(f'mysql+mysqlconnector://{user}:{pwd}@{host}:{port}/{db}')


def get_database_session(engine):
  Session = sessionmaker(bind=engine)
  return Session()


def compute_best_lineup(df, formation, budget):

    # problem definition
    prob = pulp.LpProblem('BestLineup', pulp.LpMaximize)

    # get unique identifiers
    ids = df['id'].tolist()

    # parameters
    overalls = pd.Series(df['overall'].values, index=ids).to_dict()
    values = pd.Series(df['value'].values, index=ids).to_dict()

    ## dynamic paramters: selected positions
    ### convert position-strings into binary variables
    for pos in formation:
        df[f'is_{pos}'] = np.where(df['position'] == pos, 1, 0)

    ### extract positional parameters
    positions = {}
    for pos in formation:
        positions[pos] = pd.Series(df[f'is_{pos}'].values, index=ids).to_dict()

    # define the decision variable
    players = pulp.LpVariable.dicts("Player", ids, cat='Binary')

    # set objective
    prob += pulp.lpSum([overalls[i] * players[i] for i in ids]), "Total Rating of Lineup"

    # set constraints
    prob += pulp.lpSum([players[i] for i in ids]) == 11, "Pick_11_Players"
    prob += pulp.lpSum([values[i] * players[i] for i in ids]) <= budget, "Total_Value_Under_Budget"
    ## check if required position is picked
    for pos in formation:
        prob += pulp.lpSum([positions[pos][i] * players[i] for i in ids]) == 1, f"Pick_{pos.upper()}"

    result = prob.solve()

    picked_player_ids = [int(i.name.split('_')[1]) for i in prob.variables() if i.varValue > 0]

    return prob, picked_player_ids
