# elo_engine.py
import math

def calculate_expected_match_score(carlsen_elo, opponent_elo):
    # FIDE formula expects (Opponent - Player). I initially reversed this and it broke the math!
    elo_diff = opponent_elo - carlsen_elo
    
    # FIDE 400-point rule. Gotta cap the difference to prevent weird probability spikes
    if elo_diff > 400:
        elo_diff = 400
    elif elo_diff < -400:
        elo_diff = -400
        
    return 1.0 / (1.0 + math.pow(10, elo_diff / 400.0))

def calculate_tournament_expected_score(carlsen_elo, opponent_elos_list):
    # Just summing up all expected match scores for the whole tournament
    return sum(calculate_expected_match_score(carlsen_elo, opp) for opp in opponent_elos_list)

def calculate_required_score(target_elo_change, expected_performance):
    # Derived from: Delta = K * (Actual - Expected). Solving for Actual here.
    # K is 10 for Super GMs like Carlsen
    return (target_elo_change / 10.0) + expected_performance