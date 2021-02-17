def validator(model, data):
    """
    Validate input data
    :param model:
    :param data:
    :return:
    """
    is_error = False
    try:
        for key in model.keys():
            if model[key].required and data.get(key) is None:
                is_error = True
                break
    except:
        is_error = True
    return is_error
