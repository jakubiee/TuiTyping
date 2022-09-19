import json

def read_settings_file():
    with open('./src/settings.json', 'r') as settings:
        data = json.load(settings)
    return data

def write_settings_file(new_settings):
    with open('./src/settings.json', 'w') as settings:
        settings.write(json.dumps(new_settings))
    return

def get_setting_value(key):
    data = read_settings_file()
    return data[key]

def edit_setting_value(key, value):
    data = read_settings_file()
    data[key] = value
    write_settings_file(data)