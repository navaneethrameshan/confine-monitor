from client.main import main
import os

list_delete= ['log_shelf.db.dat', 'log_shelf.db.dir', 'log_shelf.db.bak']

for value in list_delete:
    path= os.path.join(os.path.dirname(__file__),value )

    if(os.path.exists(path)):
        os.remove(path)
        print("Removing: " + path)

main.main()
