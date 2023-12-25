# Создание и заполнение базы данных "Пиццерия"
# Гусева Анастасия

from sqlmodel import Field, SQLModel, create_engine, Session
from datetime import date, time

class Client(SQLModel, table=True):
    id_client: str = Field(default=None, primary_key=True)  #size 6
    full_name: str                                          #size 30
    reg_date: date

class Payment(SQLModel, table=True):
    id_pay: int = Field(default=None, primary_key=True)
    type: str                                               #size 8

class Menu(SQLModel, table=True):
    id_menu: str = Field(default=None, primary_key=True)    #size 4
    name: str                                               #size 15
    comp: str                                               #size 100
    price: float = Field(default=0)                         #size 5

class Order(SQLModel, table=True):
    id_order: str = Field(default=None, primary_key=True)                         #size 8
    id_client: str = Field(default=None, foreign_key="client.id_client")          #size 6
    id_pay: int = Field(foreign_key="payment.id_pay")                             #size 8
    ord_date: date
    ord_time: time
    total: float = Field(default=0)                         #size 4

class Content(SQLModel, table=True):
    id_cont: str = Field(default=None, primary_key=True)    #size 10
    id_order: str = Field(foreign_key='order.id_order')     #size 8
    id_menu: str = Field(foreign_key="menu.id_menu")        #size 4

Client_1=Client(id_client="000001",full_name="Васильева Дарья Михайловна",reg_date=date(2020,4,5))
Client_2=Client(id_client="000002",full_name="Чекалова Ольга Ростиславовна",reg_date=date(2022,10,3))
Client_3=Client(id_client="000003",full_name="Снежко Евгений Олегович",reg_date=date(2022,7,7))
Client_4=Client(id_client="000004",full_name="Овощин Данила Сергеевич",reg_date=date(2021,12,1))

Payment_1=Payment(id_pay=1,type="Наличные")
Payment_2=Payment(id_pay=2,type="Карта")
Payment_3=Payment(id_pay=3,type="СБП")

Pizza_1=Menu(id_menu="0001",name="Три сыра",comp="Моцарелла, сыры чеддер, пармезан, соус альфредо", price=520.50)
Pizza_2=Menu(id_menu="0002",name="Пепперони",comp="Пепперони, моцарелла, томаты, томатный соус", price=615.50)
Pizza_3=Menu(id_menu="0003",name="Гавайская",comp="Цыпленок, ананасы, моцарелла, соус альфредо", price=540.50)
Pizza_4=Menu(id_menu="0004",name="Маргарита",comp="Моцарелла, томаты, итальянские травы, томатный соус", price=480.50)
Pizza_5=Menu(id_menu="0005",name="Ветчина и сыр",comp="Ветчина, моцарелла, соус альфредо", price=490.50)

Order_1=Order(id_order="00000001",id_client="000001",id_pay=3,ord_date=date(2023,12,11),ord_time=time(17,44))
Order_2=Order(id_order="00000002",id_client="000002",id_pay=1,ord_date=date(2023,11,12),ord_time=time(12,32))
Order_3=Order(id_order="00000003",id_client="000003",id_pay=2,ord_date=date(2023,12,6),ord_time=time(15,18))
Order_4=Order(id_order="00000004",id_client="000004",id_pay=3,ord_date=date(2023,12,4),ord_time=time(9,28))

Cont_1=Content(id_cont="0000000001",id_order="00000001",id_menu="0001")
Cont_2=Content(id_cont="0000000002",id_order="00000002",id_menu="0003")
Cont_3=Content(id_cont="0000000003",id_order="00000002",id_menu="0004")
Cont_4=Content(id_cont="0000000004",id_order="00000002",id_menu="0002")
Cont_5=Content(id_cont="0000000005",id_order="00000003",id_menu="0004")
Cont_6=Content(id_cont="0000000006",id_order="00000003",id_menu="0005")
Cont_7=Content(id_cont="0000000007",id_order="00000004",id_menu="0002")

engine = create_engine("sqlite:///database.db")
if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    mas=[Client_1,Client_2,Client_3,Client_4,Payment_1,Payment_2,Payment_3,Pizza_1,Pizza_2,Pizza_3,Pizza_4,Pizza_5,Order_1,Order_2,Order_3,Order_4,Cont_1,Cont_2,Cont_3,Cont_4,Cont_5,Cont_6,Cont_7]
    with Session(engine) as session:
        for i in mas:
            session.add(i)
        session.commit()