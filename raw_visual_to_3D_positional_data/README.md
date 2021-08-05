# raw_visual_to_3D_positional_data

In a __new terminal__ launch [pipeline_launch](https://github.com/Roboskel-Manipulation/openpose_3D_localization/tree/main/pipeline_launch):

        roslaunch pipeline_launch pipeline_launch.launch sim:=true live_camera:=false

In a __new terminal__ launch [bag_read_server](https://github.com/ThanasisTs/bag_read_service):
        
        roslaunch bag_read_service bag_read_service.launch bag_file:="filename"

To record the transformed keypoints, in a __new terminal__ run:

        rosbag record -O ~/keypoints_tf.bag /transform_topic

To read the first message from the rosbag file and start the pipeline, in a __new terminal__ run:

        rosservice call /next_msg


# From rosbag to .csv

If you want to convert a rosbag to a CSV file, check [these instructions](https://github.com/ThanasisTs/instructions/tree/master/rosbag_to_csv)

