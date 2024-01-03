from fastapi import HTTPException


def error_handler(cod_error, message=""):
    if cod_error == 400 and message == "":
        return HTTPException(status_code=400,
                             detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                    "ocurriendo una división por 0.")
    else:
        return HTTPException(status_code=cod_error,
                             detail=message)

