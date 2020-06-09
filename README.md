# Web Scraper ve Rest API

#### [cars.com](https://www.cars.com) üzerinden çekilen araç verilerinin MySQL veritabanında saklanması ve bu verilerin rest api aracalığı ile JSON formatında sunulması için hazırlanmış olan Python uygulaması.

---
### Kullanılan Kütüphaneler:
- Flask
```shell
$ pip install Flask
```
- flask_restful
```shell
$ pip install flask-restful
```
- Peewee ORM
```shell
$ pip install peewee
```
- pymsql
```shell
$ pip install PyMySQL
```
- BeautifulSoup4
```shell
$ pip install beautifulsoup4
```
- simplejson: Veritabanından okunan Decimal veri tipini JSON nesnesine dönüştürmek için gerekli.
```shell
$ pip install simplejson
```
---
### Kullanımı:

##### settings.py dosyası içerisinde veritabanına bağlanmak için gerekli olan MySQL Server parametreleri bulunmaktadır.
##### Verileri çekmeden önce models.py modülü kullanılarak veritabanı ve tablo oluşturulması gerekiyor.
> Komut satırından aşağıdaki komut çalıştırılarak tablo yapısı oluşturuluyor:
```shell
$ python models.py
```
---
##### Daha sonra cars.com üzerinden araç verilerini çekmek için main.py modülü kullanılıyor.
> Komut satırından aşağıdaki komut çalıştırılarak araç verileri çekiliyor ve MySQL veritabanına yazdırılıyor.
```shell
$ python main.py
```
---
##### Veriler MySQL veritabanına aktarıldıktan sonra api.py modülü aracılığı ile JSON formatında sunulabilir hale getirilmektedir.
> Komut satırından aşağıdaki komut çalıştırılarak API başlatılıyor. 
```shell
$ python api.py
```

---
##### Veriler marka, dış renk, iç renk, yıl ve vites türüne göre filtrelenebilmektedir. Filtrelemeler çoklu şekilde sorgulanabilmektedir.
##### Örnek sorgular aşağıdaki gibidir:

- xx.com/cars/list : Araç listesinin tümü
- xx.com/cars/list/?extcolor=black : Siyah renkli araçlar
- xx.com/cars/list/?brand=BMW&extcolor=black : Siyah renkli BMW araçlar
- xx.com/cars/list/?trans=automatic&brand=Ford&year=2018: : Otomatik vites türündeki 2018 yılına ait Ford marka araçlar.

---
##### Uygulama localhost üzerinde test edilmiştir. 
