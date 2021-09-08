## rosbag_to_csv

# Description
Convert a rosbag to csv and a visualization example using the Plotly library in Jupyter Notebook

# Rosbag to CSV
To convert a rosbag to a CSV file:
- Clone the [rosbag_pandas](https://github.com/eurogroep/rosbag_pandas)
- Run `bag_to_csv -b ~/path_to_rosbag_input.bag -o ~/path_to_csv_output.csv`

# CSV refactoring for 2D & 3D Openpose data
This section pertains to csvs containing Openpose 2D & 3D data produced using the [openpose_3D_localization](https://github.com/Roboskel-Manipulation/openpose_3D_localization) repo. 
- `csv_refactor_2d.py` and `csv_refactor_3d.py`: Convert the csv produced by the [rosbag_pandas](https://github.com/eurogroep/rosbag_pandas) package and produce another csv in a more readable and self-explainable form.
- Arguments: The input csv 

# Visualization
This example shows how to visualize data from a CSV created with the aforementioned procedure using the `plotly` library

To run the vizualization example:
- In a terminal navigate to this repo
- Run `jupyter notebook plot.ipynb`
