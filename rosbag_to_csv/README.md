## rosbag_to_csv

# Description
Convert a rosbag to csv and a visualization example using the Plotly library in Jupyter Notebook

# Rosbag to CSV
To convert a rosbag to a .csv:
- Clone the [rosbag_pandas](https://github.com/eurogroep/rosbag_pandas)
- Navigate to ~/path_to_catkin_ws/src/rosbag_pandas/scripts
- Run `python bag_to_csv -b ~/path_to_rosbag_input.bag -o ~/path_to_csv_output.csv`

# Visualization
To run the vizualization example:
- In a terminal navigate to this repo
- Run `jupyter notebook plot.ipynb`
