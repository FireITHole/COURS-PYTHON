from datetime import datetime

now = datetime.now()
date_de_naissance = datetime(2002, 6, 11)

diff = now - date_de_naissance
print(diff.days // 365.25)
