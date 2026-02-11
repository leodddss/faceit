import elo

class PeekitMatchService:
    _elo_system = elo.Elo(k_factor=32)

    @staticmethod
    def get_rank_level(elo_points: int) -> int:
        match elo_points:
            case p if p <= 500: return 1
            case p if p <= 750: return 2
            case p if p <= 1000: return 3
            case p if p <= 1250: return 4
            case p if p <= 1500: return 5
            case p if p <= 1750: return 6
            case p if p <= 2000: return 7
            case p if p <= 2300: return 8
            case p if p <= 2600: return 9
            case _: return 10

    @classmethod
    def calculate_team_match(cls, team_ct_elo: list[int], team_t_elo: list[int], winner: str):
        avg_ct = sum(team_ct_elo) / len(team_ct_elo)
        avg_t = sum(team_t_elo) / len(team_t_elo)

        match winner:
            case "CT":
                new_ct, new_t = cls._elo_system.rate_5vs5(avg_ct, avg_t)
            case "T":
                new_t, new_ct = cls._elo_system.rate_5vs5(avg_t, avg_ct)
            case _:
                return None

        return round(new_ct - avg_ct), round(new_t - avg_t)

if __name__ == "__main__":
    ct_team = [1000, 1050, 980, 1020, 1100]
    t_team = [1000, 950, 1010, 990, 1050]

    service = PeekitMatchService()
    
    ct_change, t_change = service.calculate_team_match(ct_team, t_team, "CT")
    
    print(f"CT Change: {ct_change:+}")
    print(f"T Change: {t_change:+}")
    print(f"Rank for 1450 Elo: {service.get_rank_level(1450)}")
