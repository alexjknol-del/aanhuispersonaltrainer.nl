#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bouwt aanhuispersonaltrainer.nl — invalshoek: materiaal en apparatuur."""
import os, html, re

BASIS = os.path.dirname(os.path.abspath(__file__))
DOMEIN = "https://aanhuispersonaltrainer.nl"

MENU = [
    ("index.html", "Start"),
    ("wat-neemt-de-trainer-mee.html", "In de kofferbak"),
    ("zelf-aanschaffen.html", "Zelf kopen"),
    ("de-miskopen.html", "Miskopen"),
    ("aanbieders.html", "Aanbieders"),
    ("artikelen.html", "Artikelen"),
]

# derde volgorde in de reeks: geen van de zustersites hanteert deze
PARTIJEN = [
    dict(naam="LET'S DO IT Personal Training", kleur="#c2a04b", url="https://letsdoitpt.nl/",
         punten=["Meer dan tachtig vrouwelijke trainsters, actief sinds 2007",
                 "Neemt het materiaal mee dat bij jouw programma hoort",
                 "Verdieping rond zwangerschap, herstel na de bevalling en overgang",
                 "Eigen app met bewegingsvideo's voor tussen de sessies"]),
    dict(naam="YourHealth Personal Training", kleur="#ef7d1a", url="https://yourhealthpt.nl/",
         punten=["Ruim honderd trainers door heel Nederland",
                 "Strippenkaarten die je vooruit koopt, ruime geldigheid",
                 "Medical trainers voor wie met een blessure of aandoening traint",
                 "Ook boksen, waarvoor de trainer eigen handschoenen en pads meebrengt"]),
    dict(naam="Jouw Personal Trainer aan Huis", kleur="#1e7a4e", url="https://www.jouwpersonaltraineraanhuis.nl/",
         punten=["Trainers met een achtergrond in fysiotherapie of leefstijlcoaching",
                 "Werkt veel met lichaamsgewicht, banden en lichte gewichten",
                 "Gericht op kracht, balans en mobiliteit, ook op latere leeftijd",
                 "Partner of huisgenoot mag zonder meerkosten meedoen"]),
]


def blok_partijen(notities=None):
    notities = notities or {}
    uit = ['<div class="g-artikelen">']
    for i, p in enumerate(PARTIJEN, 1):
        punten = "".join(f"<li>{html.escape(x)}</li>" for x in p["punten"])
        n = notities.get(p["naam"], "")
        extra = f'<p>{html.escape(n)}</p>' if n else ""
        uit.append(f"""
      <article class="g-artikel">
        <div class="g-artikel__kop">
          <span class="g-artikel__nr" style="background:{p['kleur']};color:#111310">{i:02d}</span>
          <h3 style="margin:0">{html.escape(p['naam'])}</h3>
        </div>
        <div class="g-artikel__body">
          {extra}
          <ul style="list-style:none;margin:0 0 16px;padding:0;font-size:.94rem;color:#3a3d35">{punten}</ul>
          <a class="g-knop g-knop--leeg" style="margin-top:auto;align-self:flex-start;font-size:.8rem;padding:10px 16px" href="{p['url']}" rel="noopener">Naar de website</a>
        </div>
      </article>""")
    uit.append("</div>")
    return "".join(uit).replace("<li>", '<li style="padding-left:18px;position:relative;margin-bottom:7px">')


def pagina(bestand, titel, omschrijving, inhoud, diepte=0, extra_head="", extra_body=""):
    op = "../" * diepte
    nav = ""
    for pad, label in MENU:
        actief = ' aria-current="page"' if pad == bestand else ""
        nav += f'<a href="{op}{pad}"{actief}>{html.escape(label)}</a>'
    canoniek = DOMEIN + "/" + ("" if bestand == "index.html" else bestand[:-5])
    doc = f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titel)}</title>
<meta name="description" content="{html.escape(omschrijving)}">
<link rel="canonical" href="{canoniek}">
<link rel="stylesheet" href="catalogus.css">
{extra_head}
</head>
<body>

<header class="g-balk">
  <div class="g-baan g-balk__in">
    <a class="g-merk" href="{op}index.html"><i></i>aanhuispersonaltrainer</a>
    <nav class="g-nav">{nav}</nav>
  </div>
</header>

{inhoud}

<section class="g-slot">
  <div class="g-baan">
    <h2>materiaal is het middel, niet het doel</h2>
    <p>Geen van de drie aanbieders hieronder verwacht dat je iets in huis hebt. Ze komen met wat nodig is en kijken pas daarna of aanschaffen zin heeft.</p>
    <div class="g-knoppen" style="justify-content:center">
      <a class="g-knop g-knop--leeg" href="{op}aanbieders.html">Naar de aanbieders</a>
      <a class="g-knop g-knop--leeg" href="{op}zelf-aanschaffen.html">Wat je zelf zou kopen</a>
    </div>
  </div>
</section>

<footer class="g-voet">
  <div class="g-baan">
    <div class="g-voet__kol">
      <div>
        <h4>aanhuispersonaltrainer.nl</h4>
        <p>Over het materiaal bij training aan huis: wat de trainer meebrengt, wat je zelf zou aanschaffen, wat je beter laat staan en hoe lang het meegaat.</p>
      </div>
      <div>
        <h4>Pagina's</h4>
        <p><a href="{op}wat-neemt-de-trainer-mee.html">In de kofferbak</a><br>
        <a href="{op}zelf-aanschaffen.html">Zelf aanschaffen</a><br>
        <a href="{op}de-miskopen.html">Miskopen</a><br>
        <a href="{op}aanbieders.html">Aanbieders</a><br>
        <a href="artikelen.html">Artikelen</a></p>
      </div>
      <div>
        <h4>Aanbieders</h4>
        <p><a href="https://letsdoitpt.nl/" rel="noopener">LET'S DO IT</a><br>
        <a href="https://yourhealthpt.nl/" rel="noopener">YourHealth</a><br>
        <a href="https://www.jouwpersonaltraineraanhuis.nl/" rel="noopener">Jouw Personal Trainer aan Huis</a></p>
      </div>
    </div>
    <div class="g-voet__slot">aanhuispersonaltrainer.nl — onafhankelijke wegwijzer, verkoopt zelf niets.</div>
  </div>
