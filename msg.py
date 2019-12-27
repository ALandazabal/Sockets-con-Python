SERVER:

#Asignación de nombres
json_msg = {
    'msg_type': 0,
    'client_name': client_name,
}

#Recurso ocupado
json_msg = {
    'msg_type': 1,
    'msg_subtype': 0,
}
#Recurso otorgado
json_msg = {
    'msg_type': 1,#Respuesta de recurso
    'msg_subtype': 1,#Msg de recurso ocupado
    'resource_index': client_msg['resource_index'] #nombre al cliente que se le otorgó
}

#Recurso por liberar
json_msg = {
    'msg_type': 1,  #Respuesta de recurso
    'msg_subtype': 2 #Msg de recurso por liberar
}

#último recurso
json_msg = {
    'msg_type': 2,
    'resource_index': client_msg['resource_index']
}

#Liberar recursos
json_msg = {
    'msg_type': 3,
}


CLIENT

#Solicitud de recurso
json_msg = {
    'msg_type': 0,
    'resource_index': index,
    'client_name': name,
}
#Solicitud último recurso
json_msg = {
    'msg_type': 1,
    'resource_index': missing_resource,
    'client_name': name
}
#Liberar recurso
json_msg = {
    'msg_type': 2,
    'client_name': name
}