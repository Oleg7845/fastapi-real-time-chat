import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=5000, workers=2, reload=True)


#uvicorn main:app2 --host 0.0.0.0 --port 80 --workers 2