# #!/usr/bin/env python3
# """
# Script to create database tables for the URL shortener application.
# Run this once to set up your database schema.
# """

# from app.database import engine, Base
# from app.features.url_shortener.models import URL

# def create_tables():
#     """Create all tables defined in models."""
#     try:
#         print("Creating database tables...")
#         Base.metadata.create_all(bind=engine)
#         print("✅ Tables created successfully!")
#         print("Tables created:")
#         print("- urls")
#     except Exception as e:
#         print(f"❌ Error creating tables: {e}")
#         raise

# if __name__ == "__main__":
#     create_tables()