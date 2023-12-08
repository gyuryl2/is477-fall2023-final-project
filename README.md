# is477-fall2023-final-project
A reproducible analysis based on IS 477 class materials

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10252061.svg)](https://doi.org/10.5281/zenodo.10252061)

## Overview
This repository is dedicated to the execution of a systematic and replicable analysis focused on a subset of outcomes derived from the Iris dataset. The Iris dataset encompasses comprehensive information on three distinct classes of the Iris flower. Each class is represented by 50 instances, and each instance is characterized by four essential data points extracted from actual flowers: petal length, petal width, sepal length, and sepal width. The primary objective of this analysis is to perform statistical analysis that can inform the development of a predictive model capable of discerning the Iris flower's classification based on these critical data points.

The analysis involved the computation and documentation of key summary statistics, offering a comprehensive overview of the inherent characteristics of each class. The recorded summary statistics encapsulate vital information, including the minimum and maximum values, standard deviation, first quartile, third quartile, and mean, for each of the four aforementioned data points. The minimum and maximum values provide insights into the range of variation within each class, offering a glimpse into the diversity present in the Iris flower populations. The standard deviation serves as a measure of the dispersion of data points, shedding light on the degree of variability exhibited by each class. Meanwhile, the first and third quartiles contribute to a nuanced understanding of the central tendency and distribution of the data, enhancing our ability to discern patterns within the Iris classes. Furthermore, the mean values offer a succinct representation of the central tendency of each class, serving as a crucial reference point.

The summary statistics reveal distinctive morphological characteristics within each Iris flower class—Setosa, Versicolor, and Virginica. Iris-setosa is characterized by compact dimensions, as reflected in its smaller mean sepal and petal sizes, along with relatively low variability. In contrast, Iris-versicolor exhibits larger sizes and greater variability, particularly evident in sepal and petal lengths. Iris-virginica stands out as the largest and most variable among the three classes, with larger mean sizes and increased standard deviations across all measured attributes. 

## Contributions
The collaborative efforts of Gyury Lee and Josh Sorkin are integral to this project. Joint contributions span across all sections, demonstrating a cohesive partnership in achieving the final outcomes.

## Analysis
The analysis section of the project takes into account each of the three types of Iris flowers as the results are organized by flower type. The statistics calculated include the mean, minimum, maximum, and standard deviation for the sepal length, sepal width, petal length and petal width of each flower. The information also includes the interquartile ranges for each of statistics. 

### Summary Statistics for Iris-setosa:

For sepal length, the mean is 5.006 units, with a standard deviation of 0.35249, showcasing a relatively consistent size. The petal length averages 1.464 units, demonstrating a compact size, with a standard deviation of 0.173511. Sepal width has a mean of 3.418 units and a standard deviation of 0.381024, indicating moderate variability. The petal width, with a mean of 0.244 units and a standard deviation of 0.10721, is notably smaller in comparison. These statistics reveal the distinct characteristics of Iris-setosa, emphasizing its compact size and limited variability across the measured attributes.

### Summary Statistics for Iris-versicolor:

In the case of Iris-versicolor, the summary statistics highlight a larger size and increased variability compared to Iris-setosa. With a mean sepal length of 5.936 units and a standard deviation of 0.516171, Iris-versicolor exhibits greater variation in sepal length. The mean petal length is 4.260 units, with a standard deviation of 0.469911, showcasing a larger and more varied petal size. Sepal width and petal width also display increased means (2.770 and 1.326 units, respectively) and standard deviations (0.313798 and 0.197753, respectively). These statistics underscore the larger and more diverse morphological characteristics of Iris-versicolor.

### Summary Statistics for Iris-virginica:

The summary statistics for Iris-virginica reveal a distinct set of characteristics, differentiating it from both Iris-setosa and Iris-versicolor. Iris-virginica has the largest mean sepal length (6.588 units) and petal length (5.552 units), indicating a larger overall size. The standard deviations for sepal length (0.63588) and petal length (0.551895) are comparatively higher, suggesting increased variability. Sepal width and petal width, with means of 2.974 and 2.026 units, respectively, also display larger sizes compared to the other two classes. These statistics portray Iris-virginica as the largest and most variable among the three Iris flower classes, with distinct morphological characteristics setting it apart.

## Workflow
![DAG of Iris Analysis Workflow](workflow.png)

## Reproducing

First, clone this repository

*  Create a virtual environment (.venv)

* Install the required Python packages using the command
    ```pip install -r requirements.txt```
    
* Please view the environment log for details regarding the software used.

Run the Scripts using the command: prepare_data.py using the command
```snakemake --core 1 run_all```
Output: Downloads and extracts all data for the Iris dataset from archive.ics.edu and checks the integrity of data using SHA-256 hash comparison. Reads the dataset into a dataframe and writes the profiling report to profiling/report.html. Summary statistics grouped by each of the three flowers including data on petal width, petal length, sepal width, and sepal length inside of the 'results' subdirectory.


## License

We have chosen to use the Creative Commons Attribution 4.0 (CC-BY-4.0).

The Creative Commons Attribution 4.0 (CC-BY-4.0) has the Domain Content, Data. Requires attribution and does not require share-alike.
We have chosen to implement the Creative Commons Attribution 4.0 (CC-BY-4.0) because this data license allows for the use of the datasets for any purpose as long as appropriate credit is provided. This will not limit users from applying and adapting the data in any way they choose while still ensuring that the original author of the data set is accredited.

We have chosen to use the MIT software license.

The MIT software license is a permissive free and open-source license(FOSS). This license provides anyone with the ability to use the software without any restrictions. However, the copyright notice and permission notice are required to be included in all copies or substantial portions of the software.

We decided to use the MIT license because it has very few restrictions on future users of the software. Furthermore, this license is one of the easiest to apply and administer. Despite the lack of requirements, the MIT license still ensures that the original author is accredited in future distributions of the work.

## References and Citations

Fisher,R. A.. (1988). Iris. UCI Machine Learning Repository. https://doi.org/10.24432/C56C76.
