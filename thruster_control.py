#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

class ThrusterControlNode:
    def __init__(self):
        rospy.init_node('thruster_control_node')

        # Define the joint publishers for left and right thrusters
        self.left_thruster_pub = rospy.Publisher('/left_propellers_joint/command', Float64, queue_size=1)
        self.right_thruster_pub = rospy.Publisher('/right_propellers_joint/command', Float64, queue_size=1)

    def run(self):
        # Set a non-zero torque command to make the propellers spin
        left_torque = 10.0  # Adjust this value to control the left propeller's torque
        right_torque = 10.0  # Adjust this value to control the right propeller's torque

        rospy.loginfo(f"Publishing left_torque: {left_torque}, right_torque: {right_torque}")

        # Publish the torque commands to the joint positions
        while not rospy.is_shutdown():
            self.left_thruster_pub.publish(left_torque)
            self.right_thruster_pub.publish(right_torque)
            rospy.sleep(0.1)  # Adjust the sleep duration to control the update rate

if __name__ == '__main__':
    try:
        thruster_control_node = ThrusterControlNode()
        thruster_control_node.run()
    except rospy.ROSInterruptException:
        pass

