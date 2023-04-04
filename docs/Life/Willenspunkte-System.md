---
title: "Willenspunkte-System"
author: Emanuel Regnath
date: "2022-12-13"
lang: de
share: true
category: Life
---
👨‍🔬 F. Wolff & E. Regnath · 📆 Dec. 2022 ·  🧪 Entwurf v1.1

Willenspunkte sind eine Skala, mit der Personen ihre Vorlieben und Abneigungen zum Ausdruck bringen können. Das Willenspunkte-System hilft bei der Entscheidungsfindung innerhalb von Gruppen und ist besonders gut für zwei Arten von Abstimmungen geeignet:

1. Angebot für eine Person, z.B. “Wer isst das letzte Kuchenstück?”
2. Auswahl für eine Gruppe, z.B. “Was wollen wir spielen? A oder B?”

| Punkte | Generelle Bedeutung                                   | Beispiel Kuchen                                |
|:------:| ----------------------------------------------------- | ---------------------------------------------- |
| **4** | 😍 Yeah! Ich will das unbedingt!<br>Sonst bin ich traurig!  | Viel Hunger und Lieblingskuchen!                |
| **3** | 😁 Jaa, ich hab schon ziemlich Bock darauf.              | Hunger *oder* mag diesen Kuchen sehr.       |
| **2** | 😃 Jo, ich hätte Lust aber es ist mir nicht so wichtig.  | Generell Appetit auf Kuchen.                    |
| **1** | 🙂 Ok. Wäre dabei aber auch Ok wenn nicht.               | Wenn ihn sonst keiner will...                      |
| **-1** | 😐 Hm. Eher nicht aber wäre auch dabei.                  | Eigentlich satt aber bevor er weggeworfen wird... |
| **-2** | 🙁 Ne, bin dagegen aber zur Not lass ich mich überreden. | Bin voll aber Oma ist sonst traurig.            |
| **-3** | ☹ Nein, das muss jetzt echt nicht sein.                 | Platz gleich. Entweder morgen oder Müll.       |
| **-4** | 😭 Niemals! Das wäre das schlimmste. Ich weigere mich!   | Allergisch auf Kuchen!                         |

> [!important] Wichtig:
> Die Willenspunkte spiegeln keine Entscheidung wider, sondern sind nur ein Ausdruck der persönlichen Einstellung zur Frage! 

Auf die Zahl 0 wurde verzichtet, um Enthaltungen zu vermeiden.

### Vorteile: 
* Durch eine klare Zahlenzuweisung kann besser unterschieden werden. 
* Alle wissen, wie sehr eine Person etwas will und so ist es für eine 2 auf Kuchen auch leicht zu akzeptieren, wenn die Person mit 3 Willenspunkten den Kuchen bekommt.
* Zahlen sind neutral und man bevorzugt keine.



## Analysierte Varianten
Als Referenz sind hier weitere Varianten aufgelistet, die wieder verworfen wurden.

> [!example]- Option A: 1..4
> Das ursprüngliche System: Wer isst das letzte Stück?
> * 1: Zur Not, bevor es weggeschmissen wird, esse ich es
> * 2: Ich würde es essen, überlasse es aber auch gern anderen
> * 3: Ich hab schon ziemlich Bock drauf oder hab Hunger
> * 4: Ich will es! Es ist mein Liebling, macht mich sehr glücklich
> 
> → Getestet, funktioniert sehr gut. Aber: nicht geeignet um genauere Abstimmungen vorzunehmen

> [!example]- Option B: -3 .. 3 (ohne 0)
> Für z.B. Wollen wir Spiel X spielen?
> * -3: Stark dagegen ()
> * -2: Dagegen (Will Nicht essen)
> * -1: Eher dagegen aber OK  (Zur Not essen)
> * 1: Eher dafür aber Ok falls nicht (Leichter Appetit)
> * 2: Dafür (Will essen)
> * 3: Stark dafür ()
> 
> Probleme:
> * Nur 3 positive Möglichkeiten sind zu wenig (Tendenz zur Mitte)
> * -1 schwierig. Wenn es bedeutet ("will nicht"), dann sind -2/-3 fast egal. Wenn -1 als erstes positives gilt ("Zur Not esse ich") ist der Zahlenwert nicht intuitiv & großer Sprung von 1 zu -1

> [!example]- Option C: -4, -2, 0,1,2,3
Mittelwert ist 0 und -4 in einer Zweierabstimmung ist eine Art "Veto". 4 "positive" Werte, 0 = bevor es weggeschmissen wird. → Warum nicht -3..3?
> * -4: Gar kein Bock (ich bin raus/dumme Idee)
> * -2: Dagegen
> * 0: Mir egal, bin mit beidem einverstanden
> * 1: Eher dafür aber Ok falls nicht
> * 2: Dafür
> * 3: Stark dafür
> 
> → Vorteil: Liefert leichter ein eindeutiges Ergebnis bei gerader Anzahl an Personen. Respektiert, dass es schlimmer ist, etwas zu machen was man nicht will, als etwas nicht zu machen was man will.


### Oder Ganz Anders?
* -1..2 (-1 Dagegen, 0 Eher nicht aber Ok, 1 Dafür, 2 Stark dafür)
* **-4, -2, 0, 1, 2, 3** (avg. 0, 2–1–3)
* -4, -2, -1, 1, 2 4 
* **-6, -3, -1, 1, 2, 3, 4**  (avg 0, 3–4)
* -8 -2 1 2 3 4  (avg 0, 4 positive Optionen, 6 gesamt)
* -5 -1 1 2 3 (avg0, 3 positive)
* -5 -3, -1 1 2 3 (- 0.5!, 3–3)
* -3, -1, 1, 3 
* -10, -3, -1, 1, 2, 4, 7 (nonlin)
* -7, -3, -1, 1, 2, 3, 5 (all prime, avg0, 3–4, nonlin)