</footer>
{extra_body}
</body>
</html>
"""
    # interne verwijzingen zonder .html: Cloudflare Pages serveert die vorm en
    # stuurt .html met een 308 door, wat anders elke klik een omweg geeft
    doc = re.sub(r'href="([a-z0-9\-]+)\.html"',
                 lambda m: 'href="/"' if m.group(1) == "index" else 'href="%s"' % m.group(1), doc)
    pad = os.path.join(BASIS, bestand)
    os.makedirs(os.path.dirname(pad) or ".", exist_ok=True)
    open(pad, "w", encoding="utf-8").write(doc)
    return bestand


# ------------------------------------------------------- de materiaalkiezer
KIEZER_JS = """
<script>
(function(){
  var kaart = {
    band:   {label:'weerstandsbanden', doet:['trekbewegingen voor je rug','schouders zonder gewicht te hoeven tillen','opwarmen van heupen en schouders']},
    gewicht:{label:'halters of een kettlebell', doet:['zwaarder worden in benen en rug','tillen met techniek','romp stabiel houden onder belasting']},
    mat:    {label:'een mat', doet:['alles op de grond zonder pijnlijke knieën','rompoefeningen','mobiliteit en rekwerk']},
    lussen: {label:'een ophangsysteem', doet:['optrekken met je eigen gewicht','moeilijkheid regelen door je voeten te verzetten','trekwerk zonder gewichten']},
    bank:   {label:'een verhoging of stevige stoel','doet':['opstappen en uitvalspassen','opdrukken op hoogte','triceps en heupbruggen']},
    ruimte: {label:'drie bij drie meter of meer', doet:['verplaatsingen en korte sprints','circuits met meerdere posten','oefeningen in de lengte']}
  };
  var advies = [
    {mist:'gewicht', tekst:'Zonder enige weerstand loop je na een week of zes vast. Dit is het eerste dat de moeite van aanschaffen waard is: één verstelbare halterset of één kettlebell.'},
    {mist:'mat', tekst:'Een mat is het goedkoopste dat het meeste verschil maakt. Zonder mat slaat de helft van het grondwerk over, ook als je het niet doorhebt.'},
    {mist:'band', tekst:'Banden vullen precies het gat dat gewichten thuis laten vallen: trekbewegingen. Ze kosten weinig en nemen geen ruimte in.'},
    {mist:'lussen', tekst:'Een ophangsysteem is de goedkoopste manier om trekwerk toe te voegen als er geen rek in huis is. Niet noodzakelijk, wel handig.'},
    {mist:'bank', tekst:'Een stevige stoel of de onderste traptrede doet hetzelfde werk. Hier hoef je niets voor te kopen.'},
    {mist:'ruimte', tekst:'Met minder ruimte kan bijna alles nog; alleen verplaatsingen en sprints vallen af. Die vervang je door werk op de plaats.'}
  ];
  var vinkjes = document.querySelectorAll('.g-kiezer input[type=checkbox]');
  var lijst = document.getElementById('g-kan');
  var tip = document.getElementById('g-tip');
  if(!vinkjes.length || !lijst || !tip) return;

  function ververs(){
    var heeft = [];
    vinkjes.forEach(function(v){ if(v.checked) heeft.push(v.value); });
    var kan = [];
    heeft.forEach(function(k){ if(kaart[k]) kaart[k].doet.forEach(function(d){ if(kan.indexOf(d)<0) kan.push(d); }); });
    lijst.innerHTML = '';
    if(!kan.length){
      var li = document.createElement('li');
      li.textContent = 'Vink hierboven aan wat je in huis hebt. Ook niets aanvinken is een antwoord: met alleen je lichaamsgewicht en een stoel kun je al beginnen.';
      lijst.appendChild(li);
    } else {
      kan.slice(0,6).forEach(function(d){
        var li = document.createElement('li'); li.textContent = d; lijst.appendChild(li);
      });
    }
    var gekozen = null;
    for(var i=0;i<advies.length;i++){
      if(heeft.indexOf(advies[i].mist)<0){ gekozen = advies[i]; break; }
    }
    tip.innerHTML = gekozen
      ? '<strong>Eerst dit</strong>' + gekozen.tekst
      : '<strong>Eerst dit</strong>Je hebt alles wat een trainer thuis nodig heeft. Koop voorlopig niets meer bij; variatie zit vanaf hier in de oefeningen, niet in nieuwe spullen.';
  }
  vinkjes.forEach(function(v){ v.addEventListener('change', ververs); });
  ververs();
})();
</script>
"""

KIEZER = """
<div class="g-kiezer">
  <div class="g-kiezer__kop">
    <h3>wat kun je met wat je al hebt</h3>
    <p>Vink aan wat er in huis is. Rechts zie je wat daarmee kan, en welk ding als eerste iets zou toevoegen.</p>
  </div>
  <div class="g-kiezer__body">
    <div class="g-vinkjes">
      <label class="g-vinkje"><input type="checkbox" value="mat"><span>Een mat<b>Of een dikke handdoek op een zachte vloer</b></span></label>
      <label class="g-vinkje"><input type="checkbox" value="band"><span>Weerstandsbanden<b>Elastieken banden of een lange band met handvatten</b></span></label>
      <label class="g-vinkje"><input type="checkbox" value="gewicht"><span>Halters of een kettlebell<b>Ook een gevulde rugzak telt mee</b></span></label>
      <label class="g-vinkje"><input type="checkbox" value="lussen"><span>Een ophangsysteem<b>Lussen aan een deur, balk of boom</b></span></label>
      <label class="g-vinkje"><input type="checkbox" value="bank"><span>Een stevige verhoging<b>Bank, stoel, kist of onderste traptrede</b></span></label>
      <label class="g-vinkje"><input type="checkbox" value="ruimte"><span>Drie bij drie meter vrije vloer<b>Gemeten met de tafel aan de kant</b></span></label>
    </div>
    <div class="g-uitkomst">
      <h4>Hiermee kun je trainen</h4>
      <ul id="g-kan"></ul>
      <div class="g-uitkomst__tip" id="g-tip"></div>
    </div>
  </div>
</div>
"""

# --------------------------------------------------------------- homepage
home = f"""
<main>
<section class="g-start">
  <div class="g-baan g-start__raster">
    <div>
      <span class="g-etiket">de kofferbak van je trainer</span>
      <h1>alles wat je nodig hebt past in één tas</h1>
      <p class="g-lead">Een sportschool heeft driehonderd vierkante meter apparatuur nodig om te doen wat een trainer met acht dingen in een tas voor elkaar krijgt. Deze site gaat over die acht dingen: wat ze doen, wat je zelf zou aanschaffen, wat je beter laat staan en hoe lang het meegaat.</p>
      <div class="g-knoppen">
        <a class="g-knop" href="wat-neemt-de-trainer-mee.html">Kijk in de tas</a>
        <a class="g-knop g-knop--leeg" href="de-miskopen.html">De miskopen</a>
      </div>
    </div>
    <div class="g-film">
      <video autoplay muted loop playsinline preload="metadata" poster="gereedschap-loop.jpg"
             aria-label="Beelden van trainingen met banden, gewichten, een ophangsysteem en een balanstrainer">
        <source src="gereedschap-loop.webm" type="video/webm">
        <source src="gereedschap-loop.mp4" type="video/mp4">
      </video>
      <div class="g-film__band">materiaal in gebruik · buiten en aan huis</div>
    </div>
  </div>
</section>

