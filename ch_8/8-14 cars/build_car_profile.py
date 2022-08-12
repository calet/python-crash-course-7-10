def car_info(manufacturer, model, **whole):
    whole["manufacturer"] = manufacturer
    whole["model"] = model
    return whole
