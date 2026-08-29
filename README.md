# aanhuispersonaltrainer.nl

Statische site over trainingsmateriaal bij personal training aan huis. Geen build-stap nodig:
alle HTML staat kant-en-klaar in de repo.

## Opnieuw genereren
`python3 bouw.py` schrijft alle pagina's, `sitemap.xml` en `robots.txt` opnieuw weg.
Teksten staan in `bouw.py`, opmaak in `blad/catalogus.css`.

## Interactief onderdeel
De materiaalkiezer op de homepage draait op vanilla JavaScript, ingesloten onderaan `index.html`
(gegenereerd uit `KIEZER_JS` in `bouw.py`). Geen externe scripts, geen cookies, niets wordt opgeslagen.

## Beeld
`beeld/` bevat negen foto's plus de animatie `gereedschap-loop` (webm, mp4, posterframe).
De animatie is 960x640 met harde veegovergangen. Afmetingen zijn bewust een veelvoud van 16
en er staan vaste keyframes in; zonder dat gaan sommige hardwarematige VP9-decoders strepen tonen.

## Opmaak insluiten bij handmatige upload naar Cloudflare
De dashboard-uploader van Cloudflare bewaart CSS soms als `application/octet-stream`, waarna de
browser de stylesheet weigert. Bij deployment via GitHub speelt dit niet. Doe je het toch handmatig,
sluit de opmaak dan eerst in de pagina's in.
