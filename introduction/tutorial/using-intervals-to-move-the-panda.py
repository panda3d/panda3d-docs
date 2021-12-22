from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.interval.IntervalGlobal import LerpPosInterval, LerpHprInterval
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

        # Create the sequence of lerp intervals needed for the panda to
        # walk back and forth.
        self.panda_pace = Sequence(
            LerpPosInterval(self.panda_actor, 13,
                            Point3(0, -10, 0), startPos=Point3(0, 10, 0)),
            LerpHprInterval(self.panda_actor, 3,
                            Point3(180, 0, 0), startHpr=Point3(0, 0, 0)),

            LerpPosInterval(self.panda_actor, 13,
                            Point3(0, 10, 0), startPos=Point3(0, -10, 0)),
            LerpHprInterval(self.panda_actor, 3,
                            Point3(0, 0, 0), startHpr=Point3(180, 0, 0)),
            name="panda-pace"
        )
        self.panda_pace.loop()

    # Define a procedure to move the camera.
    def spin_camera_task(self, task):
        angle_degrees = task.time * 6.0
        angle_radians = angle_degrees * (pi / 180.0)
        self.camera.set_pos(20 * sin(angle_radians), -20 * cos(angle_radians), 3)
        self.camera.set_hpr(angle_degrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()