<section class="g-vak">
  <div class="g-baan">
    <div class="g-titel">
      <span class="g-titel__nr">01 — DE KERN</span>
      <h2>drie dingen dekken tachtig procent</h2>
      <p>Trainers verschillen in stijl, maar bijna iedereen komt met deze drie. De rest is aanvulling.</p>
    </div>
    <div class="g-artikelen">
      <article class="g-artikel">
        <img src="gewicht-tillen.jpg" alt="Vrouw tilt een gewicht op van het gras" loading="lazy">
        <div class="g-artikel__kop"><span class="g-artikel__nr">01</span><h3 style="margin:0">verstelbaar gewicht</h3></div>
        <div class="g-artikel__body">
          <p>Eén set verstelbare halters of twee kettlebells vervangen een heel rek. Van twee kilo voor schouderwerk tot twintig voor benen, zonder dat er meer dan een halve vierkante meter in beslag wordt genomen.</p>
          <dl><dt>doet</dt><dd>Kracht in benen, rug, borst en schouders</dd>
              <dt>gaat mee</dt><dd>Tientallen jaren, mits niet op tegels gegooid</dd></dl>
          <div class="g-oordeel g-oordeel--ja">Waard om zelf te kopen, maar pas na een week of acht</div>
        </div>
      </article>
      <article class="g-artikel">
        <img src="weerstandsband.jpg" alt="Weerstandsbanden liggen klaar op de grond" loading="lazy">
        <div class="g-artikel__kop"><span class="g-artikel__nr">02</span><h3 style="margin:0">weerstandsbanden</h3></div>
        <div class="g-artikel__body">
          <p>Vullen het gat dat gewichten thuis laten vallen: trekken. Zonder rek of kabelstation is een band aan een deurpost de enige manier om je rug echt aan het werk te krijgen.</p>
          <dl><dt>doet</dt><dd>Trekbewegingen, opwarmen, fijnere dosering</dd>
              <dt>gaat mee</dt><dd>Eén tot drie jaar, latex droogt uit</dd></dl>
          <div class="g-oordeel g-oordeel--ja">Goedkoopste aanvulling met het grootste bereik</div>
        </div>
      </article>
      <article class="g-artikel">
        <img src="bal-boven-hoofd.jpg" alt="Vrouw traint op een mat met een bal boven het hoofd" loading="lazy">
        <div class="g-artikel__kop"><span class="g-artikel__nr">03</span><h3 style="margin:0">een fatsoenlijke mat</h3></div>
        <div class="g-artikel__body">
          <p>De onopvallende held. Een mat van anderhalve centimeter maakt harde tegels bruikbaar, houdt gewichten van je laminaat en bepaalt of grondwerk wel of niet wordt overgeslagen.</p>
          <dl><dt>doet</dt><dd>Comfort, grip en bescherming van de vloer</dd>
              <dt>gaat mee</dt><dd>Vijf jaar of langer bij fatsoenlijke dichtheid</dd></dl>
          <div class="g-oordeel g-oordeel--ja">Het enige dat vrijwel iedereen uiteindelijk zelf koopt</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="g-vak g-vak--warm">
  <div class="g-baan">
    <div class="g-titel">
      <span class="g-titel__nr">02 — KIEZER</span>
      <h2>doe de inventaris</h2>
      <p>Veel mensen hebben meer in huis dan ze denken. Onderstaand blokje rekent het voor je uit.</p>
    </div>
    {KIEZER}
  </div>
</section>

<section class="g-vak g-vak--zwart">
  <div class="g-baan">
    <div class="g-titel">
      <span class="g-titel__nr">03 — REGELS</span>
      <h2>vier vuistregels bij aanschaf</h2>
      <p>Ze schelen een berging vol ongebruikte spullen.</p>
    </div>
    <div class="g-blokken">
      <div class="g-blok"><h3>koop pas na acht weken</h3><p>In de eerste twee maanden verandert je programma nog voortdurend. Wat in week twee onmisbaar leek, ligt in week acht ongebruikt. Laat de trainer zolang meebrengen wat nodig is.</p></div>
      <div class="g-blok"><h3>zwaarder dan je denkt</h3><p>De klassieke fout is te licht kopen. Halters van drie kilo zijn na twee maanden te licht voor benen en rug. Koop verstelbaar of koop meteen het zwaarste dat je nu net niet aankunt.</p></div>
      <div class="g-blok"><h3>één ding tegelijk</h3><p>Koop nooit een pakket. Bijna elk voordeelpakket bevat twee bruikbare dingen en vier vulartikelen. Los kopen is per stuk duurder en in totaal goedkoper.</p></div>
      <div class="g-blok"><h3>waar laat je het</h3><p>Materiaal dat op zolder ligt, wordt niet gebruikt. Bepaal de opbergplek voordat je bestelt, en zit die plek meer dan tien seconden van je trainingsplek af, koop dan niets.</p></div>
    </div>
  </div>
</section>

<section class="g-vak">
  <div class="g-baan">
    <div class="g-titel">
      <span class="g-titel__nr">04 — AANBIEDERS</span>
      <h2>drie partijen die met eigen materiaal komen</h2>
      <p>Gelijk gepresenteerd. Alle drie brengen mee wat bij jouw programma hoort; je hoeft vooraf niets aan te schaffen.</p>
    </div>
    {blok_partijen()}
  </div>
</section>

<section class="g-vak g-vak--warm">
  <div class="g-baan">
    <div class="g-titel">
      <span class="g-titel__nr">05 — ARTIKELEN</span>
      <h2>uitgezocht</h2>
    </div>
    <div class="g-stukken">
      <article class="g-stuk">
        <img src="ophangsysteem.jpg" alt="Ophangsysteem gespannen tussen bomen" loading="lazy">
        <div class="g-stuk__t">
          <h3><a href="banden-versus-gewichten.html">Banden of gewichten</a></h3>
          <p>Wat een elastiek wel kan en een halter niet, en waarom de vergelijking meestal verkeerd wordt gemaakt.</p>
          <a class="g-stuk__meer" href="banden-versus-gewichten.html">Lezen →</a>
        </div>
      </article>
      <article class="g-stuk">
        <img src="balanstrainer.jpg" alt="Vrouw traint op een balanstrainer bij het water" loading="lazy">
        <div class="g-stuk__t">
          <h3><a href="hoe-lang-gaat-het-mee.html">Hoe lang gaat het mee</a></h3>
          <p>Levensduur per soort materiaal, en waaraan je ziet dat een band of mat vervangen moet worden.</p>
          <a class="g-stuk__meer" href="hoe-lang-gaat-het-mee.html">Lezen →</a>
        </div>
      </article>
      <article class="g-stuk">
        <img src="rek-in-park.jpg" alt="Trainingsrek in een park met een mat ervoor" loading="lazy">
        <div class="g-stuk__t">
          <h3><a href="zonder-iets-beginnen.html">Zonder iets beginnen</a></h3>
          <p>Zes weken trainen met alleen een stoel, een muur en een trap. Wanneer dat ophoudt te werken.</p>
          <a class="g-stuk__meer" href="zonder-iets-beginnen.html">Lezen →</a>
        </div>
      </article>
    </div>
  </div>
