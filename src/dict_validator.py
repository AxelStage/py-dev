


eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}


##################

def match_keys(data, valid, path):
    data_keys = data.keys()
    valid_keys = valid.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys

    if missing_keys or extra_keys:
        missing_path = {path + "." + str(key) for key in missing_keys}
        missing_msg = ("Missing keys: " + ", ".join(missing_path)) if missing_keys else ""

        extra_path = {path + "." + str(key) for key in extra_keys}
        extra_msg = ("Extra keys: " + ", ".join(extra_path)) if extra_keys else ""

        return False, " ".join((missing_msg, extra_msg))
    else:
        return True, None


def match_types(data, template, path):

    for key, value in template.items():

        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value

        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            error_msg = ( "incorrect type " + path + "." + key +
                          " -> expected " + template_type.__name__ +
                          ", found " + type(data_value).__name__)

            return False, error_msg

    return True, None

def recurse_validate(data, template, path=""):
    is_ok, error_msg = match_keys(data, template, path)
    if not is_ok:
        return False, error_msg

    is_ok, error_msg = match_types(data, template, path)
    if not is_ok:
        return False, error_msg

    dictionary_type_keys =  {key for key,value in template.items() if isinstance(value, dict)}

    for key in dictionary_type_keys:
        sub_path = path + "." + str(key)
        sub_template = template[key]
        sub_data = data[key]
        is_ok, error_msg = recurse_validate(sub_data, sub_template, sub_path)

        if not is_ok:
            return False, error_msg

    return True, None

# class SchemaError(Exception):
#     pass

# def validate(data, template):
#     is_ok, error_msg = recurse_validate(data, template, "")

#     if not is_ok:
#         raise SchemaError(error_msg)