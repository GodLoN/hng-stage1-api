from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "healthy"}

@app.get("/health")
async def health():
    return {"message": "healthy"}


@app.get("/me")
async def me():
    return {
        "name": "Godwin Obi",
	"email": "godlonwhitegtr28@gmail.com",
	"github": "https://github.com/GodLoN"
    }

