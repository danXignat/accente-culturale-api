from api.app import app

def main():
    import uvicorn
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=settings.port,
        reload=os.getenv("RENDER") != "true"  # No reload in production
    )

if __name__ == "__main__":
    main()

"""
DATABASE_URL=sqlite:///data/db.sqlite
JWT_SECRET_KEY=your_secure_secret_here
ADMIN_USERNAME=your_admin_username
ADMIN_PASSWORD=your_secure_password
RENDER=true
"""