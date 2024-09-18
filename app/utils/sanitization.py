def sanitize_object(obj):
    if obj:
        obj_dict = obj.__dict__.copy()
        obj_dict.pop("_sa_instance_state", None)
        user_roles = ["user", "role"]
        for user_role in user_roles:
            if obj_dict.get(user_role):
                enum_role = obj_dict[user_role].__dict__
                enum_role.pop("__objclass__", None)
                obj_dict[user_role] = enum_role["_name_"]
        return obj_dict
    return None
