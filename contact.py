class Contact:
    count_id=0
    def __init_contact__(self, personName, phone_number, group):
        count_id+=1
        self.current=count_id
        self.name = personName
        self.number = phone_number
        self.group = group
#Заготовка под ооп, хотел перевети и сделать с объектоми класса, давать в кортеж( если он там нужен вообще) обьекты класса Сontact