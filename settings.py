pip install dj.database-url
import dj.database-url
import os

DATABASE = {
  "default":dj_database_url.parse(os.environ.get("postgresql://test_db_3g5k_user:CEVBDa5ghaeNExGmYWo4qqkNMzqfejnV@dpg-d0epg0h5pdvs73au8520-a.oregon-postgres.render.com/test_db_3g5k"))
