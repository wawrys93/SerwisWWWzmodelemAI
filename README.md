# Serwis WWW z modelem AI


Serwis WWW oparty na Flasku, który wykorzystuje model AI do przewidywań na podstawie przesłanych danych. Całość została skonteneryzowana przy użyciu Dockera.

---

## 1. Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz zainstalowane:
- **Docker**
- **Python 3.9 lub nowszy** (jeśli chcesz uruchomić lokalnie bez Dockera)

---

## 2. Instalacja lokalna (opcjonalna)

1. Sklonuj repozytorium z GitHuba:
```
git clone https://github.com/username/ai-web-service.git
cd ai-web-service
```
2. Zainstaluj zależności:
```
pip install -r requirements.txt
```
3. Uruchom aplikację:
```
python app.py
```
4. Odwiedź stronę testową w przeglądarce:
```
http://localhost:5000
```

---

## 3. Budowa i uruchomienie Dockera

1. Zbuduj obraz Dockera:
```
docker build -t ai-web-service .
```
2. Uruchom kontener:
```
docker run -d -p 5000:5000 ai-web-service
```
3. Sprawdź działające kontenery:
```
docker ps
```

---

## 4. Testowanie aplikacji

1. Otwórz przeglądarkę:
```
http://localhost:5000
```
Powinieneś zobaczyć komunikat:
```
AI Prediction Service is running!
```

2. Przetestuj predykcję za pomocą `curl`:
```
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"values": [5, 6, 7]}'
```
Odpowiedź:
```
{"predictions":[5.0,6.0,7.0]}
```

---

## 5. Zatrzymanie kontenera

Zatrzymaj kontener:
```
docker stop <CONTAINER_ID>
```
Usuń kontener:
```
docker rm <CONTAINER_ID>
```

---

## 6. Pliki w projekcie

- **app.py** - kod
- **Dockerfile** - konfiguracja Dockera
- **requirements.txt** - treść zadania

---

