from pprint import pprint
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px


def append_columns(df, columns_names, values):
    for column_name, value in zip(columns_names, values):
        df[column_name] = value


df = pd.read_csv("./udemy_courses_extended.csv")
is_paid = df["is_paid"]
paid = df.loc[is_paid == True]
free = df.loc[is_paid == False]

dfg = df.groupby("is_paid", as_index=False).count()
dfg = dfg[["is_paid", "course_id"]].rename(columns={"course_id": "count"})
dfg["is_paid"] = dfg["is_paid"].map({True: "Paid", False: "Free"})

new_labels = ["num_subscribers_max", "num_subscribers_min", "num_subscribers_avg"]
new_columns = [
    [
        free[["num_subscribers"]].max().max(),
        paid[["num_subscribers"]].max().max(),
    ],
    [
        free[["num_subscribers"]].min().min(),
        paid[["num_subscribers"]].min().min(),
    ],
    [
        free[["num_subscribers"]].mean().mean(),
        paid[["num_subscribers"]].mean().mean(),
    ],
]
append_columns(
    dfg,
    new_labels,
    new_columns,
)

PIES = [
    [
        go.Pie(
            labels=dfg["is_paid"],
            values=dfg["num_subscribers_min"],
            name="Sub Min",
            title="Subscribers Minimal",
            textinfo="value+label",
        ),
        go.Pie(
            labels=dfg["is_paid"],
            values=dfg["num_subscribers_avg"],
            name="Sub Avg",
            title="Subscribers Average",
            textinfo="value+label",
        ),
    ],
    [
        go.Pie(
            labels=dfg["is_paid"],
            values=dfg["num_subscribers_max"],
            name="Sub Max",
            title="Subscribers Max",
            textinfo="value+label",
        ),
        go.Pie(
            labels=dfg["is_paid"],
            values=dfg["count"],
            name="Paid to free ratio",
            title="Paid to free ratio",
            textinfo="percent+label",
        ),
    ],
    [
        go.Pie(
            labels=free["level"],
            values=free["num_subscribers"],
            name="Course lvls Free",
            title="Course levels Free",
            textinfo="value+label",
        ),
        go.Pie(
            labels=paid["level"],
            values=paid["num_subscribers"],
            name="Course lvls Paid",
            title="Course levels Paid",
            textinfo="value+label",
        ),
    ],
]

fig = make_subplots(
    rows=2,
    cols=3,
    specs=[[{"type": "domain"} for _ in range(3)] for _ in range(2)],
)
for idx, col in enumerate(PIES):
    for jdx, pie in enumerate(col):
        fig.add_trace(pie, jdx + 1, idx + 1)

fig.update_traces(
    hole=0.4,
    hoverinfo="label+percent+name+value",
    textposition="inside",
    textfont_size=15,
)
fig.update_layout(
    showlegend=True,
)
fig.show()
