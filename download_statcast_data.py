import pandas as pd
import os
from pybaseball import pitching_stats
from pybaseball import batting_stats
from pybaseball import team_pitching
from pybaseball import team_batting

def download_statcastdata(start_date, end_date, min_innings, min_abs):
    """
    Downloads statcast data for both battings and pitching for a given date range.
    """

    """
    Start of pitching data
    """
    pitch_data = pitching_stats(start_date, end_date, qual = min_innings)

    df = pd.DataFrame(pitch_data)

    pitch_file = "pitching_stats_" + str(start_date) + "_" + str(end_date) + ".csv"

    df.to_csv(pitch_file, index=False)
   
    print(f"data exported to {pitch_file}")

    """
    Start of batting data
    """
    bat_data = batting_stats(start_date, end_date, qual = min_abs)

    df = pd.DataFrame(bat_data)

    bat_file = "batting_stats_" + str(start_date) + "_" + str(end_date) + ".csv"

    df.to_csv(bat_file, index=False)

    print(f"data exported to {bat_file}")

    """
    Start of Team Pitching data
    """
    team_pitch_data = team_pitching(start_date, end_date)

    df = pd.DataFrame(team_pitch_data)

    team_pitch_file = "team_pithing_stats_" + str(start_date) + "_" + str(end_date) + ".csv"

    df.to_csv(team_pitch_file, index=False)

    print(f"data exported to {team_pitch_file}")
    
    """
    Start of Team batting data
    """
    team_bat_data = team_batting(start_date, end_date)

    df = pd.DataFrame(team_bat_data)

    team_bat_file = "team_batting_stats_" + str(start_date) + "_" + str(end_date) + ".csv"

    df.to_csv(team_bat_file, index=False)

    print(f"data exported to {team_bat_file}")  


if __name__ == "__main__":
    start_date = "2024"  #change for start year
    end_date = "2024"  #change for end year
    min_innings = 50
    min_abs = 200

    download_statcastdata(start_date, end_date, min_innings, min_abs)