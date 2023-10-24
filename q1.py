class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no
    
    def entry_show(self,id,movie_name,time):
        info=(id, movie_name, time)
        self._show_list.append(info)

        seat=[]
        for i in range(self._rows):  
            row=[]
            for j in range(self._cols):
                row.append('free')
            seat.append(row)
        self._seats[id]=seat
    
    def book_seats(self,id,list):
        if id in self._seats:
            seats=self._seats[id]
            for seat in list:
                row,col=seat
                if 0<=row<self._rows and 0<=col< self._cols:
                    if seats[row][col]=="free":
                        seats[row][col]="booked"
                    else:
                        print(f'seat {row}, {col} is already booked')
                else:
                    print(f'invalid seat {row},{col}')
        else:
            print(f'id {id} not found')
    
    def view_show_list(self):
        print(f'HALL NO {self._hall_no} all running show')
        for show in self._show_list:
            # print(f'{show.id} {show.movie_name} {show.time}')
            print(show)

    def view_available_seats(self,id):
        print(f'{id} available seats:')
        seat=self._seats[id]  
        for se in seat:
            print(se)


class Star_Cinema:
    _hall_list=[]

    def entry_hall(self,hall):
        self._hall_list.append(hall)
    
ob1=Hall(10,15,1)
ob2=Hall(8,10,2)

chinema=Star_Cinema()

chinema.entry_hall(ob1)
chinema.entry_hall(ob2)

ob1.entry_show('show 1','Pathaan','10:00 AM')
ob2.entry_show('show 2','Extraction 2','3:00 PM')
ob2.entry_show('show 3','jailer','8:00 PM')

# print(ob2.seats)
ob2.book_seats('show 2',[(0,0),(0,1),(1,2)])
ob2.view_show_list()
ob2.view_available_seats('show 2')
ob2.view_available_seats('show 3')
# print(ob2.seats)