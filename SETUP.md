# 🚀 Guida Rapida di Setup - MyStory

## ⚡ In 3 passaggi

### 1️⃣ Apri la cartella in VS Code
```
cd c:\Users\PC_DELL\Desktop\Mystory
code .
```

### 2️⃣ Installa dipendenze (primo avvio solamente)
Apri il terminale integrato (Ctrl+`) e esegui:
```
npm install
```

### 3️⃣ Avvia il server
```
npm run dev
```

✅ Pronto! Visita **http://localhost:5173/** nel browser

---

## 🎮 Come iniziare

### Test veloce senza login
1. Muovi i slider per cambiare gli anni
2. Clicca sui badge colorati per attivare/disattivare aree geografiche
3. Ruota il globo col mouse e clicca su un evento

### Test con registrazione
1. Clicca "Registrati"
2. Inserisci nome, email e password
3. Accedi e aggiungi un evento personale nella sezione "La tua mappa personale"
4. Ricarica la pagina: il tuo evento sarà ancora lì!

---

## 📝 Modifiche comuni

### Aggiungere un nuovo evento storico
Apri `src/data/events.js` e aggiungi un oggetto nell'array `historicalEvents`:

```javascript
{
  id: 'evt-NUMERO',
  title: 'Nome dell\'evento',
  description: 'Descrizione breve',
  startYear: -1000,
  endYear: -900,
  yearLabel: '1000/900 a.C.',
  lat: 30.0,      // latitudine
  lng: 35.0,      // longitudine
  region: 'africaMiddleEast', // scegli da: africaMiddleEast, europe, mediterranean, asiaOceania, americas
  wikipediaUrl: 'https://it.wikipedia.org/wiki/...'
}
```

### Cambiare colore di un'area
In `src/data/events.js`, modifica `regionConfig`:
```javascript
europe: {
  id: 'europe',
  label: 'Europa',
  color: '#FF0000'  // cambia il colore hex
}
```

### Cambiare il range di anni
In `src/App.jsx` modifica:
```javascript
const minYear = -10000;  // anno minimo
const maxYear = -500;    // anno massimo
```

---

## 🛠️ Comandi utili

| Comando | Effetto |
|---------|---------|
| `npm run dev` | Avvia server di sviluppo |
| `npm run build` | Compila per produzione (cartella `dist/`) |
| `npm run preview` | Visualizza la build di produzione |
| `npm audit` | Controlla vulnerabilità |
| `npm audit fix` | Correggi vulnerabilità |

---

## ✨ Funzionalità principali

✅ Mappamondo 3D interattivo con zoom/rotazione  
✅ 5 colori per distinguere aree geografiche  
✅ Filtri temporali (10000 a.C. - 2026 d.C.)  
✅ 5 epoche storiche predefinite (Antichità, Tardo Antico, Medioevo, Età Moderna, Contemporanea)  
✅ Accesso libero senza registrazione  
✅ Registrazione opzionale per mappe personali  
✅ Salvataggio dati nel browser (localStorage)  
✅ Link Wikipedia per approfondimenti  
✅ 93 eventi storici di default  
✅ Oltre 50 eventi storici di default  

---

## ❓ Risoluzione problemi

**Il dev server non parte?**
- Verifica di avere Node.js installato: `node --version`
- Cancella `node_modules` e rifai `npm install`

**Gli eventi non appaiono?**
- Controlla che gli anni nell'evento siano dentro il range impostato
- Verifica che l'area geografica (`region`) sia corretta

**I dati dell'utente non si salvano?**
- Il browser deve avere localStorage abilitato
- Controlla che non sia in modalità "incognito"

**Il globo non si vede?**
- Ricarica la pagina (Ctrl+Shift+R)
- Verifica la connessione internet (scarica risorse da CDN)

---

## 📦 Il progetto è pronto all'uso!

Non serve configurare altro. Inizia a esplorare e personalizzare come preferisci.

Buon divertimento con MyStory! 🌍📚
