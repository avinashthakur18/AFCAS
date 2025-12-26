import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr

# Load data
df = pd.read_csv("fee_data.csv")

#  Show dataset
def show_data():
    return df

# Paid vs Pending chart
def fee_status_chart():
    status_count = df["Status"].value_counts()
    plt.figure()
    status_count.plot(kind="bar")
    plt.title("Paid vs Pending Fees")
    plt.xlabel("Status")
    plt.ylabel("Number of Students")
    return plt

# Monthly collection chart
def monthly_collection_chart():
    monthly = df[df["Status"]=="Paid"].groupby("Month")["Fee_Amount"].sum()
    plt.figure()
    monthly.plot(kind="bar")
    plt.title("Monthly Fee Collection")
    plt.xlabel("Month")
    plt.ylabel("Total Fee Collected")
    return plt

#  Summary
def summary():
    paid = len(df[df["Status"]=="Paid"])
    pending = len(df[df["Status"]=="Pending"])
    total = df[df["Status"]=="Paid"]["Fee_Amount"].sum()
    return f"""
Total Students : {len(df)}
Fees Paid      : {paid}
Fees Pending   : {pending}
Total Collected: ₹ {total}
"""

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("# 🎓 Student Fee Collection Analysis System")
    gr.Markdown("### Minor Project using Pandas + Gradio")

    btn1 = gr.Button("📋 Show Fee Data")
    out1 = gr.Dataframe()
    btn1.click(show_data, outputs=out1)

    btn2 = gr.Button("📊 Paid vs Pending Chart")
    out2 = gr.Plot()
    btn2.click(fee_status_chart, outputs=out2)

    btn3 = gr.Button("📈 Monthly Collection Chart")
    out3 = gr.Plot()
    btn3.click(monthly_collection_chart, outputs=out3)

    btn4 = gr.Button("🧮 Show Summary")
    out4 = gr.Textbox(lines=6)
    btn4.click(summary, outputs=out4)

app.launch()
