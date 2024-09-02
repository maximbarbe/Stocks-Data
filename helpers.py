import csv
import pathlib
from typing import List


def get_tickers():
    if not pathlib.Path("./tickers.txt"):
        with open ('nasdaq_screener_1724091433683.csv', mode="r") as csvfile, open("tickers.txt", mode='a') as file:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i != 0:
                    file.write(row.rstrip())
    return
    

def remove_failed_tickers(tickers:List[str], failed:dict):
    with open("tickers.txt", mode="w") as f:
        f.write("")
    with open('tickers.txt', mode="a") as file:
        for ticker in tickers:
            if failed.get(ticker, None) == None:
                file.write(f"{ticker}\n")
    return


