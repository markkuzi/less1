from time import sleep


def sleeping(time):
    for i in range(time, 0, -1):
        print(f'{i}')
        sleep(1)


class TrafficLight:
    __color = 'red'

    def running(self):
        while True:
            print(self.__color)
            sleeping(7)
            self.__color = 'yellow'
            print(self.__color)
            sleeping(2)
            self.__color = 'green'
            print(self.__color)
            sleeping(5)
            self.__color = 'red'


first_traffic_light = TrafficLight()
first_traffic_light.running()
