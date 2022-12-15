import numpy as np

import rclpy
from rclpy.node import Node

# from crazyflie_interfaces.msg import LogDataGeneric
# from geometry_msgs.msg import PoseStamped

from sensor_msgs.msg import Joy

from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter, ParameterValue, ParameterType

class TeleopNode(Node):

    def __init__(self):
        super().__init__('teleop_aug')

        self.cfs = ["cf5", "cf6", "cf231"]

        self.setParamsServiceServer = self.create_client(SetParameters, "/crazyflie_server/set_parameters")

        self.setParamsServiceTeleop = self.create_client(SetParameters, "/teleop/set_parameters")

        # self.publisher = self.create_publisher(
                # PoseStamped, "{}/frontnet_targetpos_typed".format(self.cf), 10)

        self.subscription1 = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10)

        self.timer = None


    def joy_callback(self, msg: Joy):
        # the expected configuration is
        # vars: ["frontnet.targetx", "frontnet.targety", "frontnet.targetz", "frontnet.targetyaw"]

        # self.get_logger().info('I heard: "%s"' % msg)

        # blue button: switch to payload controller
        if msg.buttons[2] == 1:
            # switch to payload controller
            for cf in self.cfs:
                param_name = "{}/params/stabilizer/controller".format(cf)
                value = 7
                param_type = ParameterType.PARAMETER_INTEGER
                param_value = ParameterValue(type=param_type, integer_value=int(value))
                req = SetParameters.Request()
                req.parameters = [Parameter(name=param_name, value=param_value)]
                self.setParamsServiceServer.call_async(req)

            # # switch to manual teleoperation after some time
            # if self.timer is None:
            #     self.timer = self.create_timer(2.0, self.timer_callback)


        # land: switch back to regular lee controller!
        if msg.buttons[6] == 1:
            for cf in self.cfs:
                param_name = "{}/params/stabilizer/controller".format(cf)
                value = 6
                param_type = ParameterType.PARAMETER_INTEGER
                param_value = ParameterValue(type=param_type, integer_value=int(value))
                req = SetParameters.Request()
                req.parameters = [Parameter(name=param_name, value=param_value)]
                self.setParamsServiceServer.call_async(req)

    def timer_callback(self):
        param_name = "mode"
        value = "cmd_vel_world"
        param_type = ParameterType.PARAMETER_STRING
        param_value = ParameterValue(type=param_type, string_value=str(value))
        req = SetParameters.Request()
        req.parameters = [Parameter(name=param_name, value=param_value)]
        self.setParamsServiceTeleop.call_async(req)

        self.timer.destroy()
        self.timer = None

def main(args=None):
    rclpy.init(args=args)

    node = TeleopNode()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()