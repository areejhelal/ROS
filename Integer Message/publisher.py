#!/usr/bin/env python
import rospy
#from std_msgs.msg import String
from std_msgs.msg import Int16

def simplePublisher():
    rospy.init_node('node_pub_py_1', anonymous=True)
    pub = rospy.Publisher('/test_topic_1', Int16, queue_size=10)
    rate = rospy.Rate(2) # 2Hz       # Frequence (F) = Number of msg.s/second
    print("Python Publisher Initialized")
    print("Publishing on topic /test_topic_1")

    # The string to be published on the topic.
    # topic1_content = "my second ROS topic"
    i=0
    while not rospy.is_shutdown() and i<11:
        pub.publish(i)
        #pub.publish("Hello ROS 008")
        #print("Hello")
	i=i+1
        rate.sleep()                 # Delay Time (T)   # T = 1/F = 0.5 sec

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass

