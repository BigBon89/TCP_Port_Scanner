# TCP_UDP_Port_Scanner

## Данный скрипт позволяет определить открытые и закрытые TCP/UDP порты в заданном диапазоне.

## Запуск скрипта
```
python3 main.py <host> <ports>
```
Пример ports 10,20,30,40-60
## Пример запуска
```
>python3 main.py localhost 123,135,445,5000,5040,7000,60925 
Scanning ports...
port 123|tcp closed
port 135|tcp closed
port 445|tcp closed
port 5000|tcp opened
port 5040|tcp closed
port 7000|tcp opened
port 60925|tcp opened
```