</section>
</main>
"""

# --------------------------------------------------------- in de kofferbak
kofferbak = """
<main>
<section class="g-vak" style="border-top:0">
  <div class="g-baan">
    <span class="g-etiket">inventaris</span>
    <h1>wat er in de kofferbak ligt</h1>
    <p style="max-width:62ch;color:#33362e">Acht dingen komen bij vrijwel elke trainer terug. Ze passen samen in één tas en één krat, wegen bij elkaar rond de vijfentwintig kilo, en dekken alles wat je thuis nodig hebt.</p>
  </div>
</section>

<section class="g-vak g-vak--warm">
  <div class="g-baan">
    <div class="g-titel"><span class="g-titel__nr">A — ALTIJD MEE</span><h2>het vaste deel</h2></div>
    <div class="g-vragen">
      <details open><summary>Verstelbare halters, meestal twee tot vierentwintig kilo</summary><p>Het zwaarste voorwerp in de auto en het meest gebruikte. Verstelbaar omdat een trainer bij dezelfde klant binnen één sessie van vier kilo naar zestien wil kunnen. Vaste halters zouden een aanhanger vergen.</p></details>
      <details><summary>Eén of twee kettlebells</summary><p>Voor zwaaibewegingen, dragen en alles waarbij het gewicht buiten je lichaam hangt. Een kettlebell van zestien kilo doet werk dat met halters onhandig wordt. Trainers kiezen meestal één maat en variëren met het aantal herhalingen.</p></details>
      <details><summary>Een set weerstandsbanden met verschillende zwaartes</summary><p>Vier tot zes banden, van heel licht voor schouders tot zwaar voor benen. Kosten samen minder dan één halter en vervangen thuis het complete kabelstation van een sportschool.</p></details>
      <details><summary>Een deuranker</summary><p>Een stuk band met een verdikking die je tussen deur en kozijn klemt. Daarmee wordt elke deur in huis een bevestigingspunt. Het onbeduidendste voorwerp in de tas en het meest onmisbare.</p></details>
      <details><summary>Een ophangsysteem met lussen</summary><p>Aan een deur, een boom of een balkonrand. Levert tientallen oefeningen op met alleen je eigen gewicht, waarbij de zwaarte wordt geregeld door je voeten te verzetten. Weegt niets en past in een broekzak.</p></details>
      <details><summary>Een mat</summary><p>Dikker en steviger dan een yogamat. Ligt onderin en gaat als eerste de deur uit bij aankomst.</p></details>
      <details><summary>Een verstelbare step of opstapkist</summary><p>Voor uitvalspassen, opstappen en opdrukken op hoogte. Wordt vaak vervangen door de onderste traptrede of een stevige salontafel als de trainer niet wil sjouwen.</p></details>
      <details><summary>Een timer en een hartslagband</summary><p>Klein maar sturend. De timer bepaalt het ritme van een circuit, de hartslagband laat zien of je werkelijk in de zware zone komt of dat het alleen zo voelt.</p></details>
    </div>
  </div>
</section>

<section class="g-vak">
  <div class="g-baan">
    <div class="g-titel"><span class="g-titel__nr">B — SOMS MEE</span><h2>het wisselende deel</h2>
    <p>Afhankelijk van je programma, je ruimte en soms van het seizoen.</p></div>
    <div class="g-blokken">
      <div class="g-blok"><h3>medicijnbal</h3><p>Voor werpen, vangen en draaien. Vraagt een muur die ertegen kan of een tuin. Zonder een van beide blijft hij in de auto.</p></div>
      <div class="g-blok"><h3>balanstrainer</h3><p>Halve bal met een plat vlak. Vooral bij herstel na enkel- of knieklachten en bij ouderen die valangst hebben. Neemt veel ruimte in voor één doel.</p></div>
      <div class="g-blok"><h3>slee of sledge op wielen</h3><p>Alleen bij een lange oprit of een stuk stoep. Zware conditieprikkel zonder rennen, dus geschikt voor wie knieklachten heeft.</p></div>
      <div class="g-blok"><h3>bokshandschoenen en pads</h3><p>Populair, en niet alleen om de conditie. Slaan doet iets met mensen dat squats niet doen. Vraagt wel drie bij drie meter en een trainer die het beheerst.</p></div>
      <div class="g-blok"><h3>zandzak of gevulde tas</h3><p>Onhandig gewicht dat verschuift terwijl je het draagt. Dat is precies de bedoeling: je romp moet corrigeren.</p></div>
      <div class="g-blok"><h3>koorden en pionnen</h3><p>Voor voetenwerk en korte richtingsveranderingen. Vrijwel altijd buiten, en vooral bij wie een balsport speelt of weer wil gaan spelen.</p></div>
    </div>
  </div>
</section>

<section class="g-vak g-vak--zwart">
  <div class="g-baan g-smal">
    <h2>wat er niet in ligt</h2>
    <p>Geen apparaten. Geen loopband, geen crosstrainer, geen fitnessapparaat met kabels. Niet omdat die niet werken, maar omdat je ze niet in een kofferbak krijgt en omdat één apparaat één beweging traint. Een band en een halter samen doen het werk van vier apparaten en passen in een tas.</p>
    <p>Dat is de kern van trainen aan huis: het materiaal is bewust generiek en de trainer is het specialistische deel.</p>
  </div>
</section>
</main>
"""

# ------------------------------------------------------------ zelf kopen
kopen = """
<main>
<section class="g-vak" style="border-top:0">
  <div class="g-baan">
    <span class="g-etiket">volgorde van aanschaf</span>
    <h1>wat je zelf zou aanschaffen, en wanneer</h1>
    <p style="max-width:62ch;color:#33362e">Je hoeft niets te kopen om te beginnen; alle drie de aanbieders brengen mee wat nodig is. Maar veel mensen willen na een tijdje ook tussendoor iets kunnen doen. Dit is de volgorde die per euro het meeste oplevert.</p>
  </div>
</section>

