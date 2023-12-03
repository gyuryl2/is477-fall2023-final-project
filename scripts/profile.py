from ydata_profiling import ProfileReport
import pandas as pd
import os

if not os.path.exists('profiling'):
        os.makedirs('profiling', exist_ok=True)

df  = pd.read_csv("data/iris/iris.data")
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/report.html")

