#!/usr/bin/env python
import rospy
#from std_msgs.msg import String
from std_msgs.msg import Int16

def msg_cb(d):
    print(d.data)

def subscriber_1():
    rospy.init_node('node_sub_py_1', anonymous=True)
    print("Python Subscriber Initialized")
    print("Subscribing to topic /test_topic_1")
    rospy.Subscriber('/test_topic_1', Int16, msg_cb)
    #rospy.Subscriber('/pub_topic_1', String, msg_cb)
    rospy.spin()

if __name__== '__main__':
    try:
        subscriber_1()
    except rospy.ROSInterruptException:
        pass