<section class="g-vak g-vak--warm">
  <div class="g-baan">
    <div class="g-titel"><span class="g-titel__nr">STAP VOOR STAP</span><h2>vier aankopen, in deze volgorde</h2></div>
    <div class="g-artikelen">
      <article class="g-artikel">
        <div class="g-artikel__kop"><span class="g-artikel__nr">01</span><h3 style="margin:0">de mat</h3></div>
        <div class="g-artikel__body">
          <p>Begin hier, ongeacht je doel. Kies op dikte en dichtheid, niet op kleur: anderhalve centimeter, stevig genoeg dat je vinger er niet doorheen zakt. Te zacht is net zo onhandig als te dun.</p>
          <dl><dt>wanneer</dt><dd>Meteen, ook in week één</dd><dt>let op</dt><dd>Afmeting minstens 180 bij 60 centimeter</dd></dl>
          <div class="g-oordeel g-oordeel--ja">Vrijwel iedereen heeft er baat bij</div>
        </div>
      </article>
      <article class="g-artikel">
        <div class="g-artikel__kop"><span class="g-artikel__nr">02</span><h3 style="margin:0">de banden</h3></div>
        <div class="g-artikel__body">
          <p>Een set van vier tot zes zwaartes, plus een deuranker. Hiermee kun je tussen de sessies door zelf iets doen zonder dat je iets zwaars in huis hoeft te halen. Nemen geen ruimte in en gaan mee op reis.</p>
          <dl><dt>wanneer</dt><dd>Na drie of vier weken</dd><dt>let op</dt><dd>Latex scheurt sneller dan stof, stof glijdt minder</dd></dl>
          <div class="g-oordeel g-oordeel--ja">Kleinste uitgave, grootste toename in mogelijkheden</div>
        </div>
      </article>
      <article class="g-artikel">
        <div class="g-artikel__kop"><span class="g-artikel__nr">03</span><h3 style="margin:0">het gewicht</h3></div>
        <div class="g-artikel__body">
          <p>Verstelbare halters of één kettlebell. Dit is de eerste echte uitgave en meteen de laatste die je nodig hebt. Vraag je trainer welke zwaarte je over een half jaar gebruikt, niet welke nu goed voelt.</p>
          <dl><dt>wanneer</dt><dd>Na acht weken, niet eerder</dd><dt>let op</dt><dd>Verstelmechanisme moet met één hand werken</dd></dl>
          <div class="g-oordeel g-oordeel--ja">Alleen als je ook zonder trainer wilt doorgaan</div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="g-vak">
  <div class="g-baan">
    <div class="g-titel"><span class="g-titel__nr">TWIJFELGEVALLEN</span><h2>waar het van afhangt</h2></div>
    <div class="g-vragen">
      <details open><summary>Ophangsysteem: alleen als je een goed bevestigingspunt hebt</summary><p>Aan een binnendeur werkt het, mits die deur naar je toe opendraait en het kozijn stevig is. In een tuin met een tak op tweeënhalve meter werkt het uitstekend. Heb je geen van beide, koop het dan niet; het ding is nutteloos zonder ophangpunt.</p></details>
      <details><summary>Opstapkist: meestal onnodig</summary><p>De onderste traptrede is even hoog, kost niets en staat er al. Alleen zinvol als je gelijkvloers woont zonder trap en veel opstapwerk in je programma zit.</p></details>
      <details><summary>Hartslagband: alleen bij conditiewerk</summary><p>Bij krachttraining zegt je hartslag weinig. Traint je op uithoudingsvermogen of moet je om medische redenen binnen een zone blijven, dan is een borstband nauwkeuriger dan een horloge.</p></details>
      <details><summary>Tweede set halters: bijna nooit</summary><p>Zodra je verstelbare halters hebt, is een tweede set zonde. Wil je zwaarder, dan koop je losse schijven bij, geen nieuwe set.</p></details>
    </div>
  </div>
</section>

<section class="g-vak g-vak--zwart">
  <div class="g-baan g-smal">
    <h2>tweedehands of nieuw</h2>
    <p>Gewichten zijn ideaal tweedehands: ijzer slijt niet en de prijs ligt vaak op de helft. Controleer alleen of het verstelmechanisme soepel loopt en of er geen schijven ontbreken.</p>
    <p>Banden juist niet. Latex veroudert ook als het ongebruikt in een la ligt, en een band die tijdens een trekbeweging knapt komt met kracht terug. Dat is het bespaarde bedrag niet waard.</p>
    <p>Matten zitten ertussenin. Een gebruikte mat van een goed merk is prima; een gebruikte goedkope mat is meestal al doorgezakt.</p>
  </div>
</section>
</main>
"""

# --------------------------------------------------------------- miskopen
miskopen = """
<main>
<section class="g-vak" style="border-top:0">
  <div class="g-baan">
    <span class="g-etiket">wat er in de berging belandt</span>
    <h1>de miskopen</h1>
    <p style="max-width:62ch;color:#33362e">Iedere trainer die bij mensen thuis komt, ziet dezelfde ongebruikte spullen staan. Niet omdat het slechte producten zijn, maar omdat ze iets beloven wat materiaal niet kan waarmaken.</p>
  </div>
</section>

<section class="g-vak g-vak--warm">
  <div class="g-baan">
    <div class="g-titel"><span class="g-titel__nr">TOP VIJF</span><h2>wat er het vaakst stof staat te vangen</h2></div>
    <div class="g-blokken">
      <div class="g-blok"><h3>de hometrainer als kapstok</h3><p>Het bekendste voorbeeld en niet zonder reden. Een hometrainer traint één beweging in één vlak. Wie hem gebruikt wordt beter in fietsen, en verder verandert er weinig. Hij neemt bovendien meer ruimte in dan alle andere spullen samen.</p></div>
      <div class="g-blok"><h3>trilplaten</h3><p>Verkocht met de belofte dat je passief resultaat boekt. De trilling geeft een licht effect op doorbloeding en dat is het. Voor de aanschafprijs koop je twee jaar begeleiding met banden en gewichten.</p></div>
      <div class="g-blok"><h3>het buikapparaat</h3><p>Elk seizoen een nieuwe vorm. Het probleem is niet het apparaat maar het uitgangspunt: buikspieroefeningen halen geen vet weg op die plek. Dat is niet hoe het lichaam werkt, hoe hardnekkig het idee ook is.</p></div>
      <div class="g-blok"><h3>opvouwbare bankjes van dun plaatstaal</h3><p>Voelen wankel, en dat is precies waarom ze niet gebruikt worden. Bij een oefening waarbij je gewicht boven je hoofd hebt, moet de ondergrond geen twijfel oproepen.</p></div>
      <div class="g-blok"><h3>voordeelpakketten</h3><p>Een doos met tien artikelen waarvan er twee bruikbaar zijn. De rest is te licht, te klein of te kwetsbaar. Los kopen kost per stuk meer en in totaal minder.</p></div>
      <div class="g-blok"><h3>het complete krachtstation</h3><p>Ooit populair, zelden gebruikt. Neemt de ruimte in van een tweepersoonsbed, biedt minder variatie dan één set halters en is bij verhuizing onverkoopbaar.</p></div>
    </div>
  </div>
</section>

<section class="g-vak">
  <div class="g-baan">
    <div class="g-titel"><span class="g-titel__nr">HERKENNEN</span><h2>drie signalen van een miskoop</h2></div>
    <div class="g-vragen">
      <details open><summary>Het traint precies één beweging</summary><p>Alles wat je maar op één manier kunt gebruiken, verveelt binnen een maand en past daarna nergens meer in je programma. Materiaal dat blijft, is materiaal dat tien dingen kan.</p></details>
      <details><summary>Het wordt verkocht met een resultaat, niet met een functie</summary><p>Een band wordt verkocht als band. Een apparaat dat wordt verkocht als "strakke buik in zes weken" verkoopt een uitkomst die niet van het apparaat afhangt.</p></details>
      <details><summary>Het past niet in de ruimte waar je traint</summary><p>Alles wat je eerst moet verplaatsen voordat je kunt beginnen, wordt op den duur niet meer verplaatst. Dat is geen kwestie van discipline maar van drempel.</p></details>
    </div>
    <div class="g-uitlicht">
      <p>Vuistregel die de meeste miskopen voorkomt: koop niets waarvan je de naam pas kent sinds je de advertentie zag.</p>
    </div>
  </div>
