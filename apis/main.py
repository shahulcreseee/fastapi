from fastapi import FastAPI, Body
import schemas

app = FastAPI()

fakeDB = {
    1:{'one':'morning'},
    2:{'two','afternoon'},
    3:{'three','evening'}
}

@app.get("/")
def getItems():
    return fakeDB

@app.get("/{id}")
def getItem(id:int):
    return fakeDB[id]

@app.post("/")
def postItem(task: str):
    newId = len(fakeDB.keys())+1
    fakeDB[newId] = {"task": task}
    return fakeDB

@app.post("/item")
def addItem(item: schemas.Item):
    newId = len(fakeDB.keys()) + 1
    fakeDB[newId] = {"task": item.task}
    return fakeDB

@app.post("/itembody")
def addItemBody(body = Body()):
    newId = len(fakeDB.keys()) + 1
    fakeDB[newId] = {"task": body['task']}
    return fakeDB

@app.put("/{id}")
def updateItem(id: int, item: schemas.Item):
    fakeDB[id]['task'] = item.task
    return fakeDB

@app.delete("/{id}")
def deleteItem(id: int):
    del fakeDB[id]
    return fakeDB