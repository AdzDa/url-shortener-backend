# from sqlalchemy import text
# from app.database import engine

# # Check what columns exist in the urls table
# with engine.connect() as connection:
#     try:
#         result = connection.execute(text("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'urls'"))
#         print("Current 'urls' table columns:")
#         for row in result:
#             print(f"  - {row.column_name}: {row.data_type}")
#     except Exception as e:
#         print(f"Error: {e}")
        
#     # Also show the table structure
#     try:
#         result = connection.execute(text("\\d urls"))
#         print("\nTable structure:")
#         for row in result:
#             print(row)
#     except Exception as e:
#         print(f"Could not show table structure: {e}")