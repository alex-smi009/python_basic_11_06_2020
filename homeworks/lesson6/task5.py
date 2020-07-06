'''
����������� ����� Stationery (������������ ��������������). ���������� � ��� ������� title (��������) � ����� draw (���������).
����� ������� ��������� ������� ���������.� ������� ��� �������� ������ Pen (�����), Pencil (��������), Handle (������).
� ������ �� ������� ����������� ��������������� ������ draw. ��� ������� �� ������� ������ ������ �������� ���������� ���������.
������� ���������� ������� � ���������, ��� ������� ��������� ����� ��� ������� ����������.
'''
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'������ ��������� {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'�� ����� {self.title}. ������ ��������� ������'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'�� ����� {self.title}. ������ ��������� ����������'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'�� ����� {self.title}. ������ ��������� ��������'


pen = Pen('�����')
pencil = Pencil('��������')
handle = Handle('������')
print(pen.draw())
print(pencil.draw())
print(handle.draw())