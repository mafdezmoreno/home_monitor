import board
import adafruit_dht
import datetime


class Data:
    
    temp = 0
    humi = 0
    now = ""

    def read_sensor(self):
        try:
            dhtDevice = adafruit_dht.DHT11(board.D17)
            self.temp = dhtDevice.temperature
            self.humi= dhtDevice.humidity
            print('Temp: {0:0.1f}* C  Humidity: {1:0.1f} %'.format(self.temp, self.humi))


        except Exception as e:
            print ('error '+str(e))

        except Exception as error:
            raise error

        dhtDevice.exit()

    def get_formated_temp(self):
        t ='{0:0.1f}'.format(self.temp)
        return t

    def get_formated_humi(self):
        return self.humi

    def update_time(self):
        temp = datetime.datetime.now()
        self.now = temp.strftime("%d-%m-%Y %H:%M")
        print(self.now)

    def get_time_string(self):
        return self.now
