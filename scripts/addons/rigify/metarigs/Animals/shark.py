# SPDX-FileCopyrightText: 2017-2022 Blender Foundation
#
# SPDX-License-Identifier: GPL-2.0-or-later

import bpy

from mathutils import Color


def create(obj):  # noqa
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    for i in range(6):
        arm.rigify_colors.add()

    arm.rigify_colors[0].name = "Root"
    arm.rigify_colors[0].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[0].normal = Color((0.4353, 0.1843, 0.4157))
    arm.rigify_colors[0].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[0].standard_colors_lock = True
    arm.rigify_colors[1].name = "IK"
    arm.rigify_colors[1].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[1].normal = Color((0.6039, 0.0000, 0.0000))
    arm.rigify_colors[1].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[1].standard_colors_lock = True
    arm.rigify_colors[2].name = "Specials"
    arm.rigify_colors[2].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[2].normal = Color((0.9569, 0.7882, 0.0471))
    arm.rigify_colors[2].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[2].standard_colors_lock = True
    arm.rigify_colors[3].name = "Tweak"
    arm.rigify_colors[3].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[3].normal = Color((0.0392, 0.2118, 0.5804))
    arm.rigify_colors[3].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[3].standard_colors_lock = True
    arm.rigify_colors[4].name = "FK"
    arm.rigify_colors[4].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[4].normal = Color((0.1176, 0.5686, 0.0353))
    arm.rigify_colors[4].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[4].standard_colors_lock = True
    arm.rigify_colors[5].name = "Extra"
    arm.rigify_colors[5].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[5].normal = Color((0.9686, 0.2510, 0.0941))
    arm.rigify_colors[5].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[5].standard_colors_lock = True

    bone_collections = {}

    for bcoll in list(arm.collections_all):
        arm.collections.remove(bcoll)

    def add_bone_collection(name, *, ui_row=0, ui_title='', sel_set=False, color_set_id=0):
        new_bcoll = arm.collections.new(name)
        new_bcoll.rigify_ui_row = ui_row
        new_bcoll.rigify_ui_title = ui_title
        new_bcoll.rigify_sel_set = sel_set
        new_bcoll.rigify_color_set_id = color_set_id
        bone_collections[name] = new_bcoll

    def assign_bone_collections(pose_bone, *coll_names):
        assert not len(pose_bone.bone.collections)
        for name in coll_names:
            bone_collections[name].assign(pose_bone)

    def assign_bone_collection_refs(params, attr_name, *coll_names):
        ref_list = getattr(params, attr_name + '_coll_refs', None)
        if ref_list is not None:
            for name in coll_names:
                ref_list.add().set_collection(bone_collections[name])

    add_bone_collection('Face', ui_row=1, color_set_id=5)
    add_bone_collection('Face (Tweak)', ui_row=2, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Spine', ui_row=4, color_set_id=3)
    add_bone_collection('Spine (Tweak)', ui_row=5, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Tail', ui_row=6, color_set_id=6)
    add_bone_collection('Fins.L', ui_row=8, color_set_id=5)
    add_bone_collection('Fins.L (Tweak)', ui_row=9, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Fins.R', ui_row=8, color_set_id=5)
    add_bone_collection('Fins.R (Tweak)', ui_row=9, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Fins', ui_row=11, color_set_id=3)
    add_bone_collection('Fins (Tweak)', ui_row=12, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Root', ui_row=15, color_set_id=1)

    bones = {}

    bone = arm.edit_bones.new('spine.003')
    bone.head = -0.0000, 0.3182, 0.4031
    bone.tail = -0.0000, 0.0152, 0.3904
    bone.roll = 0.0001
    bone.use_connect = False
    bones['spine.003'] = bone.name
    bone = arm.edit_bones.new('spine.002')
    bone.head = -0.0000, 0.3182, 0.4031
    bone.tail = -0.0000, 0.7152, 0.4305
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['spine.002'] = bone.name
    bone = arm.edit_bones.new('spine.008')
    bone.head = -0.0000, 0.0152, 0.3904
    bone.tail = 0.0000, -0.3259, 0.3967
    bone.roll = 0.0001
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.003']]
    bones['spine.008'] = bone.name
    bone = arm.edit_bones.new('spine.001')
    bone.head = -0.0000, 0.7152, 0.4305
    bone.tail = -0.0000, 1.0816, 0.4540
    bone.roll = -0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.002']]
    bones['spine.001'] = bone.name
    bone = arm.edit_bones.new('spine.004')
    bone.head = 0.0000, -0.3259, 0.3967
    bone.tail = 0.0000, -0.5947, 0.4044
    bone.roll = -0.0001
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.008']]
    bones['spine.004'] = bone.name
    bone = arm.edit_bones.new('chest_fin.Bot.L')
    bone.head = 0.0889, 0.2605, 0.2866
    bone.tail = 0.1731, 0.3299, 0.1901
    bone.roll = -2.3171
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.008']]
    bones['chest_fin.Bot.L'] = bone.name
    bone = arm.edit_bones.new('chest_fin.Bot.R')
    bone.head = -0.0889, 0.2605, 0.2866
    bone.tail = -0.1731, 0.3299, 0.1901
    bone.roll = 2.3171
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.008']]
    bones['chest_fin.Bot.R'] = bone.name
    bone = arm.edit_bones.new('spine')
    bone.head = -0.0000, 1.0816, 0.4540
    bone.tail = -0.0000, 1.3362, 0.4776
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.001']]
    bones['spine'] = bone.name
    bone = arm.edit_bones.new('mid_fin.Top')
    bone.head = 0.0000, 0.7296, 0.5396
    bone.tail = 0.0000, 0.7709, 0.6351
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.001']]
    bones['mid_fin.Top'] = bone.name
    bone = arm.edit_bones.new('mid_fin.Bot')
    bone.head = 0.0000, 0.7296, 0.3505
    bone.tail = 0.0000, 0.8233, 0.2684
    bone.roll = 1.5708
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.001']]
    bones['mid_fin.Bot'] = bone.name
    bone = arm.edit_bones.new('spine.005')
    bone.head = 0.0000, -0.5947, 0.4044
    bone.tail = 0.0000, -1.2084, 0.4328
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.004']]
    bones['spine.005'] = bone.name
    bone = arm.edit_bones.new('top_fin')
    bone.head = 0.0000, -0.2777, 0.5550
    bone.tail = 0.0000, -0.1962, 0.7053
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.004']]
    bones['top_fin'] = bone.name
    bone = arm.edit_bones.new('back_fin.T.Bk')
    bone.head = 0.0000, 1.2501, 0.5345
    bone.tail = 0.0000, 1.5211, 0.7594
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['back_fin.T.Bk'] = bone.name
    bone = arm.edit_bones.new('back_fin.B.Bk')
    bone.head = 0.0000, 1.2305, 0.4158
    bone.tail = 0.0000, 1.3289, 0.2452
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine']]
    bones['back_fin.B.Bk'] = bone.name
    bone = arm.edit_bones.new('spine.006')
    bone.head = 0.0000, -1.2084, 0.4328
    bone.tail = 0.0000, -1.5634, 0.4275
    bone.roll = -0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['spine.006'] = bone.name
    bone = arm.edit_bones.new('shoulder.L')
    bone.head = 0.0729, -0.9648, 0.3756
    bone.tail = 0.2649, -0.9648, 0.3157
    bone.roll = 3.4558
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['shoulder.L'] = bone.name
    bone = arm.edit_bones.new('shoulder.R')
    bone.head = -0.0729, -0.9648, 0.3756
    bone.tail = -0.2649, -0.9648, 0.3157
    bone.roll = -3.4558
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.005']]
    bones['shoulder.R'] = bone.name
    bone = arm.edit_bones.new('top_fin.001')
    bone.head = 0.0000, -0.1962, 0.7053
    bone.tail = 0.0000, -0.1362, 0.8158
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['top_fin']]
    bones['top_fin.001'] = bone.name
    bone = arm.edit_bones.new('back_fin.T.001.Bk')
    bone.head = 0.0000, 1.5211, 0.7594
    bone.tail = 0.0000, 1.7667, 0.9633
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['back_fin.T.Bk']]
    bones['back_fin.T.001.Bk'] = bone.name
    bone = arm.edit_bones.new('back_fin.B.001.Bk')
    bone.head = 0.0000, 1.3289, 0.2452
    bone.tail = 0.0000, 1.3818, 0.1513
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['back_fin.B.Bk']]
    bones['back_fin.B.001.Bk'] = bone.name
    bone = arm.edit_bones.new('spine.007')
    bone.head = 0.0000, -1.5634, 0.4275
    bone.tail = 0.0000, -2.0661, 0.4364
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['spine.006']]
    bones['spine.007'] = bone.name
    bone = arm.edit_bones.new('side_fin.L')
    bone.head = 0.2140, -0.9624, 0.2213
    bone.tail = 0.5220, -0.9078, -0.1343
    bone.roll = -2.3170
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.L']]
    bones['side_fin.L'] = bone.name
    bone = arm.edit_bones.new('side_fin.R')
    bone.head = -0.2140, -0.9624, 0.2213
    bone.tail = -0.5220, -0.9078, -0.1343
    bone.roll = 2.3170
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['shoulder.R']]
    bones['side_fin.R'] = bone.name
    bone = arm.edit_bones.new('back_fin.T.002.Bk')
    bone.head = 0.0000, 1.7667, 0.9633
    bone.tail = 0.0000, 1.9489, 1.1145
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['back_fin.T.001.Bk']]
    bones['back_fin.T.002.Bk'] = bone.name
    bone = arm.edit_bones.new('eye.L')
    bone.head = 0.1405, -1.6860, 0.4161
    bone.tail = 0.3684, -1.6810, 0.4156
    bone.roll = 3.1352
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.007']]
    bones['eye.L'] = bone.name
    bone = arm.edit_bones.new('eye.R')
    bone.head = -0.1405, -1.6860, 0.4161
    bone.tail = -0.3684, -1.6810, 0.4156
    bone.roll = -3.1352
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.007']]
    bones['eye.R'] = bone.name
    bone = arm.edit_bones.new('jaw.master')
    bone.head = -0.0000, -1.5791, 0.2788
    bone.tail = 0.0000, -1.9421, 0.3386
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['spine.007']]
    bones['jaw.master'] = bone.name
    bone = arm.edit_bones.new('side_fin.L.001')
    bone.head = 0.5220, -0.9078, -0.1343
    bone.tail = 0.7928, -0.7598, -0.4802
    bone.roll = -2.2826
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['side_fin.L']]
    bones['side_fin.L.001'] = bone.name
    bone = arm.edit_bones.new('side_fin.R.001')
    bone.head = -0.5220, -0.9078, -0.1343
    bone.tail = -0.7928, -0.7598, -0.4802
    bone.roll = 2.2826
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['side_fin.R']]
    bones['side_fin.R.001'] = bone.name
    bone = arm.edit_bones.new('jaw')
    bone.head = -0.0000, -1.5791, 0.2788
    bone.tail = 0.0000, -1.7326, 0.3041
    bone.roll = 0.0000
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['jaw.master']]
    bones['jaw'] = bone.name
    bone = arm.edit_bones.new('jaw.002.L')
    bone.head = 0.0891, -1.5791, 0.2894
    bone.tail = 0.1110, -1.7198, 0.3129
    bone.roll = 1.4894
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['jaw.master']]
    bones['jaw.002.L'] = bone.name
    bone = arm.edit_bones.new('jaw.002.R')
    bone.head = -0.0891, -1.5791, 0.2894
    bone.tail = -0.1110, -1.7198, 0.3129
    bone.roll = -1.4894
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['jaw.master']]
    bones['jaw.002.R'] = bone.name
    bone = arm.edit_bones.new('jaw.001')
    bone.head = 0.0000, -1.7326, 0.3041
    bone.tail = 0.0000, -1.8860, 0.3294
    bone.roll = 0.0000
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['jaw']]
    bones['jaw.001'] = bone.name
    bone = arm.edit_bones.new('jaw.003.L')
    bone.head = 0.1110, -1.7198, 0.3129
    bone.tail = 0.1260, -1.8159, 0.3326
    bone.roll = 1.2807
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['jaw.002.L']]
    bones['jaw.003.L'] = bone.name
    bone = arm.edit_bones.new('jaw.003.R')
    bone.head = -0.1110, -1.7198, 0.3129
    bone.tail = -0.1260, -1.8159, 0.3326
    bone.roll = -1.2807
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['jaw.002.R']]
    bones['jaw.003.R'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['spine.003']]
    pbone.rigify_type = 'spines.basic_spine'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Spine (Tweak)')
    assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Spine (Tweak)')
    pbone = obj.pose.bones[bones['spine.002']]
    pbone.rigify_type = 'spines.basic_tail'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Tail')
    try:
        pbone.rigify_parameters.connect_chain = True
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.copy_rotation_axes = (True, False, True)
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Spine (Tweak)')
    pbone = obj.pose.bones[bones['spine.008']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    pbone = obj.pose.bones[bones['spine.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Tail')
    pbone = obj.pose.bones[bones['spine.004']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    pbone = obj.pose.bones[bones['chest_fin.Bot.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Spine (Tweak)')
    pbone = obj.pose.bones[bones['chest_fin.Bot.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Tail')
    pbone = obj.pose.bones[bones['spine']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Tail')
    pbone = obj.pose.bones[bones['mid_fin.Top']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    pbone = obj.pose.bones[bones['mid_fin.Bot']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    pbone = obj.pose.bones[bones['spine.005']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    pbone = obj.pose.bones[bones['top_fin']]
    pbone.rigify_type = 'limbs.simple_tentacle'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fins (Tweak)')
    pbone = obj.pose.bones[bones['back_fin.T.Bk']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    try:
        pbone.rigify_parameters.primary_rotation_axis = 'Z'
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fins (Tweak)')
    pbone = obj.pose.bones[bones['back_fin.B.Bk']]
    pbone.rigify_type = 'limbs.super_finger'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    try:
        pbone.rigify_parameters.primary_rotation_axis = 'Z'
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fins (Tweak)')
    pbone = obj.pose.bones[bones['spine.006']]
    pbone.rigify_type = 'spines.super_head'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    try:
        pbone.rigify_parameters.connect_chain = True
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Spine (Tweak)')
    pbone = obj.pose.bones[bones['shoulder.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    try:
        pbone.rigify_parameters.make_widget = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['shoulder.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    try:
        pbone.rigify_parameters.make_widget = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['top_fin.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    pbone = obj.pose.bones[bones['back_fin.T.001.Bk']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    pbone = obj.pose.bones[bones['back_fin.B.001.Bk']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    pbone = obj.pose.bones[bones['spine.007']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Spine')
    pbone = obj.pose.bones[bones['side_fin.L']]
    pbone.rigify_type = 'limbs.simple_tentacle'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins.L')
    try:
        pbone.rigify_parameters.copy_rotation_axes = (True, False, False)
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fins.L (Tweak)')
    pbone = obj.pose.bones[bones['side_fin.R']]
    pbone.rigify_type = 'limbs.simple_tentacle'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins.R')
    try:
        pbone.rigify_parameters.copy_rotation_axes = (True, False, False)
    except AttributeError:
        pass
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fins.R (Tweak)')
    pbone = obj.pose.bones[bones['back_fin.T.002.Bk']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins')
    pbone = obj.pose.bones[bones['eye.L']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['eye.R']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['jaw.master']]
    pbone.rigify_type = 'basic.super_copy'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    try:
        pbone.rigify_parameters.make_widget = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.make_deform = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['side_fin.L.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins.L')
    pbone = obj.pose.bones[bones['side_fin.R.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Fins.R')
    pbone = obj.pose.bones[bones['jaw']]
    pbone.rigify_type = 'limbs.simple_tentacle'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Face (Tweak)')
    pbone = obj.pose.bones[bones['jaw.002.L']]
    pbone.rigify_type = 'limbs.simple_tentacle'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Face (Tweak)')
    pbone = obj.pose.bones[bones['jaw.002.R']]
    pbone.rigify_type = 'limbs.simple_tentacle'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Face (Tweak)')
    pbone = obj.pose.bones[bones['jaw.001']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['jaw.003.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')
    pbone = obj.pose.bones[bones['jaw.003.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    assign_bone_collections(pbone, 'Face')

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        bone.bbone_x = bone.bbone_z = bone.length * 0.05
        arm.edit_bones.active = bone

    arm.collections.active_index = 0

    return bones


if __name__ == "__main__":
    create(bpy.context.active_object)