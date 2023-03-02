import os
import time
for hora  in range(24):
    for minuto  in range(60):
        for segundos in range(60):
            os.system("cls")
            print(f'{hora}:{minuto}:{segundos}')
            time.sleep(1)
   