</section>

<section class="g-vak g-vak--zwart">
  <div class="g-baan g-smal">
    <h2>en wat als je het al hebt</h2>
    <p>Weggooien hoeft meestal niet. Een hometrainer is een prima opwarming van tien minuten voordat de trainer met de rest begint. Een balanstrainer die je zelf nooit gebruikt, blijkt in handen van een trainer opeens vier oefeningen op te leveren.</p>
    <p>Zeg bij de kennismaking gewoon wat er staat. De kans is groot dat het ergens in past, en anders weet je dat het weg kan.</p>
  </div>
</section>
</main>
"""

# ------------------------------------------------------------- aanbieders
aanbieders = f"""
<main>
<section class="g-vak" style="border-top:0">
  <div class="g-baan">
    <span class="g-etiket">naast elkaar</span>
    <h1>drie aanbieders die alles meebrengen</h1>
    <p style="max-width:62ch;color:#33362e">Bij alle drie geldt hetzelfde uitgangspunt: je hoeft vooraf niets aan te schaffen. De trainer komt met wat bij jouw programma past. Hieronder dezelfde soort informatie per partij.</p>
  </div>
</section>

<section class="g-vak">
  <div class="g-baan">{blok_partijen({
    "LET'S DO IT Personal Training": "Uitsluitend vrouwelijke trainsters, met materiaal afgestemd op het programma.",
    "YourHealth Personal Training": "Grootste bereik, dus ook buiten de Randstad meestal een trainer beschikbaar.",
    "Jouw Personal Trainer aan Huis": "Werkt bewust licht: veel lichaamsgewicht en banden, minder zwaar ijzer.",
  })}</div>
</section>

<section class="g-vak g-vak--warm">
  <div class="g-baan">
    <div class="g-titel"><span class="g-titel__nr">VRAGEN</span><h2>wat je over materiaal kunt vragen</h2></div>
    <div class="g-vragen">
      <details open><summary>Blijft er iets staan tussen de sessies door?</summary><p>Dat verschilt per trainer en is bespreekbaar. Sommigen laten een band en een mat achter zodat je zelf iets kunt doen; anderen nemen alles mee. Vraag het bij de kennismaking, want het bepaalt of je tussendoor iets kunt.</p></details>
      <details><summary>Wat als ik zelf al iets heb?</summary><p>Zeg het vooraf. Een trainer die weet dat er halters staan, laat de zijne in de auto en gebruikt de ruimte in het programma voor iets anders. Ook oude of goedkope spullen zijn bruikbaar.</p></details>
      <details><summary>Kan ik trainen zonder dat er iets in huis komt?</summary><p>Ja. Met lichaamsgewicht, een muur, een stoel en een trap kun je maandenlang vooruit. Op enig moment stokt de vooruitgang in kracht, maar dat duurt langer dan de meeste mensen denken.</p></details>
      <details><summary>Wat als ik vier hoog woon zonder lift?</summary><p>Dan komt er minder gewicht mee en wordt er meer met banden en lichaamsgewicht gewerkt. Geef het van tevoren door; dat scheelt een trainer die met vierentwintig kilo aan de voordeur staat.</p></details>
      <details><summary>Wordt het materiaal schoongemaakt?</summary><p>Bij alle drie de aanbieders hoort dat bij het werk, zeker bij matten en handschoenen. Vind je het belangrijk, vraag er dan naar; het is een normale vraag.</p></details>
    </div>
  </div>
</section>
</main>
"""

ARTIKELEN = [
    dict(bestand="banden-versus-gewichten.html",
         titel="Banden of gewichten",
         omschrijving="Wat een weerstandsband wel kan en een halter niet, en waarom die vergelijking meestal verkeerd wordt gemaakt.",
         beeld="ophangsysteem.jpg", alt="Ophangsysteem gespannen tussen bomen",
         inhoud="""
<p>De vraag komt bijna altijd zo: zijn banden net zo goed als gewichten? Daarmee wordt het verkeerde vergeleken. Het zijn geen concurrenten maar aanvullingen, en ze verschillen in iets fundamentelers dan zwaarte.</p>

<h2>Een halter is overal even zwaar</h2>
<p>Een halter van tien kilo weegt tien kilo, of je hem nu net optilt of bovenaan de beweging bent. Dat maakt hem voorspelbaar en daarom uitstekend om kracht op te bouwen. Je weet precies wat je vorige week deed en wat je nu erbij legt.</p>

<h2>Een band wordt zwaarder naarmate hij verder rekt</h2>
<p>Dat betekent dat het begin licht is en het eind zwaar. Voor sommige oefeningen is dat een nadeel; voor trekbewegingen is het juist prettig, omdat je schouder aan het begin het kwetsbaarst is en aan het eind het sterkst.</p>
<p>Het is ook de reden dat banden zo geschikt zijn na een blessure. De belasting bouwt zichzelf op tijdens de beweging in plaats van meteen vol op je gewricht te staan.</p>

<div class="g-uitlicht">
  <p>Kort: gewicht voor duwen en tillen, banden voor trekken en voor alles wat voorzichtig moet. Thuis heb je beide nodig, en juist daarom is de vraag welke van de twee beter is niet te beantwoorden.</p>
</div>

<h2>Wat een band thuis oplost</h2>
<p>In een sportschool trek je aan kabels: roeien, latpulldown, kabelvlieger. Thuis is dat de grote afwezige. Zonder iets om aan te trekken traint bijna iedereen te veel voorkant en te weinig achterkant, met een houding die daarna nog slechter wordt dan hij was.</p>
<p>Een band aan een deuranker lost dat in één keer op, voor de prijs van een pizza.</p>

<h2>Waar de band tekortschiet</h2>
<ul>
  <li>Zware beenoefeningen. Je benen zijn sterker dan welke band ook aankan.</li>
  <li>Meten van vooruitgang. Een band geeft geen getal; je weet niet of je sterker wordt of alleen verder rekt.</li>
  <li>Duurzaamheid. Latex veroudert, ook ongebruikt. Reken op één tot drie jaar.</li>
</ul>

<h2>De praktische conclusie</h2>
<p>Wie één ding koopt, koopt banden: goedkoop, klein, breed inzetbaar. Wie serieus sterker wil worden, komt er niet omheen om daarnaast gewicht in huis te halen. En wie met een trainer werkt, hoeft die keuze de eerste maanden helemaal niet te maken, want beide liggen in de auto.</p>
"""),
    dict(bestand="hoe-lang-gaat-het-mee.html",
         titel="Hoe lang gaat het mee",
         omschrijving="Levensduur per soort trainingsmateriaal, en waaraan je ziet dat een band, mat of ophangsysteem vervangen moet worden.",
         beeld="balanstrainer.jpg", alt="Vrouw traint op een balanstrainer",
         inhoud="""
