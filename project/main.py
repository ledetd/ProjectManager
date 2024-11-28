import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('db.sqlite3')

df = pd.read_sql_query("SELECT * FROM project_day", cnx)

lift_frame_sum = df['lift_frame'].sum()
mpd_manifold_building_sum = df['mpd_manifold_building'].sum()
rcd_housing_sum = df['pipework'].sum()
pipework_sum = df['mpd_supervisor'].sum()
mpd_supervisor_sum = df['mpd_operator'].sum()
mpd_operator_sum = df['rcd_housing'].sum()

print('lift_frame', lift_frame_sum)
print('mpd_manifold_building',mpd_manifold_building_sum)
print('pipework',rcd_housing_sum)
print('mpd_supervisor',pipework_sum)
print('mpd_operator',mpd_supervisor_sum)
print('rcd_housing',mpd_operator_sum)

cnx.commit()
cnx.close()