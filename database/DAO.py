from database.DB_connect import DBConnect
from model.piloti import PilotaGara


class DAO:

    @staticmethod
    def get_anni():
        cnx = DBConnect.get_connection()
        a = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query1 = """SELECT DISTINCT year as y
                           FROM seasons
                        """
            cursor.execute(query1)
            for row in cursor:
                a.append(row["y"])
            cursor.close()
            cnx.close()
        return a

    @staticmethod
    def get_piloti(data):
        cnx = DBConnect.get_connection()
        a = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query1 = """SELECT d.driverId, forename, surname, position, rc.raceId 
                        FROM drivers d, results r, races rc
                        WHERE rc.raceId = r.raceId and r.driverId = d.driverId and year = %s and position is not null
                    """
            cursor.execute(query1, (data,))
            for row in cursor:
                a.append(PilotaGara(**row))
            cursor.close()
            cnx.close()
        return a


if __name__ == '__main__':
    DAO = DAO()
    print(DAO.get_piloti(1963))