#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import Range
import sonar_package.sonar
import time #Delay

class SonarPublisher:
    def __init__ (self, addr):
        self.addr = addr

    def sonar_talker(self):
        pub = rospy.Publisher('sonar' + str(self.addr) + '_range_topic', Int32, queue_size=10) # publisher object
        rospy.init_node('sonar' + str(self.addr) + '_publisher_node', anonymous=True) # initialize publisher node
        rate = rospy.Rate(10) # ros rate
        rospy.loginfo("Ros sonar node now publishing.")
        s = sonar_package.sonar.Sonar(self.addr)
        while not rospy.is_shutdown():
            rangeValue = s.read_range()
            rospy.loginfo(self.addr)
            rospy.loginfo(rangeValue)
            pub.publish(rangeValue)
            rate.sleep()

if __name__ == "__main__":
    try:
        t0x70 = SonarPublisher(0x70)
        t0x72 = SonarPublisher(0x72)
        t0x74 = SonarPublisher(0x74)
        rospy.loginfo("0x70")
        t0x70.sonar_talker()
        rospy.loginfo("0x72")
        t0x72.sonar_talker()
        rospy.loginfo("0x74")
        t0x74.sonar_talker()
    except rospy.ROSInterruptException:
        pass