from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable the camera trackball controls.
        self.disable_mouse()

        # Load the environment model.
        self.scene = self.loader.load_model("models/environment")
        # Reparent the model to render.
        self.scene.reparent_to(self.render)
        # Apply scale and position transforms on the model.
        self.scene.set_scale(0.25, 0.25, 0.25)
        self.scene.set_pos(-8, 42, 0)

        # Add the spin_camera_task procedure to the task manager.
        self.taskMgr.add(self.spin_camera_task)

        # Load and transform the panda actor.
        self.panda_actor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.panda_actor.set_scale(0.005, 0.005, 0.005)
        self.panda_actor.reparent_to(self.render)
        # Loop its animation.
        self.panda_actor.loop("walk")

        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pos_ival1 = self.panda_actor.posInterval(13,
                                                 Point3(0, -10, 0),
                                                 startPos=Point3(0, 10, 0))
        pos_ival2 = self.panda_actor.posInterval(13,
                                                 Point3(0, 10, 0),
                                                 startPos=Point3(0, -10, 0))
        hpr_ival1 = self.panda_actor.hprInterval(3,
                                                 Point3(180, 0, 0),
                                                 startHpr=Point3(0, 0, 0))
        hpr_ival2 = self.panda_actor.hprInterval(3,
                                                 Point3(0, 0, 0),
                                                 startHpr=Point3(180, 0, 0))

        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(pos_ival1, hpr_ival1,
                                  pos_ival2, hpr_ival2,
                                  name="pandaPace")
        self.pandaPace.loop()

    # Define a procedure to move the camera.
    def spin_camera_task(self, task):
        angle_degrees = task.time * 6.0
        angle_radians = angle_degrees * (pi / 180.0)
        self.camera.set_pos(20 * sin(angle_radians), -20 * cos(angle_radians), 3)
        self.camera.set_hpr(angle_degrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()
