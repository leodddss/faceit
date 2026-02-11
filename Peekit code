import elo

peekit_elo = elo.Elo(k_factor=32)

def calculate_new_ranks(winner_elo, loser_elo):
    new_winner_elo, new_loser_elo = peekit_elo.rate_1vs1(winner_elo, loser_elo)
    return round(new_winner_elo), round(new_loser_elo)

def get_rank_level(elo_points):
    if elo_points <= 500: return 1
    if elo_points <= 750: return 2
    if elo_points <= 1000: return 3
    if elo_points <= 1250: return 4
    if elo_points <= 1500: return 5
    if elo_points <= 1750: return 6
    if elo_points <= 2000: return 7
    if elo_points <= 2300: return 8
    if elo_points <= 2600: return 9
    return 10

if __name__ == "__main__":
    p1, p2 = 1000, 1000
    new_p1, new_p2 = calculate_new_ranks(p1, p2)
    print(new_p1, new_p2)
    print(get_rank_level(new_p1))
