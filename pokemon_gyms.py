from bs4 import BeautifulSoup
import csv
html_doc = """
<html>
<body>
<h4><span class="mw-headline" id="Kanto">Kanto</span></h4>
<table style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background:#ACD36C">Order
</th>
<th style="background:#ACD36C">Gym
</th>
<th style="background:#ACD36C">Badge
</th>
<th style="background:#ACD36C">Type
</th>
<th style="background:#ACD36C">Leader
</th></tr>
<tr style="background:#D1C17D">
<td>1
</td>
<td><a href="/wiki/Pewter_Gym" title="Pewter Gym">Pewter Gym</a>
</td>
<td><a href="/wiki/File:Boulder_Badge.png" class="image"><img alt="Boulder Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/d/dd/Boulder_Badge.png/50px-Boulder_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/d/dd/Boulder_Badge.png/75px-Boulder_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/dd/Boulder_Badge.png/100px-Boulder_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Boulder_Badge" title="Badge">Boulder Badge</a>
</td>
<td><a href="/wiki/Rock_(type)" title="Rock (type)">Rock</a>
</td>
<td><a href="/wiki/Brock" title="Brock"><img alt="VSBrock PE.png" src="//archives.bulbagarden.net/media/upload/thumb/e/e2/VSBrock_PE.png/64px-VSBrock_PE.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/e/e2/VSBrock_PE.png/96px-VSBrock_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/e/e2/VSBrock_PE.png/128px-VSBrock_PE.png 2x" /></a><br/><a href="/wiki/Brock" title="Brock">Brock</a>
</td></tr>
<tr style="background:#9DB7F5">
<td>2
</td>
<td><a href="/wiki/Cerulean_Gym" title="Cerulean Gym">Cerulean Gym</a>
</td>
<td><a href="/wiki/File:Cascade_Badge.png" class="image"><img alt="Cascade Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/9/9c/Cascade_Badge.png/50px-Cascade_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/9/9c/Cascade_Badge.png/75px-Cascade_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/9/9c/Cascade_Badge.png/100px-Cascade_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Cascade_Badge" title="Badge">Cascade Badge</a>
</td>
<td><a href="/wiki/Water_(type)" title="Water (type)">Water</a>
</td>
<td><a href="/wiki/Misty" title="Misty"><img alt="VSMisty PE.png" src="//archives.bulbagarden.net/media/upload/thumb/0/0c/VSMisty_PE.png/64px-VSMisty_PE.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/0/0c/VSMisty_PE.png/96px-VSMisty_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/0c/VSMisty_PE.png/128px-VSMisty_PE.png 2x" /></a><br/><a href="/wiki/Misty" title="Misty">Misty</a>
</td></tr>
<tr style="background:#FAE078">
<td>3
</td>
<td><a href="/wiki/Vermilion_Gym" title="Vermilion Gym">Vermilion Gym</a>
</td>
<td><a href="/wiki/File:Thunder_Badge.png" class="image"><img alt="Thunder Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/a/a6/Thunder_Badge.png/50px-Thunder_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/a/a6/Thunder_Badge.png/75px-Thunder_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/a/a6/Thunder_Badge.png/100px-Thunder_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Thunder_Badge" title="Badge">Thunder Badge</a>
</td>
<td><a href="/wiki/Electric_(type)" title="Electric (type)">Electric</a>
</td>
<td><a href="/wiki/Lt._Surge" title="Lt. Surge"><img alt="VSLt Surge PE.png" src="//archives.bulbagarden.net/media/upload/thumb/c/c6/VSLt_Surge_PE.png/61px-VSLt_Surge_PE.png" decoding="async" loading="lazy" width="61" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/c/c6/VSLt_Surge_PE.png/91px-VSLt_Surge_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/c6/VSLt_Surge_PE.png/121px-VSLt_Surge_PE.png 2x" /></a><br/><a href="/wiki/Lt._Surge" title="Lt. Surge">Lt. Surge</a>
</td></tr>
<tr style="background:#A7DB8D">
<td>4
</td>
<td><a href="/wiki/Celadon_Gym" title="Celadon Gym">Celadon Gym</a>
</td>
<td><a href="/wiki/File:Rainbow_Badge.png" class="image"><img alt="Rainbow Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/b/b5/Rainbow_Badge.png/50px-Rainbow_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/b/b5/Rainbow_Badge.png/75px-Rainbow_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/b/b5/Rainbow_Badge.png/100px-Rainbow_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Rainbow_Badge" title="Badge">Rainbow Badge</a>
</td>
<td><a href="/wiki/Grass_(type)" title="Grass (type)">Grass</a>
</td>
<td><a href="/wiki/Erika" title="Erika"><img alt="VSErika PE.png" src="//archives.bulbagarden.net/media/upload/thumb/3/35/VSErika_PE.png/64px-VSErika_PE.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/3/35/VSErika_PE.png/96px-VSErika_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/35/VSErika_PE.png/128px-VSErika_PE.png 2x" /></a><br/><a href="/wiki/Erika" title="Erika">Erika</a>
</td></tr>
<tr style="background:#C183C1">
<td rowspan="2">5
</td>
<td rowspan="2"><a href="/wiki/Fuchsia_Gym" title="Fuchsia Gym">Fuchsia Gym</a>
</td>
<td rowspan="2"><a href="/wiki/File:Soul_Badge.png" class="image"><img alt="Soul Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/7d/Soul_Badge.png/50px-Soul_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/7d/Soul_Badge.png/75px-Soul_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/7d/Soul_Badge.png/100px-Soul_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Soul_Badge" title="Badge">Soul Badge</a>
</td>
<td rowspan="2"><a href="/wiki/Poison_(type)" title="Poison (type)">Poison</a>
</td>
<td><a href="/wiki/Koga" title="Koga"><img alt="VSKoga PE.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d8/VSKoga_PE.png/64px-VSKoga_PE.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d8/VSKoga_PE.png/96px-VSKoga_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d8/VSKoga_PE.png/128px-VSKoga_PE.png 2x" /></a><br/><a href="/wiki/Koga" title="Koga">Koga</a><br/><small>(Gen. I/III/VII)</small>
</td></tr>
<tr style="background:#FA92B2">
<td>6
</td>
<td><a href="/wiki/Saffron_Gym" title="Saffron Gym">Saffron Gym</a>
</td>
<td><a href="/wiki/File:Marsh_Badge.png" class="image"><img alt="Marsh Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/6/6b/Marsh_Badge.png/50px-Marsh_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/6/6b/Marsh_Badge.png/75px-Marsh_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/6b/Marsh_Badge.png/100px-Marsh_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Marsh_Badge" title="Badge">Marsh Badge</a>
</td>
<td><a href="/wiki/Psychic_(type)" title="Psychic (type)">Psychic</a>
</td>
<td><a href="/wiki/Sabrina" title="Sabrina"><img alt="VSSabrina PE.png" src="//archives.bulbagarden.net/media/upload/thumb/2/20/VSSabrina_PE.png/64px-VSSabrina_PE.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/2/20/VSSabrina_PE.png/96px-VSSabrina_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/20/VSSabrina_PE.png/128px-VSSabrina_PE.png 2x" /></a><br/><a href="/wiki/Sabrina" title="Sabrina">Sabrina</a>
</td></tr>
<tr style="background:#F5AC78">
<td>7
</td>
<td><a href="/wiki/Cinnabar_Gym" title="Cinnabar Gym">Cinnabar Gym</a>
</td>
<td><a href="/wiki/File:Volcano_Badge.png" class="image"><img alt="Volcano Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/1/12/Volcano_Badge.png/50px-Volcano_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/1/12/Volcano_Badge.png/75px-Volcano_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/1/12/Volcano_Badge.png/100px-Volcano_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Volcano_Badge" title="Badge">Volcano Badge</a>
</td>
<td><a href="/wiki/Fire_(type)" title="Fire (type)">Fire</a>
</td>
<td><a href="/wiki/Blaine" title="Blaine"><img alt="VSBlaine PE.png" src="//archives.bulbagarden.net/media/upload/thumb/1/11/VSBlaine_PE.png/64px-VSBlaine_PE.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/1/11/VSBlaine_PE.png/96px-VSBlaine_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/1/11/VSBlaine_PE.png/128px-VSBlaine_PE.png 2x" /></a><br/><a href="/wiki/Blaine" title="Blaine">Blaine</a>
</td></tr>
<tr style="background:#EBD69D">
<td rowspan="2">8
</td>
<td rowspan="2"><a href="/wiki/Viridian_Gym" title="Viridian Gym">Viridian Gym</a>
</td>
<td rowspan="2"><a href="/wiki/File:Earth_Badge.png" class="image"><img alt="Earth Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/78/Earth_Badge.png/50px-Earth_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/78/Earth_Badge.png/75px-Earth_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/78/Earth_Badge.png/100px-Earth_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Earth_Badge" title="Badge">Earth Badge</a>
</td>
<td><a href="/wiki/Ground_(type)" title="Ground (type)">Ground</a>
</td>
<td><a href="/wiki/Giovanni" title="Giovanni"><img alt="VSGiovanni PE.png" src="//archives.bulbagarden.net/media/upload/thumb/4/4a/VSGiovanni_PE.png/64px-VSGiovanni_PE.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/4/4a/VSGiovanni_PE.png/96px-VSGiovanni_PE.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/4a/VSGiovanni_PE.png/128px-VSGiovanni_PE.png 2x" /></a><br/><a href="/wiki/Giovanni" title="Giovanni">Giovanni</a><br/><small>(Gen. I/III/VII)</small>
</td></tr>
</tbody></table>
<h4><span class="mw-headline" id="Johto">Johto</span></h4>
<table style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background:#DCD677">Order
</th>
<th style="background:#DCD677">Gym
</th>
<th style="background:#DCD677">Badge
</th>
<th style="background:#DCD677">Type
</th>
<th style="background:#DCD677">Leader
</th></tr>
<tr style="background:#C6B7F5">
<td>1
</td>
<td><a href="/wiki/Violet_Gym" title="Violet Gym">Violet Gym</a>
</td>
<td><a href="/wiki/File:Zephyr_Badge.png" class="image"><img alt="Zephyr Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/4/4a/Zephyr_Badge.png/50px-Zephyr_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/4a/Zephyr_Badge.png/75px-Zephyr_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/4/4a/Zephyr_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Zephyr_Badge" title="Badge">Zephyr Badge</a>
</td>
<td><a href="/wiki/Flying_(type)" title="Flying (type)">Flying</a>
</td>
<td><a href="/wiki/Falkner" title="Falkner"><img alt="VSFalkner.png" src="//archives.bulbagarden.net/media/upload/5/5a/VSFalkner.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Falkner" title="Falkner">Falkner</a>
</td></tr>
<tr style="background:#C6D16E">
<td>2
</td>
<td><a href="/wiki/Azalea_Gym" title="Azalea Gym">Azalea Gym</a>
</td>
<td><a href="/wiki/File:Hive_Badge.png" class="image"><img alt="Hive Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/0/08/Hive_Badge.png/50px-Hive_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/0/08/Hive_Badge.png 1.5x" /></a><br/><a href="/wiki/Badge#Hive_Badge" title="Badge">Hive Badge</a>
</td>
<td><a href="/wiki/Bug_(type)" title="Bug (type)">Bug</a>
</td>
<td><a href="/wiki/Bugsy" title="Bugsy"><img alt="VSBugsy.png" src="//archives.bulbagarden.net/media/upload/2/2a/VSBugsy.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Bugsy" title="Bugsy">Bugsy</a>
</td></tr>
<tr style="background:#C6C6A7">
<td>3
</td>
<td><a href="/wiki/Goldenrod_Gym" title="Goldenrod Gym">Goldenrod Gym</a>
</td>
<td><a href="/wiki/File:Plain_Badge.png" class="image"><img alt="Plain Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/a/a7/Plain_Badge.png/50px-Plain_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/a/a7/Plain_Badge.png/75px-Plain_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/a/a7/Plain_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Plain_Badge" title="Badge">Plain Badge</a>
</td>
<td><a href="/wiki/Normal_(type)" title="Normal (type)">Normal</a>
</td>
<td><a href="/wiki/Whitney" title="Whitney"><img alt="VSWhitney.png" src="//archives.bulbagarden.net/media/upload/2/27/VSWhitney.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Whitney" title="Whitney">Whitney</a>
</td></tr>
<tr style="background:#A292BC">
<td>4
</td>
<td><a href="/wiki/Ecruteak_Gym" title="Ecruteak Gym">Ecruteak Gym</a>
</td>
<td><a href="/wiki/File:Fog_Badge.png" class="image"><img alt="Fog Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/4/48/Fog_Badge.png/50px-Fog_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/48/Fog_Badge.png/75px-Fog_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/4/48/Fog_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Fog_Badge" title="Badge">Fog Badge</a>
</td>
<td><a href="/wiki/Ghost_(type)" title="Ghost (type)">Ghost</a>
</td>
<td><a href="/wiki/Morty" title="Morty"><img alt="VSMorty.png" src="//archives.bulbagarden.net/media/upload/0/04/VSMorty.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Morty" title="Morty">Morty</a>
</td></tr>
<tr style="background:#D67873">
<td>5
</td>
<td><a href="/wiki/Cianwood_Gym" title="Cianwood Gym">Cianwood Gym</a>
</td>
<td><a href="/wiki/File:Storm_Badge.png" class="image"><img alt="Storm Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/b/b9/Storm_Badge.png/50px-Storm_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/b/b9/Storm_Badge.png/75px-Storm_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/b/b9/Storm_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Storm_Badge" title="Badge">Storm Badge</a>
</td>
<td><a href="/wiki/Fighting_(type)" title="Fighting (type)">Fighting</a>
</td>
<td><a href="/wiki/Chuck" title="Chuck"><img alt="VSChuck.png" src="//archives.bulbagarden.net/media/upload/a/af/VSChuck.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Chuck" title="Chuck">Chuck</a>
</td></tr>
<tr style="background:#D1D1E0">
<td>6
</td>
<td><a href="/wiki/Olivine_Gym" title="Olivine Gym">Olivine Gym</a>
</td>
<td><a href="/wiki/File:Mineral_Badge.png" class="image"><img alt="Mineral Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/7b/Mineral_Badge.png/50px-Mineral_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/7b/Mineral_Badge.png/75px-Mineral_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/7/7b/Mineral_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Mineral_Badge" title="Badge">Mineral Badge</a>
</td>
<td><a href="/wiki/Steel_(type)" title="Steel (type)">Steel</a>
</td>
<td><a href="/wiki/Jasmine" title="Jasmine"><img alt="VSJasmine.png" src="//archives.bulbagarden.net/media/upload/f/f2/VSJasmine.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Jasmine" title="Jasmine">Jasmine</a>
</td></tr>
<tr style="background:#BCE6E6">
<td>7
</td>
<td><a href="/wiki/Mahogany_Gym" title="Mahogany Gym">Mahogany Gym</a>
</td>
<td><a href="/wiki/File:Glacier_Badge.png" class="image"><img alt="Glacier Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/e/e6/Glacier_Badge.png/50px-Glacier_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/e/e6/Glacier_Badge.png/75px-Glacier_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/e/e6/Glacier_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Glacier_Badge" title="Badge">Glacier Badge</a>
</td>
<td><a href="/wiki/Ice_(type)" title="Ice (type)">Ice</a>
</td>
<td><a href="/wiki/Pryce" title="Pryce"><img alt="VSPryce.png" src="//archives.bulbagarden.net/media/upload/4/4f/VSPryce.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Pryce" title="Pryce">Pryce</a>
</td></tr>
<tr style="background:#A27DFA">
<td style="background:#border-bottom-left-radius: 10px; -moz-border-radius-bottomleft: 10px; -webkit-border-bottom-left-radius: 10px; -khtml-border-bottom-left-radius: 10px; -icab-border-bottom-left-radius: 10px; -o-border-bottom-left-radius: 10px;;">8
</td>
<td><a href="/wiki/Blackthorn_Gym" title="Blackthorn Gym">Blackthorn Gym</a>
</td>
<td><a href="/wiki/File:Rising_Badge.png" class="image"><img alt="Rising Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/5/58/Rising_Badge.png/50px-Rising_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/5/58/Rising_Badge.png/75px-Rising_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/5/58/Rising_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Rising_Badge" title="Badge">Rising Badge</a>
</td>
<td><a href="/wiki/Dragon_(type)" title="Dragon (type)">Dragon</a>
</td>
<td style="background:#border-bottom-right-radius: 10px; -moz-border-radius-bottomright: 10px; -webkit-border-bottom-right-radius: 10px; -khtml-border-bottom-right-radius: 10px; -icab-border-bottom-right-radius: 10px; -o-border-bottom-right-radius: 10px;;"><a href="/wiki/Clair" title="Clair"><img alt="VSClair.png" src="//archives.bulbagarden.net/media/upload/f/fc/VSClair.png" decoding="async" loading="lazy" width="96" height="64" /></a><br/><a href="/wiki/Clair" title="Clair">Clair</a>
</td></tr></tbody></table>
<h4><span class="mw-headline" id="Hoenn">Hoenn</span></h4>
<table style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background:#9CD7C8">Order
</th>
<th style="background:#9CD7C8">Gym
</th>
<th style="background:#9CD7C8">Badge
</th>
<th style="background:#9CD7C8">Type
</th>
<th style="background:#9CD7C8">Leader
</th></tr>
<tr style="background:#D1C17D">
<td>1
</td>
<td><a href="/wiki/Rustboro_Gym" title="Rustboro Gym">Rustboro Gym</a>
</td>
<td><a href="/wiki/File:Stone_Badge.png" class="image"><img alt="Stone Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/6/63/Stone_Badge.png/50px-Stone_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/6/63/Stone_Badge.png/75px-Stone_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/63/Stone_Badge.png/100px-Stone_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Stone_Badge" title="Badge">Stone Badge</a>
</td>
<td><a href="/wiki/Rock_(type)" title="Rock (type)">Rock</a>
</td>
<td><a href="/wiki/Roxanne" title="Roxanne"><img alt="VSRoxanne.png" src="//archives.bulbagarden.net/media/upload/thumb/9/90/VSRoxanne.png/128px-VSRoxanne.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/9/90/VSRoxanne.png/192px-VSRoxanne.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/9/90/VSRoxanne.png/256px-VSRoxanne.png 2x" /></a><br/><a href="/wiki/Roxanne" title="Roxanne">Roxanne</a>
</td></tr>
<tr style="background:#D67873">
<td>2
</td>
<td><a href="/wiki/Dewford_Gym" title="Dewford Gym">Dewford Gym</a>
</td>
<td><a href="/wiki/File:Knuckle_Badge.png" class="image"><img alt="Knuckle Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/9/97/Knuckle_Badge.png/50px-Knuckle_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/9/97/Knuckle_Badge.png/75px-Knuckle_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/9/97/Knuckle_Badge.png/100px-Knuckle_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Knuckle_Badge" title="Badge">Knuckle Badge</a>
</td>
<td><a href="/wiki/Fighting_(type)" title="Fighting (type)">Fighting</a>
</td>
<td><a href="/wiki/Brawly" title="Brawly"><img alt="VSBrawly.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d1/VSBrawly.png/128px-VSBrawly.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d1/VSBrawly.png/192px-VSBrawly.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d1/VSBrawly.png/256px-VSBrawly.png 2x" /></a><br/><a href="/wiki/Brawly" title="Brawly">Brawly</a>
</td></tr>
<tr style="background:#FAE078">
<td>3
</td>
<td><a href="/wiki/Mauville_Gym" title="Mauville Gym">Mauville Gym</a>
</td>
<td><a href="/wiki/File:Dynamo_Badge.png" class="image"><img alt="Dynamo Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/3/34/Dynamo_Badge.png/50px-Dynamo_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/3/34/Dynamo_Badge.png/75px-Dynamo_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/34/Dynamo_Badge.png/100px-Dynamo_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Dynamo_Badge" title="Badge">Dynamo Badge</a>
</td>
<td><a href="/wiki/Electric_(type)" title="Electric (type)">Electric</a>
</td>
<td><a href="/wiki/Wattson" title="Wattson"><img alt="VSWattson.png" src="//archives.bulbagarden.net/media/upload/thumb/c/c2/VSWattson.png/128px-VSWattson.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/c/c2/VSWattson.png/192px-VSWattson.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/c2/VSWattson.png/256px-VSWattson.png 2x" /></a><br/><a href="/wiki/Wattson" title="Wattson">Wattson</a>
</td></tr>
<tr style="background:#F5AC78">
<td>4
</td>
<td><a href="/wiki/Lavaridge_Gym" title="Lavaridge Gym">Lavaridge Gym</a>
</td>
<td><a href="/wiki/File:Heat_Badge.png" class="image"><img alt="Heat Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/c/c4/Heat_Badge.png/50px-Heat_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/c/c4/Heat_Badge.png/75px-Heat_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/c4/Heat_Badge.png/100px-Heat_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Heat_Badge" title="Badge">Heat Badge</a>
</td>
<td><a href="/wiki/Fire_(type)" title="Fire (type)">Fire</a>
</td>
<td><a href="/wiki/Flannery" title="Flannery"><img alt="VSFlannery.png" src="//archives.bulbagarden.net/media/upload/thumb/f/f3/VSFlannery.png/128px-VSFlannery.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/f/f3/VSFlannery.png/192px-VSFlannery.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/f/f3/VSFlannery.png/256px-VSFlannery.png 2x" /></a><br/><a href="/wiki/Flannery" title="Flannery">Flannery</a>
</td></tr>
<tr style="background:#C6C6A7">
<td>5
</td>
<td><a href="/wiki/Petalburg_Gym" title="Petalburg Gym">Petalburg Gym</a>
</td>
<td><a href="/wiki/File:Balance_Badge.png" class="image"><img alt="Balance Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/6/63/Balance_Badge.png/50px-Balance_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/6/63/Balance_Badge.png/75px-Balance_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/63/Balance_Badge.png/100px-Balance_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Balance_Badge" title="Badge">Balance Badge</a>
</td>
<td><a href="/wiki/Normal_(type)" title="Normal (type)">Normal</a>
</td>
<td><a href="/wiki/Norman" title="Norman"><img alt="VSNorman.png" src="//archives.bulbagarden.net/media/upload/thumb/a/a0/VSNorman.png/128px-VSNorman.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/a/a0/VSNorman.png/192px-VSNorman.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/a/a0/VSNorman.png/256px-VSNorman.png 2x" /></a><br/><a href="/wiki/Norman" title="Norman">Norman</a>
</td></tr>
<tr style="background:#C6B7F5">
<td>6
</td>
<td><a href="/wiki/Fortree_Gym" title="Fortree Gym">Fortree Gym</a>
</td>
<td><a href="/wiki/File:Feather_Badge.png" class="image"><img alt="Feather Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/6/62/Feather_Badge.png/50px-Feather_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/6/62/Feather_Badge.png/75px-Feather_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/62/Feather_Badge.png/100px-Feather_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Feather_Badge" title="Badge">Feather Badge</a>
</td>
<td><a href="/wiki/Flying_(type)" title="Flying (type)">Flying</a>
</td>
<td><a href="/wiki/Winona" title="Winona"><img alt="VSWinona.png" src="//archives.bulbagarden.net/media/upload/thumb/0/0a/VSWinona.png/128px-VSWinona.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/0/0a/VSWinona.png/192px-VSWinona.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/0a/VSWinona.png/256px-VSWinona.png 2x" /></a><br/><a href="/wiki/Winona" title="Winona">Winona</a>
</td></tr>
<tr style="background:#FA92B2">
<td>7
</td>
<td><a href="/wiki/Mossdeep_Gym" title="Mossdeep Gym">Mossdeep Gym</a>
</td>
<td><a href="/wiki/File:Mind_Badge.png" class="image"><img alt="Mind Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/c/cc/Mind_Badge.png/50px-Mind_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/c/cc/Mind_Badge.png/75px-Mind_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/cc/Mind_Badge.png/100px-Mind_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Mind_Badge" title="Badge">Mind Badge</a>
</td>
<td><a href="/wiki/Psychic_(type)" title="Psychic (type)">Psychic</a>
</td>
<td><a href="/wiki/Tate_and_Liza" title="Tate and Liza"><img alt="VSLiza &amp; Tate.png" src="//archives.bulbagarden.net/media/upload/thumb/c/cb/VSLiza_%26_Tate.png/128px-VSLiza_%26_Tate.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/c/cb/VSLiza_%26_Tate.png/192px-VSLiza_%26_Tate.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/cb/VSLiza_%26_Tate.png/256px-VSLiza_%26_Tate.png 2x" /></a><br/><a href="/wiki/Tate_and_Liza" title="Tate and Liza">Tate and Liza</a>
</td></tr>
<tr style="background:#9DB7F5">
<td rowspan="2">8
</td>
<td rowspan="2"><a href="/wiki/Sootopolis_Gym" title="Sootopolis Gym">Sootopolis Gym</a>
</td>
<td rowspan="2"><a href="/wiki/File:Rain_Badge.png" class="image"><img alt="Rain Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/9/9b/Rain_Badge.png/50px-Rain_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/9/9b/Rain_Badge.png/75px-Rain_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/9/9b/Rain_Badge.png/100px-Rain_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Rain_Badge" title="Badge">Rain Badge</a>
</td>
<td rowspan="2"><a href="/wiki/Water_(type)" title="Water (type)">Water</a>
</td>
<td><a href="/wiki/Wallace" title="Wallace"><img alt="VSWallace.png" src="//archives.bulbagarden.net/media/upload/thumb/3/3d/VSWallace.png/128px-VSWallace.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/3/3d/VSWallace.png/192px-VSWallace.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/3d/VSWallace.png/256px-VSWallace.png 2x" /></a><br/><a href="/wiki/Wallace" title="Wallace">Wallace</a><b><sup><a href="/wiki/Pok%C3%A9mon_Ruby_and_Sapphire_Versions" title="Pokémon Ruby and Sapphire Versions"><span style="color:#A00000;">R</span><span style="color:#0000A0;">S</span></a></sup></b><b><sup><a href="/wiki/Pok%C3%A9mon_Omega_Ruby_and_Alpha_Sapphire" title="Pokémon Omega Ruby and Alpha Sapphire"><span style="color:#AB2813;">OR</span><span style="color:#26649C;">AS</span></a></sup></b>
</td></tr></tbody></table>
<h4><span class="mw-headline" id="Sinnoh">Sinnoh</span></h4>
<table style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background:#B7A3C3">Order
</th>
<th style="background:#B7A3C3">Gym
</th>
<th style="background:#B7A3C3">Badge
</th>
<th style="background:#B7A3C3">Type
</th>
<th style="background:#B7A3C3">Leader
</th></tr>
<tr style="background:#D1C17D">
<td>1
</td>
<td><a href="/wiki/Oreburgh_Gym" title="Oreburgh Gym">Oreburgh Gym</a>
</td>
<td><a href="/wiki/File:Coal_Badge.png" class="image"><img alt="Coal Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/0/0b/Coal_Badge.png/50px-Coal_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/0/0b/Coal_Badge.png/75px-Coal_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/0b/Coal_Badge.png/100px-Coal_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Coal_Badge" title="Badge">Coal Badge</a>
</td>
<td><a href="/wiki/Rock_(type)" title="Rock (type)">Rock</a>
</td>
<td><a href="/wiki/Roark" title="Roark"><img alt="VSRoark BDSP.png" src="//archives.bulbagarden.net/media/upload/thumb/8/84/VSRoark_BDSP.png/64px-VSRoark_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/8/84/VSRoark_BDSP.png/96px-VSRoark_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/84/VSRoark_BDSP.png/128px-VSRoark_BDSP.png 2x" /></a><br/><a href="/wiki/Roark" title="Roark">Roark</a>
</td></tr>
<tr style="background:#A7DB8D">
<td>2
</td>
<td><a href="/wiki/Eterna_Gym" title="Eterna Gym">Eterna Gym</a>
</td>
<td><a href="/wiki/File:Forest_Badge.png" class="image"><img alt="Forest Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/8/8c/Forest_Badge.png/50px-Forest_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/8/8c/Forest_Badge.png/75px-Forest_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/8c/Forest_Badge.png/100px-Forest_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Forest_Badge" title="Badge">Forest Badge</a>
</td>
<td><a href="/wiki/Grass_(type)" title="Grass (type)">Grass</a>
</td>
<td><a href="/wiki/File:VSGardenia_BDSP.png" class="image" title="pxlink=Gardenia"><img alt="pxlink=Gardenia" src="//archives.bulbagarden.net/media/upload/thumb/d/d9/VSGardenia_BDSP.png/64px-VSGardenia_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d9/VSGardenia_BDSP.png/96px-VSGardenia_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d9/VSGardenia_BDSP.png/128px-VSGardenia_BDSP.png 2x" /></a><br/><a href="/wiki/Gardenia" title="Gardenia">Gardenia</a>
</td></tr>
<tr style="background:#D67873">
<td>3<b><sup><a href="/wiki/Pok%C3%A9mon_Diamond_and_Pearl_Versions" title="Pokémon Diamond and Pearl Versions"><span style="color:#AAAAFF;">D</span><span style="color:#FFAAAA;">P</span></a></sup></b><b><sup><a href="/wiki/Pok%C3%A9mon_Brilliant_Diamond_and_Shining_Pearl" title="Pokémon Brilliant Diamond and Shining Pearl"><span style="color:#44BAE5">BD</span><span style="color:#DA7D99">SP</span></a></sup></b><br/>4<b><sup><a href="/wiki/Pok%C3%A9mon_Platinum_Version" title="Pokémon Platinum Version"><span style="color:#999999;">Pt</span></a></sup></b>
</td>
<td><a href="/wiki/Veilstone_Gym" title="Veilstone Gym">Veilstone Gym</a>
</td>
<td><a href="/wiki/File:Cobble_Badge.png" class="image"><img alt="Cobble Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/2/27/Cobble_Badge.png/50px-Cobble_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/2/27/Cobble_Badge.png/75px-Cobble_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/27/Cobble_Badge.png/100px-Cobble_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Cobble_Badge" title="Badge">Cobble Badge</a>
</td>
<td><a href="/wiki/Fighting_(type)" title="Fighting (type)">Fighting</a>
</td>
<td><a href="/wiki/Maylene" title="Maylene"><img alt="VSMaylene BDSP.png" src="//archives.bulbagarden.net/media/upload/thumb/0/0a/VSMaylene_BDSP.png/64px-VSMaylene_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/0/0a/VSMaylene_BDSP.png/96px-VSMaylene_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/0a/VSMaylene_BDSP.png/128px-VSMaylene_BDSP.png 2x" /></a><br/><a href="/wiki/Maylene" title="Maylene">Maylene</a>
</td></tr>
<tr style="background:#9DB7F5">
<td>4<b><sup><a href="/wiki/Pok%C3%A9mon_Diamond_and_Pearl_Versions" title="Pokémon Diamond and Pearl Versions"><span style="color:#AAAAFF;">D</span><span style="color:#FFAAAA;">P</span></a></sup></b><b><sup><a href="/wiki/Pok%C3%A9mon_Brilliant_Diamond_and_Shining_Pearl" title="Pokémon Brilliant Diamond and Shining Pearl"><span style="color:#44BAE5">BD</span><span style="color:#DA7D99">SP</span></a></sup></b><br/>5<b><sup><a href="/wiki/Pok%C3%A9mon_Platinum_Version" title="Pokémon Platinum Version"><span style="color:#999999;">Pt</span></a></sup></b>
</td>
<td><a href="/wiki/Pastoria_Gym" title="Pastoria Gym">Pastoria Gym</a>
</td>
<td><a href="/wiki/File:Fen_Badge.png" class="image"><img alt="Fen Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/1/13/Fen_Badge.png/50px-Fen_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/1/13/Fen_Badge.png/75px-Fen_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/1/13/Fen_Badge.png/100px-Fen_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Fen_Badge" title="Badge">Fen Badge</a>
</td>
<td><a href="/wiki/Water_(type)" title="Water (type)">Water</a>
</td>
<td><a href="/wiki/Crasher_Wake" title="Crasher Wake"><img alt="VSCrasher Wake BDSP.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d6/VSCrasher_Wake_BDSP.png/64px-VSCrasher_Wake_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d6/VSCrasher_Wake_BDSP.png/96px-VSCrasher_Wake_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d6/VSCrasher_Wake_BDSP.png/128px-VSCrasher_Wake_BDSP.png 2x" /></a><br/><a href="/wiki/Crasher_Wake" title="Crasher Wake">Crasher Wake</a>
</td></tr>
<tr style="background:#A292BC">
<td>5<b><sup><a href="/wiki/Pok%C3%A9mon_Diamond_and_Pearl_Versions" title="Pokémon Diamond and Pearl Versions"><span style="color:#AAAAFF;">D</span><span style="color:#FFAAAA;">P</span></a></sup></b><b><sup><a href="/wiki/Pok%C3%A9mon_Brilliant_Diamond_and_Shining_Pearl" title="Pokémon Brilliant Diamond and Shining Pearl"><span style="color:#44BAE5">BD</span><span style="color:#DA7D99">SP</span></a></sup></b><br/>3<b><sup><a href="/wiki/Pok%C3%A9mon_Platinum_Version" title="Pokémon Platinum Version"><span style="color:#999999;">Pt</span></a></sup></b>
</td>
<td><a href="/wiki/Hearthome_Gym" title="Hearthome Gym">Hearthome Gym</a>
</td>
<td><a href="/wiki/File:Relic_Badge.png" class="image"><img alt="Relic Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/2/28/Relic_Badge.png/50px-Relic_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/2/28/Relic_Badge.png/75px-Relic_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/28/Relic_Badge.png/100px-Relic_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Relic_Badge" title="Badge">Relic Badge</a>
</td>
<td><a href="/wiki/Ghost_(type)" title="Ghost (type)">Ghost</a>
</td>
<td><a href="/wiki/Fantina" title="Fantina"><img alt="VSFantina BDSP.png" src="//archives.bulbagarden.net/media/upload/thumb/1/16/VSFantina_BDSP.png/64px-VSFantina_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/1/16/VSFantina_BDSP.png/96px-VSFantina_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/1/16/VSFantina_BDSP.png/128px-VSFantina_BDSP.png 2x" /></a><br/><a href="/wiki/Fantina" title="Fantina">Fantina</a>
</td></tr>
<tr style="background:#D1D1E0">
<td>6
</td>
<td><a href="/wiki/Canalave_Gym" title="Canalave Gym">Canalave Gym</a>
</td>
<td><a href="/wiki/File:Mine_Badge.png" class="image"><img alt="Mine Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/f/fe/Mine_Badge.png/50px-Mine_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/f/fe/Mine_Badge.png/75px-Mine_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/f/fe/Mine_Badge.png/100px-Mine_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Mine_Badge" title="Badge">Mine Badge</a>
</td>
<td><a href="/wiki/Steel_(type)" title="Steel (type)">Steel</a>
</td>
<td><a href="/wiki/Byron" title="Byron"><img alt="VSByron BDSP.png" src="//archives.bulbagarden.net/media/upload/thumb/8/83/VSByron_BDSP.png/64px-VSByron_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/8/83/VSByron_BDSP.png/96px-VSByron_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/83/VSByron_BDSP.png/128px-VSByron_BDSP.png 2x" /></a><br/><a href="/wiki/Byron" title="Byron">Byron</a>
</td></tr>
<tr style="background:#BCE6E6">
<td>7
</td>
<td><a href="/wiki/Snowpoint_Gym" title="Snowpoint Gym">Snowpoint Gym</a>
</td>
<td><a href="/wiki/File:Icicle_Badge.png" class="image"><img alt="Icicle Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/0/09/Icicle_Badge.png/50px-Icicle_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/0/09/Icicle_Badge.png/75px-Icicle_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/09/Icicle_Badge.png/100px-Icicle_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Icicle_Badge" title="Badge">Icicle Badge</a>
</td>
<td><a href="/wiki/Ice_(type)" title="Ice (type)">Ice</a>
</td>
<td><a href="/wiki/Candice" title="Candice"><img alt="VSCandice BDSP.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d9/VSCandice_BDSP.png/64px-VSCandice_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d9/VSCandice_BDSP.png/96px-VSCandice_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d9/VSCandice_BDSP.png/128px-VSCandice_BDSP.png 2x" /></a><br/><a href="/wiki/Candice" title="Candice">Candice</a>
</td></tr>
<tr style="background:#FAE078">
<td style="background:#border-bottom-left-radius: 10px; -moz-border-radius-bottomleft: 10px; -webkit-border-bottom-left-radius: 10px; -khtml-border-bottom-left-radius: 10px; -icab-border-bottom-left-radius: 10px; -o-border-bottom-left-radius: 10px;;">8
</td>
<td><a href="/wiki/Sunyshore_Gym" title="Sunyshore Gym">Sunyshore Gym</a>
</td>
<td><a href="/wiki/File:Beacon_Badge.png" class="image"><img alt="Beacon Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/0/0c/Beacon_Badge.png/50px-Beacon_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/0/0c/Beacon_Badge.png/75px-Beacon_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/0c/Beacon_Badge.png/100px-Beacon_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Beacon_Badge" title="Badge">Beacon Badge</a>
</td>
<td><a href="/wiki/Electric_(type)" title="Electric (type)">Electric</a>
</td>
<td style="background:#border-bottom-right-radius: 10px; -moz-border-radius-bottomright: 10px; -webkit-border-bottom-right-radius: 10px; -khtml-border-bottom-right-radius: 10px; -icab-border-bottom-right-radius: 10px; -o-border-bottom-right-radius: 10px;;"><a href="/wiki/Volkner" title="Volkner"><img alt="VSVolkner BDSP.png" src="//archives.bulbagarden.net/media/upload/thumb/0/0c/VSVolkner_BDSP.png/64px-VSVolkner_BDSP.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/0/0c/VSVolkner_BDSP.png/96px-VSVolkner_BDSP.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/0c/VSVolkner_BDSP.png/128px-VSVolkner_BDSP.png 2x" /></a><br/><a href="/wiki/Volkner" title="Volkner">Volkner</a>
</td></tr></tbody></table>
<h4><span class="mw-headline" id="Unova">Unova</span></h4>
<table class="sortable" style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background-color:#9FCADF" data-sort-type="number">Order<br/>(<b><a href="/wiki/Pok%C3%A9mon_Black_and_White_Versions" title="Pokémon Black and White Versions"><span style="color:#444444;">B</span><span style="color:#929292;">W</span></a></b>)
</th>
<th style="background-color:#9FCADF" class="unsortable">Gym
</th>
<th style="background-color:#9FCADF" class="unsortable">Badge
</th>
<th style="background-color:#9FCADF" class="unsortable">Type
</th>
<th style="background-color:#9FCADF" class="unsortable">Leader
</th></tr>
<tr style="background-color:#A7DB8D">
<td data-sort-value="1"><span class="plainlinks"><a href="/wiki/Oshawott" title="Oshawott"><img alt="Oshawott" src="//archives.bulbagarden.net/media/upload/8/86/501MS3.png" decoding="async" loading="lazy" width="32" height="32" /></a></span><br/>1
</td>
<td rowspan="3" style="background:#F5AC78"><a href="/wiki/Striaton_Gym" title="Striaton Gym">Striaton Gym</a>
</td>
<td rowspan="3" style="background:#F5AC78"><a href="/wiki/File:Trio_Badge.png" class="image"><img alt="Trio Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/50px-Trio_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/75px-Trio_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/100px-Trio_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Trio_Badge" title="Badge">Trio Badge</a>
</td>
<td><a href="/wiki/Grass_(type)" title="Grass (type)">Grass</a>
</td>
<td><a href="/wiki/Cilan" title="Cilan"><img alt="VSCilan.png" src="//archives.bulbagarden.net/media/upload/7/70/VSCilan.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Cilan" title="Cilan">Cilan</a>
</td></tr>
<tr style="background:#F5AC78">
<td data-sort-value="1"><span class="plainlinks"><a href="/wiki/Snivy" title="Snivy"><img alt="Snivy" src="//archives.bulbagarden.net/media/upload/0/06/495MS3.png" decoding="async" loading="lazy" width="32" height="32" /></a></span><br/>1
</td>
<td rowspan="3" style="background:#F5AC78"><a href="/wiki/Striaton_Gym" title="Striaton Gym">Striaton Gym</a>
</td>
<td rowspan="3" style="background:#F5AC78"><a href="/wiki/File:Trio_Badge.png" class="image"><img alt="Trio Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/50px-Trio_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/75px-Trio_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/100px-Trio_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Trio_Badge" title="Badge">Trio Badge</a>
</td>
<td><a href="/wiki/Fire_(type)" title="Fire (type)">Fire</a>
</td>
<td><a href="/wiki/Chili" title="Chili"><img alt="VSChili.png" src="//archives.bulbagarden.net/media/upload/1/15/VSChili.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Chili" title="Chili">Chili</a>
</td></tr>
<tr style="background:#9DB7F5">
<td data-sort-value="1"><span class="plainlinks"><a href="/wiki/Tepig" title="Tepig"><img alt="Tepig" src="//archives.bulbagarden.net/media/upload/9/97/498MS3.png" decoding="async" loading="lazy" width="32" height="32" /></a></span><br/>1
</td>
<td rowspan="3" style="background:#F5AC78"><a href="/wiki/Striaton_Gym" title="Striaton Gym">Striaton Gym</a>
</td>
<td rowspan="3" style="background:#F5AC78"><a href="/wiki/File:Trio_Badge.png" class="image"><img alt="Trio Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/50px-Trio_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/75px-Trio_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/74/Trio_Badge.png/100px-Trio_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Trio_Badge" title="Badge">Trio Badge</a>
</td>
<td><a href="/wiki/Water_(type)" title="Water (type)">Water</a>
</td>
<td><a href="/wiki/Cress" title="Cress"><img alt="VSCress.png" src="//archives.bulbagarden.net/media/upload/c/c6/VSCress.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Cress" title="Cress">Cress</a>
</td></tr>
<tr style="background:#C6C6A7">
<td>2
</td>
<td><a href="/wiki/Nacrene_Gym" title="Nacrene Gym">Nacrene Gym</a>
</td>
<td rowspan="2"><a href="/wiki/File:Basic_Badge.png" class="image"><img alt="Basic Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/8/85/Basic_Badge.png/50px-Basic_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/8/85/Basic_Badge.png/75px-Basic_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/85/Basic_Badge.png/100px-Basic_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Basic_Badge" title="Badge">Basic Badge</a>
</td>
<td rowspan="2"><a href="/wiki/Normal_(type)" title="Normal (type)">Normal</a>
</td>
<td><a href="/wiki/Lenora" title="Lenora"><img alt="VSLenora.png" src="//archives.bulbagarden.net/media/upload/e/ef/VSLenora.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><small><a href="/wiki/Lenora" title="Lenora">Lenora</a>
</small></td></tr>
<tr style="background:#C6C6A7">
<td>1
</td>
<td><a href="/wiki/Aspertia_Gym" title="Aspertia Gym">Aspertia Gym</a>
</td>
<td rowspan="2"><a href="/wiki/File:Basic_Badge.png" class="image"><img alt="Basic Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/8/85/Basic_Badge.png/50px-Basic_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/8/85/Basic_Badge.png/75px-Basic_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/85/Basic_Badge.png/100px-Basic_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Basic_Badge" title="Badge">Basic Badge</a>
</td>
<td rowspan="2"><a href="/wiki/Normal_(type)" title="Normal (type)">Normal</a>
</td>
<td><a href="/wiki/Cheren" title="Cheren"><img alt="VSCheren 2.png" src="//archives.bulbagarden.net/media/upload/7/75/VSCheren_2.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Cheren" title="Cheren">Cheren</a>
</td></tr>
<tr style="background:#C183C1">
<td>2
</td>
<td><a href="/wiki/Virbank_Gym" title="Virbank Gym">Virbank Gym</a>
</td>
<td><a href="/wiki/File:Toxic_Badge.png" class="image"><img alt="Toxic Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/3/3e/Toxic_Badge.png/50px-Toxic_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/3/3e/Toxic_Badge.png/75px-Toxic_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/3e/Toxic_Badge.png/100px-Toxic_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Toxic_Badge" title="Badge">Toxic Badge</a>
</td>
<td><a href="/wiki/Poison_(type)" title="Poison (type)">Poison</a>
</td>
<td><a href="/wiki/Roxie" title="Roxie"><img alt="VSRoxie.png" src="//archives.bulbagarden.net/media/upload/d/de/VSRoxie.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Roxie" title="Roxie">Roxie</a>
</td></tr>
<tr style="background:#C6D16E">
<td colspan="2">3
</td>
<td><a href="/wiki/Castelia_Gym" title="Castelia Gym">Castelia Gym</a>
</td>
<td><a href="/wiki/File:Insect_Badge.png" class="image"><img alt="Insect Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/8/8a/Insect_Badge.png/50px-Insect_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/8/8a/Insect_Badge.png/75px-Insect_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/8a/Insect_Badge.png/100px-Insect_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Insect_Badge" title="Badge">Insect Badge</a>
</td>
<td><a href="/wiki/Bug_(type)" title="Bug (type)">Bug</a>
</td>
<td><a href="/wiki/Burgh" title="Burgh"><img alt="VSBurgh.png" src="//archives.bulbagarden.net/media/upload/6/6e/VSBurgh.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Burgh" title="Burgh">Burgh</a>
</td></tr>
<tr style="background:#FAE078">
<td colspan="2">4
</td>
<td><a href="/wiki/Nimbasa_Gym" title="Nimbasa Gym">Nimbasa Gym</a>
</td>
<td><a href="/wiki/File:Bolt_Badge.png" class="image"><img alt="Bolt Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/5/5b/Bolt_Badge.png/50px-Bolt_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/5/5b/Bolt_Badge.png/75px-Bolt_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/5/5b/Bolt_Badge.png/100px-Bolt_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Bolt_Badge" title="Badge">Bolt Badge</a>
</td>
<td><a href="/wiki/Electric_(type)" title="Electric (type)">Electric</a>
</td>
<td><a href="/wiki/Elesa" title="Elesa"><img alt="VSElesa 2.png" src="//archives.bulbagarden.net/media/upload/0/0f/VSElesa_2.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Elesa" title="Elesa">Elesa</a>
</td></tr>
<tr style="background:#EBD69D">
<td colspan="2">5
</td>
<td><a href="/wiki/Driftveil_Gym" title="Driftveil Gym">Driftveil Gym</a>
</td>
<td><a href="/wiki/File:Quake_Badge.png" class="image"><img alt="Quake Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/2/29/Quake_Badge.png/50px-Quake_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/2/29/Quake_Badge.png/75px-Quake_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/29/Quake_Badge.png/100px-Quake_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Quake_Badge" title="Badge">Quake Badge</a>
</td>
<td><a href="/wiki/Ground_(type)" title="Ground (type)">Ground</a>
</td>
<td><a href="/wiki/Clay" title="Clay"><img alt="VSClay.png" src="//archives.bulbagarden.net/media/upload/0/01/VSClay.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Clay" title="Clay">Clay</a>
</td></tr>
<tr style="background:#C6B7F5">
<td colspan="2">6
</td>
<td><a href="/wiki/Mistralton_Gym" title="Mistralton Gym">Mistralton Gym</a>
</td>
<td><a href="/wiki/File:Jet_Badge.png" class="image"><img alt="Jet Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/9/9c/Jet_Badge.png/50px-Jet_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/9/9c/Jet_Badge.png/75px-Jet_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/9/9c/Jet_Badge.png/100px-Jet_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Jet_Badge" title="Badge">Jet Badge</a>
</td>
<td><a href="/wiki/Flying_(type)" title="Flying (type)">Flying</a>
</td>
<td><a href="/wiki/Skyla" title="Skyla"><img alt="VSSkyla.png" src="//archives.bulbagarden.net/media/upload/c/c7/VSSkyla.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Skyla" title="Skyla">Skyla</a>
</td></tr>
<tr style="background:#BCE6E6">
<td>7
</td>
<td><a href="/wiki/Icirrus_Gym" title="Icirrus Gym">Icirrus Gym</a>
</td>
<td><a href="/wiki/File:Freeze_Badge.png" class="image"><img alt="Freeze Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/a/ac/Freeze_Badge.png/50px-Freeze_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/a/ac/Freeze_Badge.png/75px-Freeze_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/a/ac/Freeze_Badge.png/100px-Freeze_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Freeze_Badge" title="Badge">Freeze Badge</a>
</td>
<td><a href="/wiki/Ice_(type)" title="Ice (type)">Ice</a>
</td>
<td><a href="/wiki/Brycen" title="Brycen"><img alt="VSBrycen.png" src="//archives.bulbagarden.net/media/upload/1/1d/VSBrycen.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Brycen" title="Brycen">Brycen</a>
</td></tr>
<tr style="background:#A27DFA">
<td>7
</td>
<td rowspan="2"><a href="/wiki/Opelucid_Gym" title="Opelucid Gym">Opelucid Gym</a>
</td>
<td rowspan="2"><a href="/wiki/File:Legend_Badge.png" class="image"><img alt="Legend Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/c/c0/Legend_Badge.png/50px-Legend_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/c/c0/Legend_Badge.png/75px-Legend_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/c0/Legend_Badge.png/100px-Legend_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Legend_Badge" title="Badge">Legend Badge</a>
</td>
<td rowspan="2"><a href="/wiki/Dragon_(type)" title="Dragon (type)">Dragon</a>
</td>
<td><a href="/wiki/Drayden" title="Drayden"><img alt="VSDrayden.png" src="//archives.bulbagarden.net/media/upload/d/dd/VSDrayden.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Drayden" title="Drayden">Drayden</a>
</td></tr>
<tr style="background:#9DB7F5">
<td>8
</td>
<td><a href="/wiki/Humilau_Gym" title="Humilau Gym">Humilau Gym</a>
</td>
<td><a href="/wiki/File:Wave_Badge.png" class="image"><img alt="Wave Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/0/00/Wave_Badge.png/50px-Wave_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/0/00/Wave_Badge.png/75px-Wave_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/00/Wave_Badge.png/100px-Wave_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Wave_Badge" title="Badge">Wave Badge</a>
</td>
<td><a href="/wiki/Water_(type)" title="Water (type)">Water</a>
</td>
<td style="background:#border-bottom-right-radius: 10px; -moz-border-radius-bottomright: 10px; -webkit-border-bottom-right-radius: 10px; -khtml-border-bottom-right-radius: 10px; -icab-border-bottom-right-radius: 10px; -o-border-bottom-right-radius: 10px;;"><a href="/wiki/Marlon" title="Marlon"><img alt="VSMarlon.png" src="//archives.bulbagarden.net/media/upload/e/e4/VSMarlon.png" decoding="async" loading="lazy" width="128" height="64" /></a><br/><a href="/wiki/Marlon" title="Marlon">Marlon</a>
</td></tr></tbody></table>
<h4><span class="mw-headline" id="Kalos">Kalos</span></h4>
<table style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background:#DD608C">Order
</th>
<th style="background:#DD608C">Gym
</th>
<th style="background:#DD608C">Badge
</th>
<th style="background:#DD608C">Type
</th>
<th style="background:#DD608C">Leader
</th></tr>
<tr style="background:#C6D16E">
<td>1
</td>
<td><a href="/wiki/Santalune_Gym" title="Santalune Gym">Santalune Gym</a>
</td>
<td><a href="/wiki/File:Bug_Badge.png" class="image"><img alt="Bug Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/a/a5/Bug_Badge.png/50px-Bug_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/a/a5/Bug_Badge.png/75px-Bug_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/a/a5/Bug_Badge.png/100px-Bug_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Bug_Badge" title="Badge">Bug Badge</a>
</td>
<td><a href="/wiki/Bug_(type)" title="Bug (type)">Bug</a>
</td>
<td><a href="/wiki/Viola" title="Viola"><img alt="VSViola.png" src="//archives.bulbagarden.net/media/upload/thumb/8/87/VSViola.png/128px-VSViola.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/8/87/VSViola.png/192px-VSViola.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/87/VSViola.png/256px-VSViola.png 2x" /></a><br/><a href="/wiki/Viola" title="Viola">Viola</a>
</td></tr>
<tr style="background:#D1C17D">
<td>2
</td>
<td><a href="/wiki/Cyllage_Gym" title="Cyllage Gym">Cyllage Gym</a>
</td>
<td><a href="/wiki/File:Cliff_Badge.png" class="image"><img alt="Cliff Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/3/39/Cliff_Badge.png/50px-Cliff_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/3/39/Cliff_Badge.png/75px-Cliff_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/39/Cliff_Badge.png/100px-Cliff_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Cliff_Badge" title="Badge">Cliff Badge</a>
</td>
<td><a href="/wiki/Rock_(type)" title="Rock (type)">Rock</a>
</td>
<td><a href="/wiki/Grant" title="Grant"><img alt="VSGrant.png" src="//archives.bulbagarden.net/media/upload/thumb/0/03/VSGrant.png/128px-VSGrant.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/0/03/VSGrant.png/192px-VSGrant.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/03/VSGrant.png/256px-VSGrant.png 2x" /></a><br/><a href="/wiki/Grant" title="Grant">Grant</a>
</td></tr>
<tr style="background:#D67873">
<td>3
</td>
<td><a href="/wiki/Shalour_Gym" title="Shalour Gym">Shalour Gym</a>
</td>
<td><a href="/wiki/File:Rumble_Badge.png" class="image"><img alt="Rumble Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d4/Rumble_Badge.png/50px-Rumble_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d4/Rumble_Badge.png/75px-Rumble_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d4/Rumble_Badge.png/100px-Rumble_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Rumble_Badge" title="Badge">Rumble Badge</a>
</td>
<td><a href="/wiki/Fighting_(type)" title="Fighting (type)">Fighting</a>
</td>
<td><a href="/wiki/Korrina" title="Korrina"><img alt="VSKorrina.png" src="//archives.bulbagarden.net/media/upload/thumb/4/4c/VSKorrina.png/128px-VSKorrina.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/4/4c/VSKorrina.png/192px-VSKorrina.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/4c/VSKorrina.png/256px-VSKorrina.png 2x" /></a><br/><a href="/wiki/Korrina" title="Korrina">Korrina</a>
</td></tr>
<tr style="background:#A7DB8D">
<td>4
</td>
<td><a href="/wiki/Coumarine_Gym" title="Coumarine Gym">Coumarine Gym</a>
</td>
<td><a href="/wiki/File:Plant_Badge.png" class="image"><img alt="Plant Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/7d/Plant_Badge.png/50px-Plant_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/7d/Plant_Badge.png/75px-Plant_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/7d/Plant_Badge.png/100px-Plant_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Plant_Badge" title="Badge">Plant Badge</a>
</td>
<td><a href="/wiki/Grass_(type)" title="Grass (type)">Grass</a>
</td>
<td><a href="/wiki/Ramos" title="Ramos"><img alt="VSRamos.png" src="//archives.bulbagarden.net/media/upload/thumb/0/06/VSRamos.png/128px-VSRamos.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/0/06/VSRamos.png/192px-VSRamos.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/06/VSRamos.png/256px-VSRamos.png 2x" /></a><br/><a href="/wiki/Ramos" title="Ramos">Ramos</a>
</td></tr>
<tr style="background:#FAE078">
<td>5
</td>
<td><a href="/wiki/Lumiose_Gym" title="Lumiose Gym">Lumiose Gym</a>
</td>
<td><a href="/wiki/File:Voltage_Badge.png" class="image"><img alt="Voltage Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/f/fc/Voltage_Badge.png/50px-Voltage_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/f/fc/Voltage_Badge.png/75px-Voltage_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/f/fc/Voltage_Badge.png/100px-Voltage_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Voltage_Badge" title="Badge">Voltage Badge</a>
</td>
<td><a href="/wiki/Electric_(type)" title="Electric (type)">Electric</a>
</td>
<td><a href="/wiki/Clemont" title="Clemont"><img alt="VSClemont.png" src="//archives.bulbagarden.net/media/upload/thumb/e/e7/VSClemont.png/128px-VSClemont.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/e/e7/VSClemont.png/192px-VSClemont.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/e/e7/VSClemont.png/256px-VSClemont.png 2x" /></a><br/><a href="/wiki/Clemont" title="Clemont">Clemont</a>
</td></tr>
<tr style="background:#F4BDC9">
<td>6
</td>
<td><a href="/wiki/Laverre_Gym" title="Laverre Gym">Laverre Gym</a>
</td>
<td><a href="/wiki/File:Fairy_Badge.png" class="image"><img alt="Fairy Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d1/Fairy_Badge.png/50px-Fairy_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d1/Fairy_Badge.png/75px-Fairy_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d1/Fairy_Badge.png/100px-Fairy_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Fairy_Badge" title="Badge">Fairy Badge</a>
</td>
<td><a href="/wiki/Fairy_(type)" title="Fairy (type)">Fairy</a>
</td>
<td><a href="/wiki/Valerie" title="Valerie"><img alt="VSValerie.png" src="//archives.bulbagarden.net/media/upload/thumb/2/22/VSValerie.png/128px-VSValerie.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/2/22/VSValerie.png/192px-VSValerie.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/22/VSValerie.png/256px-VSValerie.png 2x" /></a><br/><a href="/wiki/Valerie" title="Valerie">Valerie</a>
</td></tr>
<tr style="background:#FA92B2">
<td>7
</td>
<td><a href="/wiki/Anistar_Gym" title="Anistar Gym">Anistar Gym</a>
</td>
<td><a href="/wiki/File:Psychic_Badge.png" class="image"><img alt="Psychic Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/1/13/Psychic_Badge.png/50px-Psychic_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/1/13/Psychic_Badge.png/75px-Psychic_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/1/13/Psychic_Badge.png/100px-Psychic_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Psychic_Badge" title="Badge">Psychic Badge</a>
</td>
<td><a href="/wiki/Psychic_(type)" title="Psychic (type)">Psychic</a>
</td>
<td><a href="/wiki/Olympia" title="Olympia"><img alt="VSOlympia.png" src="//archives.bulbagarden.net/media/upload/thumb/7/7f/VSOlympia.png/128px-VSOlympia.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/7/7f/VSOlympia.png/192px-VSOlympia.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/7f/VSOlympia.png/256px-VSOlympia.png 2x" /></a><br/><a href="/wiki/Olympia" title="Olympia">Olympia</a>
</td></tr>
<tr style="background:#BCE6E6">
<td style="background:#border-bottom-left-radius: 10px; -moz-border-radius-bottomleft: 10px; -webkit-border-bottom-left-radius: 10px; -khtml-border-bottom-left-radius: 10px; -icab-border-bottom-left-radius: 10px; -o-border-bottom-left-radius: 10px;;">8
</td>
<td><a href="/wiki/Snowbelle_Gym" title="Snowbelle Gym">Snowbelle Gym</a>
</td>
<td><a href="/wiki/File:Iceberg_Badge.png" class="image"><img alt="Iceberg Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/8/84/Iceberg_Badge.png/50px-Iceberg_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/8/84/Iceberg_Badge.png/75px-Iceberg_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/84/Iceberg_Badge.png/100px-Iceberg_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Iceberg_Badge" title="Badge">Iceberg Badge</a>
</td>
<td><a href="/wiki/Ice_(type)" title="Ice (type)">Ice</a>
</td>
<td style="background:#border-bottom-right-radius: 10px; -moz-border-radius-bottomright: 10px; -webkit-border-bottom-right-radius: 10px; -khtml-border-bottom-right-radius: 10px; -icab-border-bottom-right-radius: 10px; -o-border-bottom-right-radius: 10px;;"><a href="/wiki/Wulfric" title="Wulfric"><img alt="VSWulfric.png" src="//archives.bulbagarden.net/media/upload/thumb/f/f0/VSWulfric.png/128px-VSWulfric.png" decoding="async" loading="lazy" width="128" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/f/f0/VSWulfric.png/192px-VSWulfric.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/f/f0/VSWulfric.png/256px-VSWulfric.png 2x" /></a><br/><a href="/wiki/Wulfric" title="Wulfric">Wulfric</a>
</td></tr></tbody></table>
<h4><span class="mw-headline" id="Galar">Galar</span></h4>
<table style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background:#C97DC0">Order
</th>
<th style="background:#C97DC0">Gym
</th>
<th style="background:#C97DC0">Badge
</th>
<th style="background:#C97DC0">Type
</th>
<th style="background:#C97DC0">Leader
</th></tr>
<tr style="background:#A7DB8D">
<td>1
</td>
<td><a href="/wiki/File:Grass_Gym_logo.png" class="image"><img alt="Grass Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/7/7d/Grass_Gym_logo.png/50px-Grass_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/7d/Grass_Gym_logo.png/75px-Grass_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/7d/Grass_Gym_logo.png/100px-Grass_Gym_logo.png 2x" /></a><br/><a href="/wiki/Turffield_Stadium" title="Turffield Stadium">Turffield Stadium</a>
</td>
<td><a href="/wiki/File:Grass_Badge.png" class="image"><img alt="Grass Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/0/00/Grass_Badge.png/50px-Grass_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/0/00/Grass_Badge.png/75px-Grass_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/00/Grass_Badge.png/100px-Grass_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Grass_Badge" title="Badge">Grass Badge</a>
</td>
<td><a href="/wiki/Grass_(type)" title="Grass (type)">Grass</a>
</td>
<td><a href="/wiki/Milo" title="Milo"><img alt="VSMilo.png" src="//archives.bulbagarden.net/media/upload/thumb/3/34/VSMilo.png/113px-VSMilo.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/3/34/VSMilo.png/170px-VSMilo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/34/VSMilo.png/226px-VSMilo.png 2x" /></a><br/><a href="/wiki/Milo" title="Milo">Milo</a>
</td></tr>
<tr style="background:#9DB7F5">
<td>2
</td>
<td><a href="/wiki/File:Water_Gym_logo.png" class="image"><img alt="Water Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/e/e8/Water_Gym_logo.png/50px-Water_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/e/e8/Water_Gym_logo.png/75px-Water_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/e/e8/Water_Gym_logo.png/100px-Water_Gym_logo.png 2x" /></a><br/><a href="/wiki/Hulbury_Stadium" title="Hulbury Stadium">Hulbury Stadium</a>
</td>
<td><a href="/wiki/File:Water_Badge.png" class="image"><img alt="Water Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/7/7a/Water_Badge.png/50px-Water_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/7/7a/Water_Badge.png/75px-Water_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/7a/Water_Badge.png/100px-Water_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Water_Badge" title="Badge">Water Badge</a>
</td>
<td><a href="/wiki/Water_(type)" title="Water (type)">Water</a>
</td>
<td><a href="/wiki/Nessa" title="Nessa"><img alt="VSNessa.png" src="//archives.bulbagarden.net/media/upload/thumb/b/b9/VSNessa.png/113px-VSNessa.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/b/b9/VSNessa.png/170px-VSNessa.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/b/b9/VSNessa.png/226px-VSNessa.png 2x" /></a><br/><a href="/wiki/Nessa" title="Nessa">Nessa</a>
</td></tr>
<tr style="background:#F5AC78">
<td>3
</td>
<td><a href="/wiki/File:Fire_Gym_logo.png" class="image"><img alt="Fire Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/a/a1/Fire_Gym_logo.png/50px-Fire_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/a/a1/Fire_Gym_logo.png/75px-Fire_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/a/a1/Fire_Gym_logo.png/100px-Fire_Gym_logo.png 2x" /></a><br/><a href="/wiki/Motostoke_Stadium" title="Motostoke Stadium">Motostoke Stadium</a>
</td>
<td><a href="/wiki/File:Fire_Badge.png" class="image"><img alt="Fire Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/c/cc/Fire_Badge.png/50px-Fire_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/c/cc/Fire_Badge.png/75px-Fire_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/cc/Fire_Badge.png/100px-Fire_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Fire_Badge" title="Badge">Fire Badge</a>
</td>
<td><a href="/wiki/Fire_(type)" title="Fire (type)">Fire</a>
</td>
<td><a href="/wiki/Kabu" title="Kabu"><img alt="VSKabu.png" src="//archives.bulbagarden.net/media/upload/thumb/e/ef/VSKabu.png/113px-VSKabu.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/e/ef/VSKabu.png/170px-VSKabu.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/e/ef/VSKabu.png/226px-VSKabu.png 2x" /></a><br/><a href="/wiki/Kabu" title="Kabu">Kabu</a>
</td></tr>
<tr style="background:#D67873">
<td>4<b><sup><a href="/wiki/Pok%C3%A9mon_Sword_and_Shield" title="Pokémon Sword and Shield"><span style="color:#00A1E9">Sw</span></a></sup></b>
</td>
<td><a href="/wiki/File:Fighting_Gym_logo.png" class="image"><img alt="Fighting Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/b/b9/Fighting_Gym_logo.png/50px-Fighting_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/b/b9/Fighting_Gym_logo.png/75px-Fighting_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/b/b9/Fighting_Gym_logo.png/100px-Fighting_Gym_logo.png 2x" /></a><br/><a href="/wiki/Stow-on-Side_Stadium" title="Stow-on-Side Stadium">Stow-on-Side Stadium</a>
</td>
<td><a href="/wiki/File:Fighting_Badge.png" class="image"><img alt="Fighting Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/2/20/Fighting_Badge.png/50px-Fighting_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/2/20/Fighting_Badge.png/75px-Fighting_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/20/Fighting_Badge.png/100px-Fighting_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Fighting_Badge" title="Badge">Fighting Badge</a>
</td>
<td><a href="/wiki/Fighting_(type)" title="Fighting (type)">Fighting</a>
</td>
<td><a href="/wiki/Bea" title="Bea"><img alt="VSBea.png" src="//archives.bulbagarden.net/media/upload/thumb/5/57/VSBea.png/113px-VSBea.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/5/57/VSBea.png/170px-VSBea.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/5/57/VSBea.png/226px-VSBea.png 2x" /></a><br/><small><a href="/wiki/Bea" title="Bea">Bea</a>
</small></td></tr>
<tr style="background:#A292BC">
<td>4<b><sup><a href="/wiki/Pok%C3%A9mon_Sword_and_Shield" title="Pokémon Sword and Shield"><span style="color:#BF004F">Sh</span></a></sup></b>
</td>
<td><a href="/wiki/File:Ghost_Gym_logo.png" class="image"><img alt="Ghost Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/6/60/Ghost_Gym_logo.png/50px-Ghost_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/6/60/Ghost_Gym_logo.png/75px-Ghost_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/60/Ghost_Gym_logo.png/100px-Ghost_Gym_logo.png 2x" /></a><br/><a href="/wiki/Stow-on-Side_Stadium" title="Stow-on-Side Stadium">Stow-on-Side Stadium</a>
</td>
<td><a href="/wiki/File:Ghost_Badge.png" class="image"><img alt="Ghost Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/3/30/Ghost_Badge.png/50px-Ghost_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/3/30/Ghost_Badge.png/75px-Ghost_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/30/Ghost_Badge.png/100px-Ghost_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Ghost_Badge" title="Badge">Ghost Badge</a>
</td>
<td><a href="/wiki/Ghost_(type)" title="Ghost (type)">Ghost</a>
</td>
<td><a href="/wiki/Allister" title="Allister"><img alt="VSAllister.png" src="//archives.bulbagarden.net/media/upload/thumb/2/27/VSAllister.png/113px-VSAllister.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/2/27/VSAllister.png/170px-VSAllister.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/27/VSAllister.png/226px-VSAllister.png 2x" /></a><br/><small><a href="/wiki/Allister" title="Allister">Allister</a>
</small></td></tr>
<tr style="background:#F4BDC9">
<td rowspan="2">5
</td>
<td rowspan="2"><a href="/wiki/File:Fairy_Gym_logo.png" class="image"><img alt="Fairy Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/c/c3/Fairy_Gym_logo.png/50px-Fairy_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/c/c3/Fairy_Gym_logo.png/75px-Fairy_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/c3/Fairy_Gym_logo.png/100px-Fairy_Gym_logo.png 2x" /></a><br/><a href="/wiki/Ballonlea_Stadium" title="Ballonlea Stadium">Ballonlea Stadium</a>
</td>
<td rowspan="2"><a href="/wiki/File:GalarFairy_Badge.png" class="image"><img alt="GalarFairy Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/e/e3/GalarFairy_Badge.png/50px-GalarFairy_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/e/e3/GalarFairy_Badge.png/75px-GalarFairy_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/e/e3/GalarFairy_Badge.png/100px-GalarFairy_Badge.png 2x" /></a><br/><a href="/wiki/Badge#GalarFairy_Badge" title="Badge">Fairy Badge</a>
</td>
<td rowspan="2"><a href="/wiki/Fairy_(type)" title="Fairy (type)">Fairy</a>
</td>
<td><a href="/wiki/Opal" title="Opal"><img alt="VSOpal.png" src="//archives.bulbagarden.net/media/upload/thumb/3/37/VSOpal.png/113px-VSOpal.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/3/37/VSOpal.png/170px-VSOpal.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/37/VSOpal.png/226px-VSOpal.png 2x" /></a><br/><a href="/wiki/Opal" title="Opal">Opal</a><br/><small>(initial)</small>
</td></tr>
<tr style="background:#D1C17D">
<td>6<b><sup><a href="/wiki/Pok%C3%A9mon_Sword_and_Shield" title="Pokémon Sword and Shield"><span style="color:#00A1E9">Sw</span></a></sup></b>
</td>
<td><a href="/wiki/File:Rock_Gym_logo.png" class="image"><img alt="Rock Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/6/68/Rock_Gym_logo.png/50px-Rock_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/6/68/Rock_Gym_logo.png/75px-Rock_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/68/Rock_Gym_logo.png/100px-Rock_Gym_logo.png 2x" /></a><br/><a href="/wiki/Circhester_Stadium" title="Circhester Stadium">Circhester Stadium</a>
</td>
<td><a href="/wiki/File:Rock_Badge.png" class="image"><img alt="Rock Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/3/3e/Rock_Badge.png/50px-Rock_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/3/3e/Rock_Badge.png/75px-Rock_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/3/3e/Rock_Badge.png/100px-Rock_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Rock_Badge" title="Badge">Rock Badge</a>
</td>
<td><a href="/wiki/Rock_(type)" title="Rock (type)">Rock</a>
</td>
<td><a href="/wiki/Gordie" title="Gordie"><img alt="VSGordie.png" src="//archives.bulbagarden.net/media/upload/thumb/6/6d/VSGordie.png/113px-VSGordie.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/6/6d/VSGordie.png/170px-VSGordie.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/6d/VSGordie.png/226px-VSGordie.png 2x" /></a><br/><small><a href="/wiki/Gordie" title="Gordie">Gordie</a>
</small></td></tr>
<tr style="background:#BCE6E6">
<td>6<b><sup><a href="/wiki/Pok%C3%A9mon_Sword_and_Shield" title="Pokémon Sword and Shield"><span style="color:#BF004F">Sh</span></a></sup></b>
</td>
<td><a href="/wiki/File:Ice_Gym_logo.png" class="image"><img alt="Ice Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/4/4e/Ice_Gym_logo.png/50px-Ice_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/4e/Ice_Gym_logo.png/75px-Ice_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/4e/Ice_Gym_logo.png/100px-Ice_Gym_logo.png 2x" /></a><br/><a href="/wiki/Circhester_Stadium" title="Circhester Stadium">Circhester Stadium</a>
</td>
<td><a href="/wiki/File:Ice_Badge.png" class="image"><img alt="Ice Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/4/43/Ice_Badge.png/50px-Ice_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/43/Ice_Badge.png/75px-Ice_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/43/Ice_Badge.png/100px-Ice_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Ice_Badge" title="Badge">Ice Badge</a>
</td>
<td><a href="/wiki/Ice_(type)" title="Ice (type)">Ice</a>
</td>
<td><a href="/wiki/Melony" title="Melony"><img alt="VSMelony.png" src="//archives.bulbagarden.net/media/upload/thumb/7/7e/VSMelony.png/113px-VSMelony.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/7/7e/VSMelony.png/170px-VSMelony.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/7e/VSMelony.png/226px-VSMelony.png 2x" /></a><br/><small><a href="/wiki/Melony" title="Melony">Melony</a>
</small></td></tr>
<tr style="background:#A29288">
<td rowspan="2">7
</td>
<td rowspan="2"><a href="/wiki/File:Dark_Gym_logo.png" class="image"><img alt="Dark Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/2/27/Dark_Gym_logo.png/50px-Dark_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/2/27/Dark_Gym_logo.png/75px-Dark_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/27/Dark_Gym_logo.png/100px-Dark_Gym_logo.png 2x" /></a><br/><a href="/wiki/Spikemuth" title="Spikemuth">Spikemuth Gym</a>
</td>
<td rowspan="2"><a href="/wiki/File:Dark_Badge.png" class="image"><img alt="Dark Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/4/4d/Dark_Badge.png/50px-Dark_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/4d/Dark_Badge.png/75px-Dark_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/4d/Dark_Badge.png/100px-Dark_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Dark_Badge" title="Badge">Dark Badge</a>
</td>
<td rowspan="2"><a href="/wiki/Dark_(type)" title="Dark (type)">Dark</a>
</td>
<td><a href="/wiki/Piers" title="Piers"><img alt="VSPiers.png" src="//archives.bulbagarden.net/media/upload/thumb/7/77/VSPiers.png/113px-VSPiers.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/7/77/VSPiers.png/170px-VSPiers.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/77/VSPiers.png/226px-VSPiers.png 2x" /></a><br/><a href="/wiki/Piers" title="Piers">Piers</a><br/><small>(initial)</small>
</td></tr>
<tr style="background:#A27DFA">
<td style="background:#border-bottom-left-radius: 10px; -moz-border-radius-bottomleft: 10px; -webkit-border-bottom-left-radius: 10px; -khtml-border-bottom-left-radius: 10px; -icab-border-bottom-left-radius: 10px; -o-border-bottom-left-radius: 10px;;">8
</td>
<td><a href="/wiki/File:Dragon_Gym_logo.png" class="image"><img alt="Dragon Gym logo.png" src="//archives.bulbagarden.net/media/upload/thumb/f/f4/Dragon_Gym_logo.png/50px-Dragon_Gym_logo.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/f/f4/Dragon_Gym_logo.png/75px-Dragon_Gym_logo.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/f/f4/Dragon_Gym_logo.png/100px-Dragon_Gym_logo.png 2x" /></a><br/><a href="/wiki/Hammerlocke_Stadium" title="Hammerlocke Stadium">Hammerlocke Stadium</a>
</td>
<td><a href="/wiki/File:Dragon_Badge.png" class="image"><img alt="Dragon Badge.png" src="//archives.bulbagarden.net/media/upload/thumb/2/27/Dragon_Badge.png/50px-Dragon_Badge.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/2/27/Dragon_Badge.png/75px-Dragon_Badge.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/27/Dragon_Badge.png/100px-Dragon_Badge.png 2x" /></a><br/><a href="/wiki/Badge#Dragon_Badge" title="Badge">Dragon Badge</a>
</td>
<td><a href="/wiki/Dragon_(type)" title="Dragon (type)">Dragon</a>
</td>
<td style="background:#border-bottom-right-radius: 10px; -moz-border-radius-bottomright: 10px; -webkit-border-bottom-right-radius: 10px; -khtml-border-bottom-right-radius: 10px; -icab-border-bottom-right-radius: 10px; -o-border-bottom-right-radius: 10px;;"><a href="/wiki/Raihan" title="Raihan"><img alt="VSRaihan.png" src="//archives.bulbagarden.net/media/upload/thumb/7/70/VSRaihan.png/113px-VSRaihan.png" decoding="async" loading="lazy" width="113" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/7/70/VSRaihan.png/170px-VSRaihan.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/7/70/VSRaihan.png/226px-VSRaihan.png 2x" /></a><br/><a href="/wiki/Raihan" title="Raihan">Raihan</a>
</td></tr></tbody></table>
<h4><span class="mw-headline" id="Paldea">Paldea</span></h4>
<table style="text-align:center; border-radius: 10px; -moz-border-radius: 10px; -webkit-border-radius: 10px; -khtml-border-radius: 10px; -icab-border-radius: 10px; -o-border-radius: 10px;; background:#0B7A0B; border: 4px solid #64D364;" cellspacing="1" cellpadding="2">
<tbody><tr>
<th style="background:#E39091">Order
</th>
<th style="background:#E39091">Gym
</th>
<th style="background:#E39091">Badge
</th>
<th style="background:#E39091">Type
</th>
<th style="background:#E39091">Leader
</th></tr>
<tr style="background:#C6D16E">
<td>1
</td>
<td><a href="/wiki/Cortondo_Gym" title="Cortondo Gym">Cortondo Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Bug.png" class="image"><img alt="SVbadge VictoryRoad Bug.png" src="//archives.bulbagarden.net/media/upload/thumb/9/95/SVbadge_VictoryRoad_Bug.png/50px-SVbadge_VictoryRoad_Bug.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/9/95/SVbadge_VictoryRoad_Bug.png/75px-SVbadge_VictoryRoad_Bug.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/9/95/SVbadge_VictoryRoad_Bug.png/100px-SVbadge_VictoryRoad_Bug.png 2x" /></a><br/><a href="/wiki/Badge#PaldeaBug_Badge" title="Badge">Bug Badge</a>
</td>
<td><a href="/wiki/Bug_(type)" title="Bug (type)">Bug</a>
</td>
<td><a href="/wiki/Katy" title="Katy"><img alt="VSKaty.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d5/VSKaty.png/64px-VSKaty.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d5/VSKaty.png/96px-VSKaty.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d5/VSKaty.png/128px-VSKaty.png 2x" /></a><br/><a href="/wiki/Katy" title="Katy">Katy</a>
</td></tr>
<tr style="background:#A7DB8D">
<td>2
</td>
<td><a href="/wiki/Artazon_Gym" title="Artazon Gym">Artazon Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Grass.png" class="image"><img alt="SVbadge VictoryRoad Grass.png" src="//archives.bulbagarden.net/media/upload/thumb/a/ac/SVbadge_VictoryRoad_Grass.png/50px-SVbadge_VictoryRoad_Grass.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/a/ac/SVbadge_VictoryRoad_Grass.png/75px-SVbadge_VictoryRoad_Grass.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/a/ac/SVbadge_VictoryRoad_Grass.png/100px-SVbadge_VictoryRoad_Grass.png 2x" /></a><br/><a href="/wiki/Badge#PaldeaGrass_Badge" title="Badge">Grass Badge</a>
</td>
<td><a href="/wiki/Grass_(type)" title="Grass (type)">Grass</a>
</td>
<td><a href="/wiki/Brassius" title="Brassius"><img alt="VSBrassius.png" src="//archives.bulbagarden.net/media/upload/thumb/6/6e/VSBrassius.png/64px-VSBrassius.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/6/6e/VSBrassius.png/96px-VSBrassius.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/6/6e/VSBrassius.png/128px-VSBrassius.png 2x" /></a><br/><a href="/wiki/Brassius" title="Brassius">Brassius</a>
</td></tr>
<tr style="background:#FAE078">
<td>3
</td>
<td><a href="/wiki/Levincia_Gym" title="Levincia Gym">Levincia Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Electric.png" class="image"><img alt="SVbadge VictoryRoad Electric.png" src="//archives.bulbagarden.net/media/upload/thumb/f/ff/SVbadge_VictoryRoad_Electric.png/50px-SVbadge_VictoryRoad_Electric.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/f/ff/SVbadge_VictoryRoad_Electric.png/75px-SVbadge_VictoryRoad_Electric.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/f/ff/SVbadge_VictoryRoad_Electric.png/100px-SVbadge_VictoryRoad_Electric.png 2x" /></a><br/><a href="/wiki/Badge#Electric_Badge" title="Badge">Electric Badge</a>
</td>
<td><a href="/wiki/Electric_(type)" title="Electric (type)">Electric</a>
</td>
<td><a href="/wiki/Iono" title="Iono"><img alt="VSIono.png" src="//archives.bulbagarden.net/media/upload/thumb/4/41/VSIono.png/107px-VSIono.png" decoding="async" loading="lazy" width="107" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/4/41/VSIono.png/160px-VSIono.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/41/VSIono.png/214px-VSIono.png 2x" /></a><br/><a href="/wiki/Iono" title="Iono">Iono</a>
</td></tr>
<tr style="background:#9DB7F5">
<td>4
</td>
<td><a href="/wiki/Cascarrafa_Gym" title="Cascarrafa Gym">Cascarrafa Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Water.png" class="image"><img alt="SVbadge VictoryRoad Water.png" src="//archives.bulbagarden.net/media/upload/thumb/4/4f/SVbadge_VictoryRoad_Water.png/50px-SVbadge_VictoryRoad_Water.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/4f/SVbadge_VictoryRoad_Water.png/75px-SVbadge_VictoryRoad_Water.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/4f/SVbadge_VictoryRoad_Water.png/100px-SVbadge_VictoryRoad_Water.png 2x" /></a><br/><a href="/wiki/Badge#PaldeaWater_Badge" title="Badge">Water Badge</a>
</td>
<td><a href="/wiki/Water_(type)" title="Water (type)">Water</a>
</td>
<td><a href="/wiki/Kofu" title="Kofu"><img alt="VSKofu.png" src="//archives.bulbagarden.net/media/upload/thumb/8/80/VSKofu.png/72px-VSKofu.png" decoding="async" loading="lazy" width="72" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/8/80/VSKofu.png/108px-VSKofu.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/8/80/VSKofu.png/144px-VSKofu.png 2x" /></a><br/><a href="/wiki/Kofu" title="Kofu">Kofu</a>
</td></tr>
<tr style="background:#C6C6A7">
<td>5
</td>
<td><a href="/wiki/Medali_Gym" title="Medali Gym">Medali Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Normal.png" class="image"><img alt="SVbadge VictoryRoad Normal.png" src="//archives.bulbagarden.net/media/upload/thumb/d/d6/SVbadge_VictoryRoad_Normal.png/50px-SVbadge_VictoryRoad_Normal.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/d/d6/SVbadge_VictoryRoad_Normal.png/75px-SVbadge_VictoryRoad_Normal.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/d/d6/SVbadge_VictoryRoad_Normal.png/100px-SVbadge_VictoryRoad_Normal.png 2x" /></a><br/><a href="/wiki/Badge#Normal_Badge" title="Badge">Normal Badge</a>
</td>
<td><a href="/wiki/Normal_(type)" title="Normal (type)">Normal</a>
</td>
<td><a href="/wiki/Larry" title="Larry"><img alt="VSLarry.png" src="//archives.bulbagarden.net/media/upload/thumb/b/b0/VSLarry.png/64px-VSLarry.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/b/b0/VSLarry.png/96px-VSLarry.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/b/b0/VSLarry.png/128px-VSLarry.png 2x" /></a><br/><a href="/wiki/Larry" title="Larry">Larry</a>
</td></tr>
<tr style="background:#A292BC">
<td>6
</td>
<td><a href="/wiki/Montenevera_Gym" title="Montenevera Gym">Montenevera Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Ghost.png" class="image"><img alt="SVbadge VictoryRoad Ghost.png" src="//archives.bulbagarden.net/media/upload/thumb/4/4c/SVbadge_VictoryRoad_Ghost.png/50px-SVbadge_VictoryRoad_Ghost.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/4c/SVbadge_VictoryRoad_Ghost.png/75px-SVbadge_VictoryRoad_Ghost.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/4c/SVbadge_VictoryRoad_Ghost.png/100px-SVbadge_VictoryRoad_Ghost.png 2x" /></a><br/><a href="/wiki/Badge#PaldeaGhost_Badge" title="Badge">Ghost Badge</a>
</td>
<td><a href="/wiki/Ghost_(type)" title="Ghost (type)">Ghost</a>
</td>
<td><a href="/wiki/Ryme" title="Ryme"><img alt="VSRyme.png" src="//archives.bulbagarden.net/media/upload/thumb/0/0b/VSRyme.png/79px-VSRyme.png" decoding="async" loading="lazy" width="79" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/0/0b/VSRyme.png/118px-VSRyme.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/0/0b/VSRyme.png/157px-VSRyme.png 2x" /></a><br/><a href="/wiki/Ryme" title="Ryme">Ryme</a>
</td></tr>
<tr style="background:#FA92B2">
<td>7
</td>
<td><a href="/wiki/Alfornada_Gym" title="Alfornada Gym">Alfornada Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Psychic.png" class="image"><img alt="SVbadge VictoryRoad Psychic.png" src="//archives.bulbagarden.net/media/upload/thumb/2/2d/SVbadge_VictoryRoad_Psychic.png/50px-SVbadge_VictoryRoad_Psychic.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/2/2d/SVbadge_VictoryRoad_Psychic.png/75px-SVbadge_VictoryRoad_Psychic.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/2/2d/SVbadge_VictoryRoad_Psychic.png/100px-SVbadge_VictoryRoad_Psychic.png 2x" /></a><br/><a href="/wiki/Badge#PaldeaPsychic_Badge" title="Badge">Psychic Badge</a>
</td>
<td><a href="/wiki/Psychic_(type)" title="Psychic (type)">Psychic</a>
</td>
<td><a href="/wiki/Tulip" title="Tulip"><img alt="VSTulip.png" src="//archives.bulbagarden.net/media/upload/thumb/b/b5/VSTulip.png/91px-VSTulip.png" decoding="async" loading="lazy" width="91" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/b/b5/VSTulip.png/137px-VSTulip.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/b/b5/VSTulip.png/182px-VSTulip.png 2x" /></a><br/><a href="/wiki/Tulip" title="Tulip">Tulip</a>
</td></tr>
<tr style="background:#BCE6E6">
<td>8
</td>
<td><a href="/wiki/Glaseado_Gym" title="Glaseado Gym">Glaseado Gym</a>
</td>
<td><a href="/wiki/File:SVbadge_VictoryRoad_Ice.png" class="image"><img alt="SVbadge VictoryRoad Ice.png" src="//archives.bulbagarden.net/media/upload/thumb/4/46/SVbadge_VictoryRoad_Ice.png/50px-SVbadge_VictoryRoad_Ice.png" decoding="async" loading="lazy" width="50" height="50" srcset="//archives.bulbagarden.net/media/upload/thumb/4/46/SVbadge_VictoryRoad_Ice.png/75px-SVbadge_VictoryRoad_Ice.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/4/46/SVbadge_VictoryRoad_Ice.png/100px-SVbadge_VictoryRoad_Ice.png 2x" /></a><br/><a href="/wiki/Badge#PaldeaIce_Badge" title="Badge">Ice Badge</a>
</td>
<td><a href="/wiki/Ice_(type)" title="Ice (type)">Ice</a>
</td>
<td><a href="/wiki/Grusha" title="Grusha"><img alt="VSGrusha.png" src="//archives.bulbagarden.net/media/upload/thumb/c/c3/VSGrusha.png/64px-VSGrusha.png" decoding="async" loading="lazy" width="64" height="64" srcset="//archives.bulbagarden.net/media/upload/thumb/c/c3/VSGrusha.png/96px-VSGrusha.png 1.5x, //archives.bulbagarden.net/media/upload/thumb/c/c3/VSGrusha.png/128px-VSGrusha.png 2x" /></a><br/><a href="/wiki/Grusha" title="Grusha">Grusha</a>
</td></tr>
</html>
</body>"""
soup = BeautifulSoup(html_doc, 'html.parser')

