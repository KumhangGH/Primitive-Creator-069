created_obj = None

		if obj_type == 'cube':
			created_obj = cmds.polyCube(name=obj_name)[0]
		elif obj_type == 'cone':
			created_obj = cmds.polyCone(name=obj_name)[0]
		elif obj_type == 'sphere':
			created_obj = cmds.polySphere(name=obj_name)[0]
		elif obj_type == 'torus':
			created_obj = cmds.polyTorus(name=obj_name)[0]
		else:
			cmds.warning(f"Unsupported object type: {obj_type}")
			return

		cmds.select(created_obj)
		print(f"Created object: {created_obj}")