import bpy

class ArmOffsets(bpy.types.PropertyGroup):
    # wrist_roll_offset = bpy.props.FloatProperty(
    #     name = "Float Value",
    #     description = "A float property",
    #     default = 23.7,
    #     min = 0.01,
    #     max = 30.0
    #     )
           
    turret_offset = bpy.props.IntProperty(
        name = "Turret Offset",
        description="A integer property",
        default = 0,
        min = -10000,
        max = 10000
        )

    shoulder_offset = bpy.props.IntProperty(
        name = "Shoulder Offset",
        description="A integer property",
        default = 0,
        min = -1000,
        max = 1000
        )

    elbow_offset = bpy.props.IntProperty(
        name = "Elbow Offset",
        description="A integer property",
        default = 0,
        min = -1000,
        max = 1000
        )


    wrist_L_offset = bpy.props.IntProperty(
        name = "Wrist Pitch Offset",
        description="A integer property",
        default = 0,
        min = -40000,
        max = 40000,
        soft_max= 5000,
        soft_min= -5000)

    wrist_R_offset = bpy.props.IntProperty(
        name = "Wrist Yaw Offset",
        description="A integer property",
        default = 0,
        min = -40000,
        max = 40000,
        soft_max= 5000,
        soft_min= -5000)


    wrist_roll_offset = bpy.props.IntProperty(
        name = "Wrist Roll Offset",
        description="A integer property",
        default = 0,
        max= 30000,
        min= -30000,
        soft_min = -5000,
        soft_max = 5000
        )

    
    gripper_offset = bpy.props.IntProperty(
        name = "Gripper Offset",
        description="A integer property",
        default = 0,
        min = -50,
        max = 50
        )

        
class ArmOffsetsPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Arm Offsets"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        layout.label(text=" Simple Row:")

        col = layout.column()
        col.prop(scene.arm_offsets, "gripper_offset", slider=True)
        col.prop(scene.arm_offsets, "wrist_roll_offset", slider=True)
        
        col.prop(scene.arm_offsets, "wrist_R_offset", slider=True)
        col.prop(scene.arm_offsets, "wrist_L_offset", slider=True)

        col.prop(scene.arm_offsets, "elbow_offset", slider=True)
        col.prop(scene.arm_offsets, "shoulder_offset", slider=True)
        col.prop(scene.arm_offsets, "turret_offset", slider=True)

def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.arm_offsets = bpy.props.PointerProperty(type=ArmOffsets)
   ## bpy.utils.register_class(ArmOffsetsPanel)


def unregister():
    #bpy.utils.unregister_class(ArmOffsetsPanel)
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.arm_offsets


if __name__ == "__main__":
    register()
