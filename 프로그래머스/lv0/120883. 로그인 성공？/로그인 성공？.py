def solution(id_pw, db):
    for id_, pw in db :
        if id_pw[0] == id_ :
            if id_pw[1] == pw :
                result = "login"
                break
            elif id_pw[1] != pw :
                result = "wrong pw"
                break
        elif id_pw[0] != id_ :
            result = "fail"
    return result