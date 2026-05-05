# simulator.py
import itertools
import data_config as data
import elo_engine as calc

# Grabbing combinations based on the quotas we defined in data_config
pool_a = list(itertools.combinations(data.POOLS["Pool_A"], data.TOURNAMENT_QUOTAS["Pool_A"]))
pool_b = list(itertools.combinations(data.POOLS["Pool_B"], data.TOURNAMENT_QUOTAS["Pool_B"]))
pool_c = list(itertools.combinations(data.POOLS["Pool_C"], data.TOURNAMENT_QUOTAS["Pool_C"]))
pool_d = list(itertools.combinations(data.POOLS["Pool_D"], data.TOURNAMENT_QUOTAS["Pool_D"]))

# Cartesian product to simulate every possible tournament bracket
# Warning: This generates millions of combinations, takes a few seconds to run
all_tournaments = list(itertools.product(pool_a, pool_b, pool_c, pool_d))


all_calculations = []
TARGET_ELO_GAIN = 4.0 

for tournament in all_tournaments:
    # itertools.product returns a messy nested tuple like ((dict, dict), (dict, dict))
    # We need to flatten this mess into a simple list of elo numbers
    opponent_elos = [player["elo"] for pool in tournament for player in pool]
    
    expected_score = calc.calculate_tournament_expected_score(data.SUBJECT_PLAYER["elo"], opponent_elos)
    required_score = calc.calculate_required_score(TARGET_ELO_GAIN, expected_score)
    
    all_calculations.append(required_score)


print(f"Done! Simulated {len(all_calculations)} tournaments.")
