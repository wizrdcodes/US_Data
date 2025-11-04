import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


monthly_US_inflation_data = pd.read_csv('../data/US_inflation_rates.python.csv')

monthly_US_inflation_data["date"] = pd.to_datetime(monthly_US_inflation_data["date"]) #Convert 'date' column to datetime format
monthly_US_inflation_data["year"] = pd.to_datetime(monthly_US_inflation_data["date"]).dt.year #Extract the year from the 'date' column
annual_cpi = monthly_US_inflation_data.groupby("year")["value"].agg(start_CPI="first", end_CPI="last") #Group by year to condense data
annual_cpi["inflation_rate"] = ((annual_cpi["end_CPI"] - annual_cpi["start_CPI"]) / annual_cpi["start_CPI"]) * 100 #Compute annual inflation rate

annual_cpi = annual_cpi.reset_index()

infl_since_1976 = annual_cpi[annual_cpi["year"] >= 1976]

# plt.text(monthly_US_inflation_data.iloc[0]["date"],
#          monthly_US_inflation_data.iloc[0]["value"],
#          "Start of Data")
# plt.text(monthly_US_inflation_data.iloc[-1]["date"],
#          monthly_US_inflation_data.iloc[-1]["value"],
#          "End of Data")

presidents_data = pd.read_csv('../data/presidents.python.csv')

presidents_data["Term"] = presidents_data["Term"].astype(str).str.strip()

def expand_term(row):
    term = row["Term"].strip()
    if "-" not in term:
        return pd.DataFrame()
    try:
        years = term.split("-")
        start_year = int(years[0].strip())

        if len(years) < 2 or not years[1].strip():
            end_year = start_year + 4
        else:
            end_year = int(years[1].strip())

        expanded_df = pd.DataFrame({"year": list(range(start_year, end_year + 1))})

        for col in row.x:
            if col != "Term":
                expanded_df[col] = row[col]

        transition_years = {1981, 1989, 1993, 2001, 2009, 2017, 2021, 2025}
        expanded_df = expanded_df[~((expanded_df["year"].isin(transition_years)) & (expanded_df["year"] == end_year))]

        return expanded_df

    except ValueError:
        return pd.DataFrame()

expanded_presidents = pd.concat([expand_term(row) for _, row in presidents_data.iterrows()], ignore_index=True)

expanded_presidents = expanded_presidents.drop_duplicates(subset=["year"], keep="last")

pres_since_1976 = expanded_presidents[expanded_presidents["year"] >= 1976]

infl_by_pres_since_1976 = pres_since_1976.merge(infl_since_1976, on="year", how="left")

known_party_mapping = {
    1976: "Democrat", 1977: "Democrat", 1978: "Democrat", 1979: "Democrat", 1980: "Democrat",
    1981: "Republican", 1982: "Republican", 1983: "Republican", 1984: "Republican",
    1985: "Republican", 1986: "Republican", 1987: "Republican", 1988: "Republican",
    1989: "Republican", 1990: "Republican", 1991: "Republican", 1992: "Republican",
    1993: "Democrat", 1994: "Democrat", 1995: "Democrat", 1996: "Democrat",
    1997: "Democrat", 1998: "Democrat", 1999: "Democrat", 2000: "Democrat",
    2001: "Republican", 2002: "Republican", 2003: "Republican", 2004: "Republican",
    2005: "Republican", 2006: "Republican", 2007: "Republican", 2008: "Republican",
    2009: "Democrat", 2010: "Democrat", 2011: "Democrat", 2012: "Democrat",
    2013: "Democrat", 2014: "Democrat", 2015: "Democrat", 2016: "Democrat",
    2017: "Republican", 2018: "Republican", 2019: "Republican", 2020: "Republican",
    2021: "Democrat", 2022: "Democrat", 2023: "Democrat", 2024: "Democrat",
    2025: "Republican"
}

infl_by_pres_since_1976["Party"] = infl_by_pres_since_1976["year"].map(known_party_mapping).fillna(infl_by_pres_since_1976["Party"])

party_colors = {"Republican": "r", "Democrat": "b"}
infl_by_pres_since_1976["color"] = infl_by_pres_since_1976["Party"].map(party_colors)

infl_by_pres_since_1976["color"] = infl_by_pres_since_1976["color"].fillna("gray")

def plot_inflation_rate_by_president():
    plt.figure(figsize=(14, 6))
    plt.scatter(infl_by_pres_since_1976["year"], infl_by_pres_since_1976["inflation_rate"], c=infl_by_pres_since_1976["color"], s=10, alpha=0.8)
    plt.xlabel("Year")
    plt.ylabel("Inflation Rate (%)")

    plt.text(infl_by_pres_since_1976.iloc[-9]["year"], infl_by_pres_since_1976.iloc[-9]["inflation_rate"], infl_by_pres_since_1976.iloc[-9]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-13]["year"], infl_by_pres_since_1976.iloc[-13]["inflation_rate"], infl_by_pres_since_1976.iloc[-13]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-21]["year"], infl_by_pres_since_1976.iloc[-21]["inflation_rate"], infl_by_pres_since_1976.iloc[-21]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-29]["year"], infl_by_pres_since_1976.iloc[-29]["inflation_rate"], infl_by_pres_since_1976.iloc[-29]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-37]["year"], infl_by_pres_since_1976.iloc[-37]["inflation_rate"], infl_by_pres_since_1976.iloc[-37]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-41]["year"], infl_by_pres_since_1976.iloc[-41]["inflation_rate"], infl_by_pres_since_1976.iloc[-41]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-49]["year"], infl_by_pres_since_1976.iloc[-49]["inflation_rate"], infl_by_pres_since_1976.iloc[-49]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-53]["year"], infl_by_pres_since_1976.iloc[-53]["inflation_rate"], infl_by_pres_since_1976.iloc[-53]["Name"].split()[-1])
    plt.text(infl_by_pres_since_1976.iloc[-54]["year"], infl_by_pres_since_1976.iloc[-54]["inflation_rate"], infl_by_pres_since_1976.iloc[-54]["Name"].split()[-1])

    # for k, row in infl_by_pres_since_1976.iterrows():
    #     plt.text(row["year"], row["inflation_rate"], row["Name"],
    #              fontsize=5, fontweight="bold")

    plt.title("US inflation Rate Since 1976 (Colored by President's Party)")
    plt.show()

plot_inflation_rate_by_president()


# monthly_US_unemployment_data = pd.read_csv('Unemployment_series_statewise_USA.1.csv')