regions = soup.find_all('h4')
tables = soup.find_all('table')

gymHeaders = ["name", "type", "region", "gym_number", "badge_name"]
gymData = []

trainerHeaders = ["name", "gym_name", "gym_type", "region"]
trainerData = []

pokemonHeaders = ["pokedex_number", "name", "attack", "defense", "hp", "sp_attack", "sp_defense", "speed", "weight", "generation", "is_legendary"]
pokemonData = []

pokemonTypeHeaders = ["pokedex_number", "type_name"]
pokemonTypeData = []

trainerOwnsHeaders = ["pokedex_number", "trainer_region", "trainer_name"]
trainerOwnsData = []

trainerMap = {}
pokemonMap = {}

for i in range(len(regions)):
    region = regions[i].get_text()
    table = tables[i]
    cols = table.find_all('th')
    rows = table.find_all('tr')[1:]
    for row in rows:
        entries = row.find_all('td')
        currentRow = []
        currentRow.append(entries[0].get_text()[0])
        currentRow[0] = int(currentRow[0])
        for i in range(1, len(cols)):
            currentRow.append(entries[i].get_text()[:-1])
            if i == len(cols) - 1:
                trainer = entries[4].get_text()[:-1]
                if "(" in trainer:
                    trainer = trainer.split("(")[0]
                currentRow[-1] = trainer
        trainer = entries[4].get_text()[:-1]
        if "(" in trainer:
            trainer = trainer.split("(")[0]
        trainerMap[trainer] = [currentRow[1], currentRow[3]]
        currentRow = [currentRow[1], currentRow[3], region, currentRow[0], currentRow[2]]
        gymData.append(currentRow)
