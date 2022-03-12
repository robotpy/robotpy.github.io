#!/usr/bin/env python3

import frontmatter
import os
import tbapy
import sys
import yaml


def update_year(tba, year, data):
    year = int(year)
    teams = data[year]
    for team, teamdata in list(teams.items()):
        updated = False
        if teamdata is None:
            teamdata = {}
        try:
            awards = tba.team_awards(int(team), year)
        except Exception as e:
            print(e, file=sys.stderr)
            continue

        for award in awards:
            updated = True
            event = tba.event(award["event_key"])
            teamdata.setdefault("awards", []).append(
                f'{event["name"]}: {award["name"]}'
            )

        if updated:
            teams[team] = teamdata


def main():
    if len(sys.argv) == 1:
        print("Usage: get_awards.py [year|all]")
        return

    year = sys.argv[1]
    data = frontmatter.load("community.md")["teamlist"]
    tba = tbapy.TBA(os.environ["TBA_KEY"])

    if year == "all":
        for year in data:
            update_year(tba, year, data)
    else:
        update_year(tba, year, data)

    print(yaml.dump(data, sort_keys=False))


if __name__ == "__main__":
    main()
