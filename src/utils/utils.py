from pydantic import BaseModel


def convert_tuple_to_model(model: BaseModel, data_tuple: tuple) -> BaseModel: 
    field_names = model.model_fields.keys() 
    data_dict = dict(zip(field_names, data_tuple)) 
    return model(**data_dict)