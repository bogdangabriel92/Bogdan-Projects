import pandas as pd

subs = pd.read_csv("data_raw/subscriptions.csv", parse_dates=["period_start","period_end"])
usage = pd.read_csv("data_raw/usage.csv", parse_dates=["date"])
tickets = pd.read_csv("data_raw/tickets.csv", parse_dates=["opened_at","closed_at"])

# churn label pe client lunar (0/1)
active = (subs[subs["is_active"]]
          .assign(month=subs["period_start"].dt.to_period("M"))
          .groupby(["customer_id","month"]).size().reset_index(name="active"))
active["active"] = 1

# usage lunar per client
u = (usage.assign(month=usage["date"].dt.to_period("M"))
          .groupby(["customer_id","month"])
          .agg(events=("events","sum"),
               minutes=("minutes_used","sum"),
               featX=("feature_X_used","sum"))
          .reset_index())

# tickets lunar (volum + durată)
t = (tickets.assign(month=tickets["opened_at"].dt.to_period("M"),
                    duration_hours=(tickets["closed_at"]-tickets["opened_at"])
                                    .dt.total_seconds()/3600)
            .groupby(["customer_id","month"])
            .agg(tickets=("ticket_id","nunique"),
                 avg_close_h=("duration_hours","mean"))
            .reset_index())

# dataset analitic
df = (active.merge(u, on=["customer_id","month"], how="left")
            .merge(t, on=["customer_id","month"], how="left")
            .fillna({"events":0,"minutes":0,"featX":0,"tickets":0,"avg_close_h":0}))

# churn în t+1 (etichetă pentru model/analiză descriptivă)
df["month_next"] = df["month"] + 1
next_active = active[["customer_id","month"]].rename(columns={"month":"month_next"})
df = df.merge(next_active.assign(active_next=1),
              on=["customer_id","month_next"], how="left")
df["churn"] = (df["active_next"].isna()).astype(int)
