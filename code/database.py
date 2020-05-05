import psycopg2
import os

class DatabaseController:

	def __init__(self):
		db_port = os.getenv('db_port') or '5432';
		connection_string = "host='localhost' \
							dbname='dbms_final_project' \
							user='dbms_project_user' \
							password='dbms_password' \
							port=" + db_port;
		self.conn = psycopg2.connect(connection_string)

	# Private method to abstract running query
	def __runQuery(self, query, params=()):
		with self.conn.cursor() as cursor:
			cursor.execute(query, params)
			return cursor.fetchall()

	def find_specific_cancer(self,cancer_type):
		query = "SELECT * FROM cancers WHERE CANCER LIKE %s;"
		return self.__runQuery(query,[cancer_type])


	def select_toxin_cancer_correlation(self, cancer_type, toxin_type):
		sql = """
		SELECT ((cancers.cases::DOUBLE PRECISION / cancers.population) * 100) as rate, toxins.%s
		FROM cancers,toxins
		WHERE cancers.county = toxins.county
		AND toxins.%s != 0
		AND cancers.cancer = %s
		ORDER BY rate ASC, toxins.%s ASC
		""" % (toxin_type, toxin_type, "'"+cancer_type+"'", toxin_type)
		return self.__runQuery(sql, [])

	def high_low_comparison(self,cancer_type):
		query = """SELECT toxins.county,
					min_cancer.cancer, max_cancer.cancer, min_cancer.cases, max_cancer.cases,
					toxins.voc, toxins.nox, toxins.co, toxins.co2, toxins.particulate, toxins.pm10, toxins.pm25, toxins.haps, toxins.so2
					FROM toxins
					LEFT JOIN(
						SELECT county, cancer, cases
						FROM cancers
						WHERE cases != 0
						AND cancer LIKE %s
						ORDER BY cases ASC
						LIMIT 1
					) AS min_cancer
					ON toxins.county = min_cancer.county
					LEFT JOIN(
						SELECT county, cancer, cases
						FROM cancers
						WHERE cases != 0
						AND cancer LIKE %s
						ORDER BY cases DESC
						LIMIT 1
					) AS max_cancer
					ON toxins.county = max_cancer.county
					WHERE (min_cancer.cases IS NOT NULL OR max_cancer.cases IS NOT NULL);"""
		return self.__runQuery(query,[cancer_type,cancer_type])




def main():
	print("This class should not be run on it's own.")

if __name__ == "__main__":
	main()