<p>Trainingsmateriaal gaat opvallend lang mee, met één uitzondering die juist gevaarlijk kan worden als je hem negeert. Een overzicht van wat wanneer op is.</p>

<h2>IJzer: praktisch onbeperkt</h2>
<p>Halters, kettlebells en schijven slijten niet. Roest is cosmetisch en te verwijderen met staalwol en een beetje olie. Het enige kwetsbare deel is het verstelmechanisme van verstelbare halters: dat is kunststof en kan breken als er hard mee wordt gewerkt. Tweedehands kopen is hier dus verstandig, mits je dat mechanisme controleert.</p>

<h2>Banden: één tot drie jaar</h2>
<p>Dit is de uitzondering. Latex veroudert door zonlicht, warmte en gewoon door de tijd, ook als de band ongebruikt in een la ligt. Een verouderde band knapt niet geleidelijk maar in één keer, en komt met kracht terug in de richting waar je aan trekt. Bij een oefening op ooghoogte is dat een reëel risico.</p>

<div class="g-uitlicht">
  <p>Controleer banden elke paar maanden: rek hem uit en kijk tegen het licht. Zie je witte streepjes, kleine scheurtjes bij de handvatten, of voelt het oppervlak plakkerig, dan is hij op. Twijfel je, gooi hem weg.</p>
</div>

<h2>Matten: drie tot acht jaar</h2>
<p>Afhankelijk van dichtheid. Een goedkope schuimmat zakt binnen een jaar door en herstelt niet meer; je merkt het doordat je knieën de vloer weer voelen. Een mat met hoge dichtheid houdt het jaren vol. Bewaren doe je opgerold, niet gevouwen, want een vouw wordt een blijvende knik.</p>

<h2>Ophangsystemen: vijf jaar of meer</h2>
<p>Het band zelf gaat lang mee; de aandacht moet naar de bevestiging. Controleer voor elke sessie of het anker goed vastzit en of het stiksel bij de lussen heel is. Buiten aan een tak: kijk naar schuurplekken door schors.</p>

<h2>Wat je nooit moet blijven gebruiken</h2>
<ul>
  <li>Een band met een zichtbare beschadiging, hoe klein ook.</li>
  <li>Een deuranker waarvan de verdikking is gaan vervormen.</li>
  <li>Een opstapkist die kraakt of wiebelt onder je gewicht.</li>
  <li>Een mat waarop je bij een plank je polsen door de mat heen voelt.</li>
</ul>

<h2>Onderhoud kost vijf minuten per maand</h2>
<p>Banden schoon en droog opbergen, uit de zon. Gewichten droog houden. Matten na het trainen afnemen, want zweet tast het oppervlak aan. Meer is er niet. Materiaal dat zo behandeld wordt, gaat langer mee dan je belangstelling ervoor.</p>
"""),
    dict(bestand="zonder-iets-beginnen.html",
         titel="Zonder iets beginnen",
         omschrijving="Zes weken trainen met alleen een stoel, een muur en een trap, en het punt waarop dat ophoudt te werken.",
         beeld="rek-in-park.jpg", alt="Trainingsrek in een park",
         inhoud="""
<p>De meest gestelde vraag voor de eerste sessie: moet ik nog iets aanschaffen? Het antwoord is nee, en dat is geen beleefdheid. Met wat er in elk huis staat, kun je maanden vooruit.</p>

<h2>Wat er al is</h2>
<ul>
  <li><strong>Een muur.</strong> Voor opdrukken op hoogte, voor een stille wandzit, voor steun bij balansoefeningen.</li>
  <li><strong>Een stevige stoel.</strong> Opstappen, opdrukken met verhoogde handen, triceps, heupbruggen, en als steun bij eenbenige oefeningen.</li>
  <li><strong>Een trap.</strong> De beste conditieprikkel in huis, en tegelijk een verhoging in vijf verschillende hoogtes.</li>
  <li><strong>Een deurpost.</strong> Voor trekbewegingen met je eigen gewicht, mits je hem goed vastpakt.</li>
  <li><strong>Een gevulde rugzak.</strong> Boeken of flessen water. Tien kilo op je rug is tien kilo, ook zonder logo erop.</li>
</ul>

<h2>Wat je in zes weken bereikt</h2>
<p>Meer dan verwacht, vooral als je van een laag startpunt komt. In de eerste weken komt vooruitgang niet uit spiergroei maar uit coördinatie: je zenuwstelsel leert de spieren die je hebt beter aansturen. Dat effect is groot en het heeft geen materiaal nodig.</p>
<p>Ook conditie reageert snel. Trapwerk drie keer per week doet binnen een maand hoorbaar iets met hoe je boven aankomt.</p>

<div class="g-uitlicht">
  <p>Het punt waarop dit stokt is te herkennen: je kunt van een oefening opeens twintig of dertig herhalingen doen zonder dat het echt zwaar wordt. Dan train je uithoudingsvermogen en geen kracht meer, en is er weerstand nodig.</p>
</div>

<h2>Wat er dan als eerste bij komt</h2>
<p>Niet een apparaat, maar iets om aan te trekken. Precies dat wat je thuis niet kunt improviseren. Een set banden met een deuranker kost weinig en opent de hele achterkant van je lichaam, die je met lichaamsgewicht alleen nauwelijks bereikt.</p>
<p>Daarna, en pas daarna, gewicht.</p>

<h2>Waarom trainers hier zelf op sturen</h2>
<p>Een trainer die in de eerste sessie een boodschappenlijst overhandigt, verkoopt spullen. Een trainer die begint met wat er staat, laat zien dat hij de omgeving kan lezen en dat hij het programma aanpast aan jou in plaats van aan zijn koffer. Dat is bovendien een goed teken voor de maanden erna.</p>
"""),
    dict(bestand="opbergen-en-opruimen.html",
         titel="Waar laat je het",
         omschrijving="Opbergen bepaalt of trainingsmateriaal gebruikt wordt of stof vangt. Vier oplossingen die in een gewoon huis werken.",
         beeld="studiovloer.jpg", alt="Trainingsvloer met gewichten en rek",
         inhoud="""
<p>De vraag waar bijna niemand over nadenkt voor de aankoop, en die achteraf bepaalt of het gebruikt wordt. Materiaal dat niet binnen tien seconden in je handen ligt, wordt op den duur niet meer gepakt.</p>

<h2>De tienseconderegel</h2>
<p>Meet het eens. Van je trainingsplek naar je materiaal en terug, inclusief kast opendoen en doos verplaatsen. Duurt dat langer dan tien seconden, dan wordt het op een grijze dinsdag de reden om het maar over te slaan. Dit klinkt overdreven, maar het is de meest voorspellende factor die trainers bij klanten zien.</p>

