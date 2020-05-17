#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist

def simplePublisher():
    rospy.init_node('node_pub_py_1', anonymous=True)
    pub = rospy.Publisher('/vel_msg_1', Twist, queue_size=10)
    vel_msg = Twist()
    rate = rospy.Rate(2) # 2Hz       # Frequence (F) = Number of msg.s/second
    print("Python Publisher Initialized")
    print("Publishing on topic /vel_msg_1")
    vel_msg.linear.x =1
    vel_msg.linear.y = 0   
    vel_msg.linear.z =0
    vel_msg.angular.x =0
    vel_msg.angular.y = 0   
    vel_msg.angular.z =0

    # The string to be published on the topic.
    # topic1_content = "my second ROS topic"

    while not rospy.is_shutdown() :
        pub.publish(vel_msg)
        rate.sleep()                 # Delay Time (T)   # T = 1/F = 0.5 sec

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass

