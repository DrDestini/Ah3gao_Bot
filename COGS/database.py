import mariadb

remoteTest = False

def getConnection():
    try:
        if remoteTest:
            con = mariadb.connect(
                user='remote',
                password='root',
                host='192.168.1.69',
                port=3306,
                database='discord_Bot'
            )
            return con
        else:
            con = mariadb.connect(
                user='pi',
                password='root',
                host='localhost',
                database='discord_Bot'
            )
            return con
    except mariadb.Error as e:
        print(f'There has been an error connecting to MariaDB: {e}')

def registerUser(discordID):
    con = getConnection()
    cur = con.cursor()

    try:
        cur.execute("INSERT INTO Users (discordID) VALUES(?)", (discordID,))
        cur.execute("INSERT INTO fishingStats (id) SELECT id FROM Users WHERE discordID=?", (discordID,))
        con.commit()
    except mariadb.Error as e:
        print(f'Error while registering user: {e}')


def doesExist(discordID):
    con = getConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT id FROM Users WHERE discordID=?", (discordID,))
        lst = cur.fetchall()
        if lst:
            return True
        else:
            registerUser(discordID)
            return False
    except mariadb.Error as e:
        print(f"Error while checking if user {discordID} exists: {e}")

def saidUwU(discordID):
    con = getConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT uwuCounter FROM Users WHERE discordID=?", (discordID,))
        lst = cur.fetchall()
        if lst:
            cur.execute("UPDATE Users SET uwuCounter=uwuCounter+1 WHERE discordID=?", (discordID,))
            con.commit()
        else:
            print(f'{discordID} is not in Database')
            registerUser(discordID)

    except mariadb.Error as e:
        print('error in SaidUWU: {e}')
    cur.close()
    con.close()

def saidOwO(discordID):
    con = getConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT owoCounter FROM Users WHERE discordID=?", (discordID,))
        lst = cur.fetchall()
        if lst:
            cur.execute("UPDATE Users SET owoCounter=owoCounter+1 WHERE discordID=?", (discordID,))
            con.commit()
        else:
            print(f'{discordID} is not in Database')
            registerUser(discordID)
    except mariadb.Error as e:
        print('error in SaidUWU: {e}')
    cur.close()
    con.close()

def getUwUOwO(discordID):  
    con = getConnection()
    cur = con.cursor()

    try:
        cur.execute("SELECT uwuCounter, owoCounter FROM Users WHERE discordID=?", (discordID,))
        lst = cur.fetchall()
        if lst:
            return lst
        else:
            registerUser(discordID)
            return None
    except mariadb.Error as e:
        print(f'Error in getUWUOWO: {e}')

    cur.close()
    con.close()

def getBalance(discordID):
    con = getConnection()
    cur = con.cursor()
    
    try:
        cur.execute("SELECT balance FROM Users WHERE discordID=?",(discordID,))
        lst = cur.fetchall()
        if lst:
            return lst[0][0]
        else:
            registerUser(discordID)
            return 100.0
    except mariadb.Error as e:
        print(f'Error fetching balance: {e}')

    cur.close()
    con.close()

def getDeuda(discordID):
    con = getConnection()
    cur = con.cursor()

    try:
        cur.execute("SELECT debt FROM Users WHERE discordID=?", (discordID,))
        lst = cur.fetchall()
        if lst:
            return lst[0][0]
        else:
            registerUser(discordID)
            return 0.0
    except mariadb.Error as e:
        print(f' Error fetching debt: {e}')
    
    cur.close()
    con.close()
def pedirCredito(discordID, credito):
    con = getConnection()
    cur = con.cursor()
    
    try:
        cur.execute("UPDATE Users SET balance=balance+?, debt=debt+? WHERE discordID=?", (credito, credito, discordID))
        con.commit()
    except mariadb.Error as e:
        print(f' Error fetching debt: {e}')
    
    cur.close()
    con.close()
def pagarCredito(discordID, cuanto):
    con = getConnection()
    cur = con.cursor()

    try:
        cur.execute("UPDATE Users SET balance = balance-?, debt=debt-? WHERE discordID=?", (cuanto,cuanto,discordID))
        con.commit()
    except mariadb.Error as e:
        print(f'Error in "pagarDeuda": {e}')
    cur.close()
    con.close()
def quitarDinero(discordID, cuanto):
    con = getConnection()
    cur = con.cursor()

    try:
        cur.execute("UPDATE Users SET balance = balance-? WHERE discordID=?", (cuanto,discordID))
        con.commit()
    except mariadb.Error as e:
        print(f'Error in "quitarDinero": {e}')
    cur.close()
    con.close()
def darDinero(discordID, cuanto):
    con = getConnection()
    cur = con.cursor()

    try:
        cur.execute("UPDATE Users SET balance = balance+? WHERE discordID=?", (cuanto,discordID))
        con.commit()
    except mariadb.Error as e:
        print(f'Error in "quitarDinero": {e}')
    cur.close()
    con.close()

def getEconomia(guildID = None):
    con = getConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT discordID, balance FROM Users")
        lst = cur.fetchall()
        if lst:
            return lst
    except mariadb.Error as e:
        print(f'Error in "getEconomia": {e}')
    cur.close()
    con.close()

def getInventarioPesca(discordID):
    con = getConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM fishingStats WHERE id=(SELECT id FROM Users WHERE discordID=?)", (discordID,))
        lst = cur.fetchall()
        if lst:
            return lst
    except mariadb.Error as e:
        print(f'Error in "getInventarioPesca": {e}')
    cur.close()
    con.close()
def getInfoPeces():
    con = getConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT Name, Price FROM fishingFishinfo")
        lst = cur.fetchall()
        if lst:
            return lst
    except mariadb.Error as e:
        print(f'Error in "getInfoPeces": {e}')
    cur.close()
    con.close()
def getFishingLevel(discordID):
    con = getConnection()
    cur = con.cursor()
    try:
        cur.execute("SELECT fishingLevel, currentXP, nextLevelXP FROM fishingStats WHERE id=(SELECT id FROM Users WHERE discordID=?)", (discordID,))
        lst = cur.fetchall()
        if lst:
            return lst
    except mariadb.Error as e:
        print(f'Error in "getFishingLevel": {e}')
    cur.close()
    con.close()
def addFishofTier(tier, discordID):
    con = getConnection()
    cur = con.cursor()
    subeNivel = False
    nivel = None
    try:
        cur.execute("SELECT fishingLevel, currentXP, nextLevelXP FROM fishingStats WHERE id=(SELECT id FROM Users WHERE discordID=?)", (discordID,))
        lst = cur.fetchall()
        if lst:
            sql = f"SELECT XP FROM fishingFishinfo WHERE Tier={tier}"
            cur.execute(sql)
            lst1 = cur.fetchall()
            for fLevel, curXP, nextXP in lst:
                curXP += lst1[0][0]
                if curXP >= nextXP:
                    fLevel += 1
                    curXP = 0
                    nextXP *= 1.05
                    subeNivel = True
                    nivel = fLevel
                cur.execute("UPDATE fishingStats SET fishingLevel = ?, currentXP = ?, nextLevelXP = ? WHERE id=(SELECT id FROM Users WHERE discordID=?)", (fLevel, curXP, nextXP, discordID))
        if tier == 0:
            sql = f"UPDATE fishingStats SET trash=trash+1 WHERE id=(SELECT id FROM Users WHERE discordID={discordID})"
        elif tier == 11:
            sql = f"UPDATE fishingStats SET llavesTesoro=llavesTesoro+1 WHERE id=(SELECT id FROM Users WHERE discordID={discordID})"
        elif tier == 12:
            sql = f"UPDATE fishingStats SET cofreTesoro=cofreTesoro+1 WHERE id=(SELECT id FROM Users WHERE discordID={discordID})"
        else:
            sql = f"UPDATE fishingStats SET fishTier{tier}=fishTier{tier}+1 WHERE id=(SELECT id FROM Users WHERE discordID={discordID})"
        cur.execute(sql)
        con.commit()
        return (subeNivel, nivel)
    except mariadb.Error as e:
        print(f'Error in "addFishofTier": {e}')
    cur.close()
    con.close()
def getPecesbyDifficulty(difficulty):
    con = getConnection()
    #esto se puede hacer mas facil con sql = "SELECT ...{0}" sabes?
    cur = con.cursor()
    try:
        sql = f"SELECT Tier, Name, XP, Price, Difficulty1 FROM fishingFishinfo WHERE {difficulty} !=0"
        cur.execute(sql)
        lst = cur.fetchall()
        if lst:
            return lst
    except mariadb.Error as e:
        print(f'Error in "getPecesbyDifficulty": {e}')
    cur.close()
    con.close()


def sellFish(discordID):
    con = getConnection()
    #esto se puede hacer mas facil con sql = "SELECT ...{0}" sabes?
    cur = con.cursor()
    try:
        listaInv = getInventarioPesca(discordID)
        listaPeces = getInfoPeces()
        dineroGanado = 0
        pecesTotales = 0
        basuraTotal = 0
        for  _, _, _, _, _, ftier1, ftier2, ftier3, ftier4, ftier5, ftier6, ftier7, ftier8, ftier9, ftier10, _, _, _, _, _, _, _, trash in listaInv:
            if trash > 0:
                dineroGanado += (listaPeces[0][1] * trash)
                basuraTotal += trash
                trash = 0
            if ftier1 > 0:
                dineroGanado += (listaPeces[1][1] * ftier1)
                pecesTotales += ftier1
                ftier1 = 0
            if ftier2 > 0:
                dineroGanado += (listaPeces[2][1] * ftier2)
                pecesTotales += ftier2
                ftier2 = 0
            if ftier3 > 0:
                dineroGanado += (listaPeces[3][1] * ftier3)
                pecesTotales += ftier3
                ftier3 = 0
            if ftier4 > 0:
                dineroGanado += (listaPeces[4][1] * ftier4)
                pecesTotales += ftier4
                ftier4 = 0
            if ftier5 > 0:
                dineroGanado += (listaPeces[5][1] * ftier5)
                pecesTotales += ftier5
                ftier5 = 0
            if ftier6 > 0:
                dineroGanado += (listaPeces[6][1] * ftier6)
                pecesTotales += ftier6
                ftier6 = 0
            if ftier7 > 0:
                dineroGanado += (listaPeces[7][1] * ftier7)
                pecesTotales += ftier7
                ftier7 = 0
            if ftier8 > 0:
                dineroGanado += (listaPeces[8][1] * ftier8)
                pecesTotales += ftier8
                ftier8 = 0
            if ftier9 > 0:
                dineroGanado += (listaPeces[9][1] * ftier9)
                pecesTotales += ftier9
                ftier9 = 0
            if ftier10 > 0:
                dineroGanado += (listaPeces[10][1] * ftier10)
                pecesTotales += ftier10
                ftier10 = 0
            cur.execute("UPDATE fishingStats SET fishTier1 = ?,fishTier2 = ?,fishTier3 = ?,fishTier4 = ?,fishTier5 = ?,fishTier6 = ?,fishTier7 = ?,fishTier8 = ?,fishTier9 = ?,fishTier10 = ?,trash = ? WHERE id=(SELECT id FROM Users WHERE discordID=?)", (ftier1, ftier2, ftier3, ftier4, ftier5, ftier6, ftier7, ftier8, ftier9, ftier10, trash, discordID))
            cur.execute("UPDATE Users SET balance = balance + ? WHERE discordID=?", (dineroGanado, discordID))
            con.commit()
            return (dineroGanado, basuraTotal, pecesTotales)
    except mariadb.Error as e:
        print(f'Error in "sellPeces": {e}')
    cur.close()
    con.close()

                