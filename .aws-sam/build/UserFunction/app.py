import json
import os
from lib_users.database import DataBase
from lib_users.schemas import User, UpdateUser


def lambda_handler(event, context):
    print("Received event:", event)
    print("Context: ", context)

    data = {}
    status_code = 200
    try:
        db = DataBase()

        if event.get("path") == "/users" and event.get("httpMethod") == "GET":
            users = db.get_users()
            data = {"users": [dict(user) for user in users]}
        elif event.get("path") == "/users" and event.get("httpMethod") == "POST":
            body = json.loads(event.get("body"))
            user = User(**body).dict()
            user = db.create_user(user)
            data = {"user": user}
        #elif "/users/" in event.get("path") and event.get("httpMethod") == "PATCH":
            #id = event.get("pathParameters").get("id")
            #user = db.get_user_by_id(id)
            #if not user:
                #raise Exception("User not found")
            #body = json.loads(event.get("body"))
            #user = UpdateUser(**body).dict(exclude_none=True)
            #if not user:
                #raise Exception("No data to update")
            #user_update = db.update_user(id, user)
            #data = {"user": user_update}
            
        elif event.get("path") == "/users" and event.get("httpMethod") == "PATCH":
            body = json.loads(event.get("body"))
            user_id = body.get("id")
            user_updates = body.get("updates")
            if user_id is not None and user_updates:
                updated_user = db.update_user(user_id, user_updates)
                if updated_user:
                    data = {"user": updated_user}
            else:
                status_code = 404  # Usuario no encontrado
        else:
                status_code = 400  # Solicitud incorrecta, falta ID o actualizaciones


    except Exception as e:
        data = {"message": str(e)}
        status_code = 400

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"  # Encabezado agregado
        },
        "statusCode": status_code,
        "body": json.dumps(data),
    }
