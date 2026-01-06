def _lower_setting(setting):
    key_orig, value_orig = setting
    key = key_orig.lower()
    value = value_orig.lower()
    return (key, value)


def add_setting(settings, setting):
    key, value = _lower_setting(setting)

    if key in settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, setting):
    key, value = _lower_setting(setting)

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings):
    if not len(settings):
        return "No settings available."

    result = "Current User Settings:\n"
    for key, val in settings.items():
        result += f"{key.capitalize()}: {val}\n"

    return result


test_settings = {}
add_setting(test_settings, ("theme", "dark"))
add_setting(test_settings, ("notifications", "enabled"))

# delete_setting({'theme': 'light'}, 'theme')
# print(view_settings(test_settings))
