import pandas as pd

orders = pd.read_csv("data_raw/orders.csv", parse_dates=["order_date"])
customers = pd.read_csv("data_raw/customers.csv", parse_dates=["signup_date"])
order_items = pd.read_csv("data_raw/order_items.csv")
products = pd.read_csv("data_raw/products.csv")

# AOV zilnic
aov_daily = (orders
             .assign(day=orders["order_date"].dt.date)
             .groupby("day")
             .agg(orders=("order_id","nunique"),
                  revenue=("revenue","sum"),
                  aov=("revenue","mean"))
             .reset_index())

# Cohorts (vectorizat)
first_order = (orders.groupby("customer_id")["order_date"].min()
               .dt.to_period("M").rename("cohort"))
orders["order_month"] = orders["order_date"].dt.to_period("M")
orders = orders.join(first_order, on="customer_id")
orders["cohort_index"] = (orders["order_month"] - orders["cohort"]).apply(lambda x: x.n)
cohort_pivot = (orders.groupby(["cohort","cohort_index"])["customer_id"]
                .nunique().unstack(fill_value=0))
