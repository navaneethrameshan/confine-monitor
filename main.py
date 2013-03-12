from client.main import main
import os

path= os.path.join(os.path.dirname(__file__), 'log_shelf.db')
os.remove(path)
main.main()
