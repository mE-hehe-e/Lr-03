# Выполнение запросов к базе данных "Пиццерия"
# Гусева Анастасия

from sqlmodel import *
from models import *

#Вывод клиентов и их номера заказов
def Cl_ord():
    with Session(engine) as session:
        print("КЛИЕНТ, НОМЕРА И ДАТЫ ИХ ЗАКАЗОВ")
        x = select(Client)
        result1 = session.exec(x)
        for cl in result1:
            print("\n",cl.full_name)
            y=select(Order).where(cl.id_client==Order.id_client)
            result2=session.exec(y)
            for ord in result2:
                print(" ",ord.id_order,"\n",ord.ord_date)

#Меню
def Men_Piz():
    with Session(engine) as session:
        print("МЕНЮ ПИЦЦЕРИИ")
        x = select(Menu)
        result1 = session.exec(x)
        for piz in result1:
            print("\n",piz.name,piz.price,"\n",piz.comp)

#Cl_ord()
Men_Piz()