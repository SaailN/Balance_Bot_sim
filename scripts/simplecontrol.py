#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
ax=0
ay=0
az=0

def callback(data):
    global ax,ay,az
    ax=data.linear_acceleration.x
    ay=data.linear_acceleration.y
    az=data.linear_acceleration.z
    print(data.linear_acceleration)
    print("...........................")

    vr=data.angular_velocity.x
    vp=data.angular_velocity.y
    vy=data.angular_velocity.z
    print(data.angular_velocity)
    print("________________________________________")




def talker():
    global ax,ay,az
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)   
    rospy.init_node('velocity_pub', anonymous=False)
    msg = Twist()

    # rospy.init_node('sensor_read', anonymous=True)

    rospy.Subscriber("/imu", Imu, callback)


    msg.linear.x = 0
    msg.linear.y = 0
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = 0

    if ax>0.6:
        msg.linear.x = 0.1
    if ax<0.6:
        msg.linear.x = -0.1


    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass