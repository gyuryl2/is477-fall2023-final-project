# Rule for preparing data
rule prepare:
    output:
        "data/iris/bezdekIris.data",
        "data/iris/Index",
        "data/iris/iris.data",
        "data/iris/iris.names"
    shell:
        "python scripts/prepare_data.py"

# Rule for profiling data
rule profile:
    output:
        "profiling/report.html"
    shell:
        "python scripts/profile.py"

# Rule for analyzing data
rule analyze:
    output:
        "results/Iris-setosa_summary.txt",
        "results/Iris-versicolor_summary.txt",
        "results/Iris-virginica_summary.txt"
    shell:
        "python scripts/analysis.py"
