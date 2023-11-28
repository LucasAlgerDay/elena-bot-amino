import amino

def joincomm(client, link):
    if link.startswith('http://aminoapps.com/c/'):
        aminoId = link[23:]
    if link.startswith('https://aminoapps.com/c/'):
        aminoId = link[24:]
    try:
        aminoId = client.search_community(aminoId).comId[0]
    except Exception:
        return {"error": "not found", "comId": None}
    try:
        client.join_community(aminoId)
    except Exception:
        return {"error": "join error", "comId": None}
    return {"error": "ok", "comId": aminoId}