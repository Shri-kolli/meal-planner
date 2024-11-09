from main import db

if __name__ == "__main__":
    print("Creating database tables...")
    db.create_all()
    print("Tables created successfully.")
