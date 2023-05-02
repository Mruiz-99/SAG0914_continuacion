import mysql.connector


mydb = mysql.connector.connect(
  host="sa-proyecto.cqhgglpbcr1a.us-east-1.rds.amazonaws.com",
  user="admin",
  password="Salesa123.",
  database='sa_p',
  autocommit = True
)
