#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

class ThrusterControlNode:
    def __init__(self):
        rospy.init_node('thruster_control_node')

        # Define the joint publishers for left and right thrusters
        self.thruster_pub = rospy.Publisher('/adhesion_propeller_joint/command', Float64, queue_size=1)

    def run(self):
        # Set a desired angular velocity for the propeller (in radians per second)
        angular_velocity = 200.0  # Adjust this value to control the left propeller's angular velocity

        rospy.loginfo(f"Publishing angular_velocity: {angular_velocity}")

        # Publish the angular velocity commands to the joint positions
        while not rospy.is_shutdown():
            self.thruster_pub.publish(angular_velocity)
            rospy.sleep(0.1)  # Adjust the sleep duration to control the update rate

if __name__ == '__main__':
    try:
        thruster_control_node = ThrusterControlNode()
        thruster_control_node.run()
    except rospy.ROSInterruptException:
        pass
