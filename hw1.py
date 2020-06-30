from time import sleep


class TrafficLight:
    color = ['Красный', 'Желтый', 'Зеленый']
    time = [7, 2, 4]

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.color[i]}')
            sleep(TrafficLight.time[i])
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
