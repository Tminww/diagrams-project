from diagrams import Diagram, Edge
from diagrams.onprem.client import User
from diagrams.onprem.network import Nginx
#from diagrams.programming.framework.Fastapi import FastAPI
from diagrams.onprem.database import PostgreSQL
#from diagrams.onprem.analytics import Parser
from diagrams.onprem.compute import Server
#from diagrams.onprem.storage import StaticFiles
#from diagrams.security import SSL

with Diagram("Client Web App Interaction", show=False):
    # Клиентская часть
    user = User("Client")

    # Веб-сервер
    nginx = Nginx("Web Server")

    # Uvicorn (ASGI сервер)
    uvicorn = Server("Uvicorn")

    # FastAPI приложение
    fastapi = PostgreSQL("FastAPI")

    # База данных
    postgres = PostgreSQL("Postgres")

    # Парсер
    parser = PostgreSQL("Parser")

    # Статические файлы
    static_files = PostgreSQL("Frontend Static Files")

    # SSL
    ssl = PostgreSQL("SSL")
    
    pravoGOV = PostgreSQL("PRAVOGOV")

    # Связи между компонентами
    user >> Edge(color="darkgreen") >> nginx
    nginx >> Edge(color="blue") >> uvicorn
    uvicorn >> Edge(color="black") >> fastapi
    fastapi >> Edge(color="brown") >> postgres
    fastapi >> Edge(color="orange") >> parser
    nginx >> Edge(color="purple") >> static_files
    user >> Edge(color="red") >> ssl >> nginx
    parser >> Edge(color="grey") >> pravoGOV
