#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def msg_cb(msg):
	rospy.loginfo("Linear Components: [%d, %d, %d]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    	rospy.loginfo("Angular Components: [%d, %d, %d]"%(msg.angular.x, msg.angular.y, msg.angular.z))

def subscriber_1():
    rospy.init_node('node_sub_py_1', anonymous=True)
    print("Python Subscriber Initialized")
    print("Subscribing to topic /vel_msg_1")
    rospy.Subscriber('/vel_msg_1', Twist, msg_cb)
    rospy.spin()

if __name__== '__main__':
    try:
        subscriber_1()
    except rospy.ROSInterruptException:
        pass