<h2>Vier opstellingen die werken</h2>
<ul>
  <li><strong>De mand in de kamer.</strong> Een gesloten rieten of stoffen mand naast de bank. Uit het zicht, binnen handbereik, en niemand ergert zich eraan.</li>
  <li><strong>Onder de bank.</strong> Matten en banden passen plat onder een bank met poten. Halters niet; die verdwijnen daar en komen er nooit meer uit.</li>
  <li><strong>Een plank in de gang.</strong> Op ooghoogte, zodat je het ziet. Zichtbaarheid werkt: materiaal dat je passeert, gebruik je vaker.</li>
  <li><strong>De hoek van de berging.</strong> Alleen als je berging ook je trainingsplek is, zoals bij een garage of schuur. Anders valt het af op de tienseconderegel.</li>
</ul>

<div class="g-uitlicht">
  <p>Bepaal de plek voordat je bestelt. Niet andersom. Dat ene besluit voorkomt de meeste ongebruikte spullen.</p>
</div>

<h2>Wat je beter niet doet</h2>
<p>Alles in een grote sporttas stoppen. Dat lijkt netjes en zorgt ervoor dat je elke keer drie dingen moet uitpakken om bij het vierde te komen. Ook: opbergen op zolder of in een kelder waar je een trap voor op moet. Dat is de dood in de pot.</p>

<h2>Als de trainer materiaal achterlaat</h2>
<p>Sommige trainers laten een band en een mat achter zodat je tussendoor iets kunt doen. Spreek dan meteen af waar het ligt en wie het schoonmaakt. Het klinkt kleinzielig, maar spullen zonder vaste plek verhuizen langzaam naar de rommelhoek, en daar eindigt het gebruik.</p>

<h2>Ruimte terugwinnen</h2>
<p>Wie al jaren materiaal heeft dat niet gebruikt wordt, kan het beste één ding tegelijk beoordelen: heb ik dit in het afgelopen half jaar aangeraakt? Zo nee, dan is het geen trainingsmateriaal maar meubilair. Verkopen of weggeven maakt ruimte vrij voor de vier vierkante meter die je wél nodig hebt.</p>
"""),
]


def artikel(a):
    inhoud = f"""
<main>
<section class="g-stukkop">
  <div class="g-baan g-smal">
    <span class="g-etiket">artikel</span>
    <h1>{html.escape(a['titel'])}</h1>
  </div>
</section>
<section class="g-tekst">
  <div class="g-baan g-smal">
    <img src="{a['beeld']}" alt="{html.escape(a['alt'])}" style="border:3px solid #111310;margin-bottom:28px" loading="lazy">
    {a['inhoud']}
    <p style="margin-top:2em"><a href="artikelen.html">Terug naar alle artikelen</a></p>
  </div>
</section>
</main>
"""
    return pagina(a["bestand"], a["titel"] + " | aanhuispersonaltrainer.nl", a["omschrijving"], inhoud, diepte=0)


def artikelindex():
    kaarten = ""
    for a in ARTIKELEN:
        naam = os.path.basename(a["bestand"])
        kaarten += f"""
      <article class="g-stuk">
        <img src="{a['beeld']}" alt="{html.escape(a['alt'])}" loading="lazy">
        <div class="g-stuk__t">
          <h3><a href="{naam}">{html.escape(a['titel'])}</a></h3>
          <p>{html.escape(a['omschrijving'])}</p>
          <a class="g-stuk__meer" href="{naam}">Lezen →</a>
        </div>
      </article>"""
    inhoud = f"""
<main>
<section class="g-vak" style="border-top:0">
  <div class="g-baan">
    <span class="g-etiket">vier stukken</span>
    <h1>artikelen</h1>
    <p style="max-width:60ch;color:#33362e">Over banden tegenover gewichten, hoe lang materiaal meegaat, beginnen zonder iets, en waar je het allemaal laat.</p>
  </div>
</section>
<section class="g-vak"><div class="g-baan"><div class="g-stukken">{kaarten}</div></div></section>
</main>
"""
    return pagina("artikelen.html", "Artikelen | aanhuispersonaltrainer.nl",
                  "Vier artikelen over trainingsmateriaal aan huis: banden of gewichten, levensduur, beginnen zonder iets en opbergen.",
                  inhoud, diepte=0)


gemaakt = []
gemaakt.append(pagina("index.html", "Aan huis personal trainer | Al het materiaal past in één tas",
    "Wat een personal trainer aan huis meebrengt, wat je zelf zou aanschaffen en in welke volgorde, en welke apparaten je beter laat staan.",
    home, extra_body=KIEZER_JS))
gemaakt.append(pagina("wat-neemt-de-trainer-mee.html", "In de kofferbak | aanhuispersonaltrainer.nl",
    "De acht dingen die vrijwel elke personal trainer aan huis meebrengt, plus het materiaal dat alleen bij bepaalde programma's meekomt.", kofferbak))
gemaakt.append(pagina("zelf-aanschaffen.html", "Zelf aanschaffen | aanhuispersonaltrainer.nl",
    "In welke volgorde je zelf trainingsmateriaal koopt, wanneer dat zinvol wordt en wat je beter tweedehands of juist nieuw haalt.", kopen))
gemaakt.append(pagina("de-miskopen.html", "De miskopen | aanhuispersonaltrainer.nl",
    "Welk trainingsmateriaal het vaakst ongebruikt in de berging staat, hoe je een miskoop vooraf herkent en wat je met het al gekochte kunt.", miskopen))
gemaakt.append(pagina("aanbieders.html", "Aanbieders | aanhuispersonaltrainer.nl",
    "Drie aanbieders die met eigen materiaal aan huis komen, naast elkaar gezet, plus de vragen die je over materiaal kunt stellen.", aanbieders))
gemaakt.append(artikelindex())
for a in ARTIKELEN:
    gemaakt.append(artikel(a))

open(os.path.join(BASIS, "robots.txt"), "w", encoding="utf-8").write(
    f"User-agent: *\nAllow: /\n\nSitemap: {DOMEIN}/sitemap.xml\n")
urls = "".join(f"  <url><loc>{DOMEIN}/{'' if b=='index.html' else b[:-5]}</loc></url>\n" for b in gemaakt)
open(os.path.join(BASIS, "sitemap.xml"), "w", encoding="utf-8").write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

pagina("404.html", "Pagina niet gevonden | aanhuispersonaltrainer.nl", "Deze pagina bestaat niet.", """
<main>
<section class="g-vak" style="border-top:0;padding-top:60px">
  <div class="g-baan g-smal" style="text-align:center">
    <span class="g-etiket">404</span>
    <h1>deze pagina ligt niet in de tas</h1>
    <p style="color:#33362e">Waarschijnlijk een oude verwijzing. Via de balk bovenaan kom je overal.</p>
    <div class="g-knoppen" style="justify-content:center"><a class="g-knop" href="/">Naar de startpagina</a></div>
  </div>
</section>
</main>
""")

print(f"{len(gemaakt)} pagina's gebouwd")