print(gymData[0:6])
print("================")
pokemonTypes = set()
with open("pokemon_downloaded.csv", newline='') as csvfile:
    pokemonReader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in pokemonReader:
        pokemonData.append([int(row[4]), row[3], int(row[0]), int(row[1]), int(row[2]), int(row[5]), int(row[6]), int(row[7]), float(row[10]) if len(row[10])>0 else '', int(row[11]), int(row[12])])
        pokemonMap[row[3]] = int(row[4])
        for i in range(8, 10):
            if len(row[i]) > 0 and (int(row[4]), row[i]) not in pokemonTypes:
                pokemonTypeData.append([int(row[4]), row[i]])
                pokemonTypes.add((int(row[4]), row[i]))
print(pokemonData[0:6])
print("================")
print(pokemonTypeData[0:12])
print("================")

with open('Trainers.csv', newline='') as csvfile:
        trainerReader = csv.reader(csvfile, delimiter=',')
        for row in trainerReader: #name[0], pokemon[1:6], type[7], keystone[8], region[9]
            currentRow = []
            currentRow.append(row[0])
            if row[0] in trainerMap:
                currentRow.append(trainerMap[row[0]][0])
                currentRow.append(trainerMap[row[0]][1])
            else:
                currentRow.append('')
                currentRow.append('')
            currentRow.append(row[-1])
            trainerData.append(currentRow)
            for i in range(1, 7):
                if row[i] in pokemonMap:
                    trainerOwnsData.append([pokemonMap[row[i]], row[-1], row[0]])
print(trainerData[0:6])
print("================")
print(trainerOwnsData[0:12])
print("================")

with open('./outputCSVs/gym.csv', 'w', newline='') as csvfile:
    typesWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    typesWriter.writerow(gymHeaders)
    for row in gymData:
        typesWriter.writerow(row)
        
with open('./outputCSVs/trainer.csv', 'w', newline='') as csvfile:
    typesWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    typesWriter.writerow(trainerHeaders)
    for row in trainerData:
        typesWriter.writerow(row)

with open('./outputCSVs/pokemon.csv', 'w', newline='') as csvfile:
    typesWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    typesWriter.writerow(pokemonHeaders)
    for row in pokemonData:
        typesWriter.writerow(row)

with open('./outputCSVs/pokemon_type.csv', 'w', newline='') as csvfile:
    typesWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    typesWriter.writerow(pokemonTypeHeaders)
    for row in pokemonTypeData:
        typesWriter.writerow(row)
        
with open('./outputCSVs/trainer_owns.csv', 'w', newline='') as csvfile:
    typesWriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    typesWriter.writerow(trainerOwnsHeaders)
    for row in trainerOwnsData:
        typesWriter.writerow(row)