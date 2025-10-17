# 1 - Model Performance Comparison
To assess the performance of VGGFace2 and CASIA-WebFace, we compare them using the mAP (Mean Average Precision) metric. This metric is superior as it not only measures whether relevant identities are retrieved, but also incorporates the ranking of those identities—penalizing cases where true matches are pushed further down the list. Unlike plain precision, which treats a correct match at rank 1 the same as one at rank 5, mAP rewards models that consistently place relevant items higher in the ranking. Furthermore, it increases as a greater proportion of all relevant identities are included in the retrieved set, making it a more comprehensive evaluation of retrieval quality.

### Results
**Table 1.** Comparison of mAP for VGGFace2 and CASIA-WebFace under different environmental noise conditions on the IronClad dataset.

| Condition              | VGGFace2 mAP | CASIA-WebFace mAP |
|------------------------|--------------|-------------------|
| No environmental noise | 0.6463       | 0.3726            |
| Gaussian blur          | 0.5575       | 0.2677            |
| Resizing               | 0.6278       | 0.3678            |
| Brightness adjustment  | 0.5506       | 0.3561            |

Table 1 reports the Mean Average Precision (mAP) for VGGFace2 and CASIA-WebFace across four environmental conditions using a BruteForce nearest neighbor search with Euclidean distance. Across all conditions, VGGFace2 outperforms CASIA-WebFace by approximately 0.2–0.3 mAP. This trend is consistent regardless of whether noise is introduced.

### Impact of Environmental Noise
Environmental degradations reduce performance for both models, but the relative gap between the two remains stable. Here is how the different environment noises impact the model:

* **Gaussian blur:** VGGFace2 drops from 0.6463 to 0.5575 (−13.7%) and CASIA-WebFace drops from 0.3726 to 0.2677 (−28.2%). Generally, VGGFace2 is more resilient to this type of noise than CASIA-WebFace.
* **Resizing:** VGGFace2 is minimally affected from 0.6463 to 0.6278 (−2.9%), while CASIA-WebFace also shows a small reduction from 0.3726 to 0.3678 (−1.3%). This means that both models are generally resilient towards this type of noise.
* **Brightness adjustment:** Both models degrade substantially, with VGGFace2 falling 14.8% and CASIA-WebFace 4.4%. Generally CASIA-WebFace is more resilient to this type of noise than VGGFace2, although VGGFace2 still beats CASIA-WebFace in raw accuracy.


### Model Selection Argument
VGGFace2 achieves higher accuracy under both the baseline condition (no environmental noise) and the more severe noise settings (Gaussian blur, brightness). CASIA-WebFace demonstrates consistently lower mAP values. Therefore, VGGFace2 should be selected.

# 2
VGG FACE, euclidean metric

CPU = Intel Core i5-11600k

**Table 2.** Comparison of Brute Force, HNSW, and LSH methods on PC in terms of identity addition time, memory footprint, query speed, and retrieval accuracy (mAP).

| Metric                  | Brute Force | HNSW (PC) | LSH (PC) |
|-------------------------|-------------|-----------|----------|
| Time Add Identities (s) | 0.0602      | 0.3072    | 0.1590   |
| Mem footprint (GB)      | 0.0043      | 0.0049    | 0.0003   |
| Time Query Probes (s/q) | 0.2522      | 0.1728    | 0.1130   |
| Max queries/s           | 3.9658      | 5.7867    | 8.8480   |
| mAP                     | 0.6463      | 0.5575    | 0.3862   |


# 3


## VGGFace2 and Brute Force
**Table 3-1.** Comparison of performance on different k values using VGGFace2 and Brute Force Index.

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.7087 | 0.3316             | 3.0161        |
| 2 | 0.6789 | 0.3319             | 3.0128        |
| 3 | 0.6619 | 0.3357             | 2.9793        |
| 4 | 0.6528 | 0.3706             | 2.6986        |
| 5 | 0.6463 | 0.3569             | 2.8017        |
| 6 | 0.6392 | 0.3634             | 2.7520        |

## VGGFace2 and HNSW
**Table 3-2.** Comparison of performance on different k values using VGGFace2 and HNSW Index.

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.7087 | 0.1659             | 6.0278        |
| 2 | 0.6784 | 0.1678             | 5.9587        |
| 3 | 0.6617 | 0.1672             | 5.9807        |
| 4 | 0.6524 | 0.1723             | 5.8050        |
| 5 | 0.6459 | 0.1718             | 5.8214        |
| 6 | 0.6388 | 0.1727             | 5.7896        |

## VGGFace2 and LSH
**Table 3-3.** Comparison of performance on different k values using VGGFace2 and LSH Index.

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.4875 | 0.0947             | 10.5600       |
| 2 | 0.4940 | 0.0953             | 10.4949       |
| 3 | 0.4903 | 0.0951             | 10.5118       |
| 4 | 0.4834 | 0.0961             | 10.4013       |
| 5 | 0.4790 | 0.0961             | 10.4018       |
| 6 | 0.4754 | 0.0970             | 10.3104       |

## CASIA-WebFace and Brute Force
**Table 3-4.** Comparison of performance on different k values using CASIA-WebFace and Brute Force Index.

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.3624 | 0.1902             | 5.2567        |
| 2 | 0.3774 | 0.1920             | 5.2077        |
| 3 | 0.3732 | 0.1964             | 5.0921        |
| 4 | 0.3697 | 0.1935             | 5.1669        |
| 5 | 0.3687 | 0.1934             | 5.1708        |
| 6 | 0.3651 | 0.1949             | 5.1306        |

## CASIA-WebFace and HNSW
**Table 3-5.** Comparison of performance on different k values using CASIA-WebFace and HNSW Index.

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.3624 | 0.1796             | 5.5679        |
| 2 | 0.3774 | 0.1827             | 5.4734        |
| 3 | 0.3732 | 0.1829             | 5.4670        |
| 4 | 0.3697 | 0.1829             | 5.4664        |
| 5 | 0.3687 | 0.1844             | 5.4216        |
| 6 | 0.3651 | 0.1818             | 5.4998        |

## CASIA-WebFace and LSH
**Table 3-6.** Comparison of performance on different k values using CASIA-WebFace and LSH Index.

| k | mAP    | Time per Query (s) | Max Queries/s |
|---|--------|--------------------|---------------|
| 1 | 0.1211 | 0.0981             | 10.1894       |
| 2 | 0.1421 | 0.0940             | 10.6393       |
| 3 | 0.1481 | 0.0919             | 10.8850       |
| 4 | 0.1532 | 0.0949             | 10.5355       |
| 5 | 0.1548 | 0.0961             | 10.4065       |
| 6 | 0.1564 | 0.0967             | 10.3460       |

# 4

## VGGFace
![VGGFace Results](imgs/task4-vggface.png)


## TODO - CASIA-WebFace

# 5
Worst Performing Identities: ['Inam-ul-Haq', 'Mark_Cuban', 'Carl_Reiner', 'Demetrius_Ferraciu', 'Max_Mayfield', 'Charles_Schumer', 'David_Wolf', 'Johnny_Depp', 'Jada_Pinkett_Smith', 'Jorge_Batlle', 'Mariah_Carey', 'John_Walsh', 'Claire_Danes', 'Edward_Lu', 'Emile_Lahoud', 'Ernie_Fletcher', 'Mario_Dumont', 'Charlie_Zaa', 'Peter_Arnett', 'Steve_Waugh', 'Warren_Buffett', 'Marcus_Gronholm', 'Thabo_Mbeki', 'Robby_Ginepri', 'Hootie_Johnson', 'Joseph_Ralston', 'Susan_Collins', 'Jon_Gruden', 'Gabriel_Valdes', 'Sean_Astin', 'Jim_Edmonds', 'Lindsey_Graham', 'Butch_Davis', 'Steve_Spurrier', 'Paul_Patton', 'George_Ryan', 'Katie_Harman', 'Daryl_Hannah', 'Felix_Mantilla', 'Kathryn_Bigelow', 'Kosuke_Kitajima', 'Phil_Vassar', 'Maria_Luisa_Mendonca', 'Priscilla_Owen', 'Guillaume_Soro', 'Franz_Beckenbauer', 'James_Franco', 'Beth_Jones', 'John_McEnroe', 'Drew_Barrymore', 'Kirk_Ferentz', 'Laila_Ali', 'Larry_Lindsey', 'Kristanna_Loken', 'Rob_Schneider', 'George_Voinovich', 'Nasser_al-Kidwa', 'Marissa_Jaret_Winokur', 'Chris_Byrd', 'Flavia_Delaroli', 'Tomoko_Hagiwara', 'Juan_Valencia_Osorio', 'John_Taylor', 'Gary_Winnick', 'Justin_Guarini', 'Lon_Kruger', 'Franz_Muentefering', 'Chok_Tong_Goh', 'Cesar_Maia', 'Garry_Trudeau', 'Brendan_Hansen', 'Darrell_Issa', 'Alejandro_Avila', 'Shannon_OBrien', 'Hichiro_Naemura', 'Dennis_Powell', 'Franco_Dragone', 'Patrick_Leahy', 'Michelle_Pfeiffer', 'Jim_Carrey', 'Mary_Landrieu', 'Nora_Bendijo', 'John_F_Kennedy_Jr', 'Vince_Carter', 'Arnaud_Clement', 'David_Leahy', 'Howard_Smith', 'Chung_Mong-joon', 'James_Parker', 'Cristina_Fernandez', 'James_Kopp', 'Jefferson_Perez', 'Stephen_Friedman', 'Darren_Clarke', 'Hashim_Thaci', 'Carlos_Bianchi', 'Jimmy_Carter', 'Jamie_Villafane', 'Dennis_Kozlowski', 'Augusto_Roa_Bastos', 'Richard_Crenna', 'Mark_Geragos', 'Christine_Gregoire', 'Miguel_Contreras', 'Jean-Claude_Braquet', 'Chris_Tucker', 'Mario_Kreutzberger', 'James_Jones', 'James_Gandolfini', 'Eunice_Barber', 'Aldo_Paredes', 'Yukiko_Okudo', 'Elvis_Presley', 'Jesse_James_Leija', 'Mike_Miller', 'Jude_Law', 'Vaclav_Havel', 'Christopher_Patten', 'Brian_Heidik', 'Howard_Schultz', 'Ellen_Engleman', 'Paul_Byrd', 'Jean-Sebastien_Giguere', 'Gillian_Anderson', 'Doug_Collins', 'Charles_Mathews', 'Celso_Amorim', 'Todd_Haynes', 'Edward_Said', 'Emily_Robison', 'Nanni_Moretti', 'Anna_Nicole_Smith', 'Gary_Doer', 'Leslie_Moonves', 'John_Garamendi', 'Warren_Beatty', 'Begum_Khaleda_Zia', 'David_Myers', 'Flor_Montulo', 'Jane_Fonda', 'Ben_Curtis', 'Freddy_Garcia', 'Annette_Lu', 'Hal_Sutton', 'Andrew_Niccol', 'Leszek_Miller', 'Martina_Hingis', 'John_McCallum', 'Dave_Campo', 'Tamara_Brooks', 'Iban_Mayo', 'Courtney_Love', 'Melanie_Griffith', 'Alberto_Ruiz_Gallardon', 'Wesley_Clark', 'Jose_Dirceu', 'Stanley_Tong', 'Frank_Lautenberg', 'Chang_Dae-whan', 'Gordon_Campbell', 'David_Spade', 'Charles_Grassley', 'Lina_Krasnoroutskaya', 'Charlotte_Rampling', 'Bill_Sizemore', 'Ricky_Ponting', 'Sheila_Wellstone', 'Joe_Gatti', 'Goran_Persson', 'Lou_Piniella', 'Tammy_Lynn_Michaels', 'Ferenc_Madl', 'Bernardo_Segura', 'Derek_Lowe', 'Andrew_Cuomo', 'Maggie_Smith', 'Monica_Seles', 'Hermann_Maier', 'Ricardo_Maduro', 'Michael_Ballack', 'Barry_Alvarez', 'Prince_Edward', 'Henrique_Meirelles', 'Amram_Mitzna', 'Andrew_Bunner', 'Alexandra_Vodjanikova', 'Lionel_Richie', 'Denise_Johnson', 'Edward_Norton', 'Janica_Kostelic', 'Darrell_Porter', 'Jong_Thae_Hwa', 'Diana_Taurasi', 'Jessica_Alba', 'Christina_Aguilera', 'Reese_Witherspoon', 'Matthew_Perry', 'Barry_Zito', 'Nicolas_Lapentti', 'Scott_McNealy', 'Gao_Qiang', 'William_Martin', 'James_Traficant', 'Bill_Parcells', 'Brian_Wells', 'Dai_Bachtiar', 'Gil_de_Ferran', 'Kurt_Busch', 'Zarai_Toledo', 'Gro_Harlem_Brundtland', 'Thomas_OBrien', 'Jean-Claude_Juncker', 'Don_Nickles', 'Doug_Duncan', 'Emma_Thompson', 'John_Cusack', 'Pete_Rose', 'Dan_Wheldon', 'Elisabeth_Schumacher', 'Michael_Kostelnik', 'Adrian_McPherson', 'Greg_Ostertag', 'George_Brumley', 'Roman_Polanski', 'Matt_Doherty', 'Adam_Scott', 'Alicia_Silverstone', 'Hun_Sen', 'Adolfo_Rodriguez_Saa', 'Charles_Kartman', 'Zhang_Ziyi', 'Peter_Greenaway', 'Ian_McKellen', 'Edie_Falco', 'Isaiah_Washington', 'Brian_Mulroney', 'Daniela_Hantuchova', 'Manuel_Poggiali', 'Megawati_Sukarnoputri', 'Franko_Simatovic', 'Frances_Fisher', 'Vanessa_Williams', 'Kate_Capshaw', 'Paul_Pierce', 'Guy_Hemmings', 'Tom_Brady', 'Morgan_Freeman', 'Marisa_Tomei', 'Elijah_Wood', 'John_Ruiz', 'John_Rosa', 'Geno_Auriemma', 'Daisy_Fuentes', 'Abdullatif_Sener', 'Luis_Gonzalez_Macchi', 'Ricky_Barnes', 'Arianna_Huffington', 'Angela_Lansbury', 'George_P_Bush', 'Lily_Tomlin', 'Jerry_Falwell', 'Chung_Mong-hun', 'Latrell_Sprewell', 'Jolanta_Kwasniewski', 'Prince_Willem-Alexander', 'Ahmad_Masood', 'Iva_Majoli', 'Ken_Watanabe', 'Thomas_Birmingham', 'William_Hochul', 'Richard_Norton-Taylor', 'Richie_Adubato', 'Jan_Ullrich', 'Princess_Aiko', 'Jessica_Lynch', 'Thierry_Falise', 'Ishaq_Shahryar', 'Mel_Brooks', 'Dick_Vermeil', 'Priscilla_Presley', 'Marlene_Weingartner', 'Fred_Funk', 'Robin_McLaurin_Williams', 'Dick_Cheney', 'Mohamed_Benaissa', 'John_Rowland', 'Lech_Walesa', 'Hideki_Matsui', 'Joe_Dumars', 'Jessica_Lange', 'Jimmy_Kimmel']

Best Performing Identities: ['Bobby_Goldwater', 'Yoko_Ono', 'Slobodan_Milosevic', 'Saeb_Erekat', 'Richard_Branson', 'Bob_Colvin', 'Billy_Graham', 'Lauren_Killian', 'Mary_Tyler_Moore', 'Leslie_Ann_Woodward', 'Kathleen_Kennedy_Townsend', 'Patrice_Chereau', 'Kathleen_Glynn', 'Lawrence_MacAulay', 'Tyler_Hamilton', 'Bill_Simon', 'Serena_Williams', 'David_Dodge', 'Lim_Dong-won', 'Gray_Davis', 'Hassan_Wirajuda', 'Carol_Moseley_Braun', 'Will_Smith', 'Greg_Gilbert', 'Thomas_Fargo', 'Christine_Ebersole', 'Gwendal_Peizerat', 'Meryl_Streep', 'Pat_Cox', 'Larry_Brown', 'Abdullah_al-Attiyah', 'Patti_Labelle', 'James_Smith', 'Klaus_Zwickel', 'Hitomi_Soga', 'Alice_Fisher', 'Martin_Scorsese', 'Takashi_Sorimachi', 'Eddie_Sutton', 'Liza_Minnelli', 'Leander_Paes', 'Gloria_Allred', 'Steven_Spielberg', 'Pete_Sampras', 'David_Kelley', 'Bud_Selig', 'Camilla_Parker_Bowles', 'Sean_Penn', 'Nadine_Vinzens', 'Art_Howe', 'Mack_Brown', 'John_Banko', 'Bode_Miller', 'Vanessa_Incontrada', 'Sandra_Bullock', 'Alimzhan_Tokhtakhounov', 'Art_Hoffmann', 'Jose_Viegas_Filho', 'Jorge_Arce', 'Lyle_Vanclief', 'Alastair_Campbell', 'Wang_Yingfan', 'Juergen_Peters', 'Chris_Cooper', 'Joerg_Haider', 'Lord_Hutton', 'Jodie_Foster', 'Rita_Wilson', 'Ozzy_Osbourne', 'Herta_Daeubler-Gmelin', 'Carlos_Mesa', 'Ellen_DeGeneres', 'Ernie_Eves', 'John_Reilly', 'Guido_Westerwelle', 'Gregory_Hines', 'Jamling_Norgay', 'James_Morris', 'Boris_Berezovsky', 'Alexandra_Stevenson', 'Boris_Becker', 'Duane_Lee_Chapman', 'Dolly_Parton', 'John_Stallworth', 'Frank_Stallone', 'Sourav_Ganguly', 'Spencer_Abraham', 'Emmanuelle_Beart', 'Jennifer_Rodriguez', 'Roy_Moore', 'Paul_McCartney', 'Mary-Kate_Olsen', 'Nick_Nolte', 'Marcelo_Salas', 'Marilyn_Monroe', 'Bijan_Namdar_Zangeneh', 'Julianna_Margulies', 'Mike_Tyson', 'John_Jumper', 'Colin_Jackson', 'Guy_Ritchie', 'Julie_Taymor', 'Joan_Claybrook', 'Richard_Gephardt', 'Joseph_Estrada', 'Mike_Holmgren', 'Laurent_Gbagbo', 'Kirk_Johnson', 'Robert_Kocharian', 'Michael_Douglas', 'Paulo_Cesar_Pinheiro', 'John_Timoney', 'Pedro_Solbes', 'Carolina_Moraes', 'Alejandro_Toledo', 'Magui_Serna', 'Jack_Grubman', 'Prince_Harry', 'Aleksander_Kwasniewski', 'Pupi_Avati', 'Margaret_Thatcher', 'Aung_San_Suu_Kyi', 'Peter_Bacanovic', 'Nicanor_Duarte_Frutos', 'David_Heymann', 'Luiz_Felipe_Scolari', 'Jason_Alexander', 'Annette_Bening', 'Tom_Craddick', 'Karen_Mok', 'Bruce_Weber', 'Julie_Gerberding', 'Patricia_Heaton', 'Frank_Solich', 'Gustavo_Kuerten', 'Gloria_Macapagal_Arroyo', 'Eva_Dimas', 'Jean-Marc_de_La_Sabliere', 'Mikhail_Youzhny', 'Justin_Leonard', 'Thaksin_Shinawatra', 'Cathy_Freeman', 'Bob_Geldof', 'Jay_Rasulo', 'Corinne_Coman', 'Amanda_Beard', 'Larry_Bowa', 'Geraldine_Chaplin', 'Rita_Moreno', 'Benazir_Bhutto', 'Gunter_Pleuger', 'Biljana_Plavsic', 'Lisa_Gottsegen', 'Theo_Epstein', 'Augustin_Calleri', 'Ibrahim_Jaafari', 'Asa_Hutchinson', 'Erika_Christensen', 'James_Blake', 'Nancy_Pelosi', 'Kenneth_Branagh', 'Prince_Naruhito', 'Georgi_Parvanov', 'Jacqueline_Obradors', 'Jia_Qinglin', 'Mitchell_Daniels', 'Andy_Hebb', 'Laura_Hernandez', 'Natalie_Maines', 'Mikhail_Kasyanov', 'Candie_Kung', 'Kathy_Winters', 'Alex_Barros', 'Intisar_Ajouri', 'Mark_Warner', 'Paul_ONeill', 'Elsa_Zylberstein', 'Abdullah', 'Blythe_Hartley', 'Paula_Radcliffe', 'Vitali_Klitschko', 'Valery_Giscard_dEstaing', 'Sean_Patrick_OMalley', 'Joe_Calzaghe', 'Miyako_Miyazaki', 'Pedro_Malan', 'Aaron_Sorkin', 'Michael_Chang', 'Xanana_Gusmao', 'Jose_Manuel_Durao_Barroso', 'Rolf_Eckrodt', 'Sam_Bith', 'Carlos_Manuel_Pruneda', 'Jeffrey_Jones', 'Ben_Glisan', 'Brian_Cowen', 'Larry_Ellison', 'Mary_Carey', 'Al_Davis', 'Padraig_Harrington', 'Jason_Kidd', 'Augusto_Pinochet', 'Alejandro_Atchugarry', 'Bill_Nelson', 'Elinor_Caplan', 'Jean-David_Levitte', 'Christian_Wulff', 'Keira_Knightley', 'Raquel_Welch', 'Ali_Khamenei', 'Chen_Liang_Yu', 'Phil_Mickelson', 'Nancy_Reagan', 'Bernard_Landry', 'Gerry_Adams', 'David_Trimble', 'Iain_Duncan_Smith', 'Ann_Veneman', 'Robin_Cook', 'Branko_Crvenkovski', 'Arantxa_Sanchez-Vicario', 'Vidar_Helgesen', 'Lisa_Ling', 'Trent_Lott', 'Tom_Daschle', 'Barbra_Streisand', 'Martha_Burk', 'Michelle_Yeoh', 'Desiree_Lemosi', 'Mikulas_Dzurinda', 'Kim_Dae-jung', 'Richard_Sambrook', 'Juan_Pablo_Montoya', 'Madonna', 'Fabiola_Zuluaga', 'Barbara_Brezigar', 'Nastassia_Kinski', 'Tyra_Banks', 'Gregory_Geoffroy', 'Mark_Schweiker', 'Tom_Glavine', 'Rupert_Grint', 'Alexander_Rumyantsev', 'Francis_George', 'Hu_Jintao', 'Cruz_Bustamante', 'Robert_Mueller', 'Jennifer_Reilly', 'Rick_Romley', 'Natalie_Coughlin', 'Chris_Bell', 'Donald_Evans', 'Miroljub', 'Ron_Dittemore', 'Costas_Simitis', 'S_Jayakumar', 'Bo_Pelini', 'Harry_Schmidt', 'Venus_Williams', 'Silvia_Farina_Elia', 'Jose_Theodore', 'Angelo_Reyes', 'Dwayne_Johnson', 'Len_Jenoff', 'George_Robertson', 'Billy_Sollie', 'Hilmi_Ozkok', 'Federico_Trillo', 'Yao_Ming', 'Ruben_Studdard', 'Paul_William_Hurley', 'Kim_Ryong-sung', 'Juan_Manuel_Marquez', 'Abdullah_Gul', 'Simon_Cowell', 'Frank_Cassell', 'Grady_Irvin_Jr', 'Peter_Hillary', 'Bob_Beauprez', 'Alison_Lohman', 'Allen_Iverson', 'Elizabeth_Dole', 'Donna_Shalala', 'Justine_Henin', 'Benjamin_Netanyahu', 'Ron_Howard', 'Jose_Sarney', 'Sheila_Copps', 'Aitor_Gonzalez', 'Julio_Iglesias_Jr', 'Lauren_Hutton', 'Valdas_Adamkus', 'Frank_Dunham_Jr', 'Kiki_Vandeweghe', 'Martha_Bowen', 'Dennis_Erickson', 'Tracee_Ellis_Ross', 'James_Kelly', 'Herb_Sendek', 'Tony_Curtis', 'Anibal_Ibarra', 'James_Cunningham', 'Elizabeth_Shue', 'Harbhajan_Singh', 'Ahmet_Necdet_Sezer', 'Bob_Hope', 'James_Ivory', 'Gary_Locke', 'George_Karl', 'Dolma_Tsering', 'Lynn_Abraham', 'Marwan_Barghouthi', 'Garry_Kasparov', 'Fran_Drescher', 'Juanes', 'Scott_McClellan', 'Bobby_Robson', 'Kristin_Davis', 'Betsy_Smith', 'Guillermo_Ortiz', 'Kelli_White', 'Joseph_Biden', 'Lee_Hoi-chang', 'Kenneth_Evans', 'Bruce_Van_De_Velde', 'Marco_Antonio_Barrera', 'Inocencio_Arias', 'Job_Cohen', 'Sue_Wicks', 'Arsinee_Khanjian', 'Gary_Bergeron', 'Aron_Ralston', 'George_Pataki', 'Elizabeth_Smart', 'George_Foreman', 'Dennis_Kucinich', 'Donatella_Versace', 'Judi_Dench', 'Geoff_Hoon', 'Pascal_Quignard', 'Bill_Frist', 'Paul_Bremer', 'Mariangel_Ruiz_Torrealba', 'Manfred_Stolpe', 'Vicki_Zhao_Wei', 'John_Negroponte', 'Anders_Fogh_Rasmussen', 'Carlos_Quintanilla_Schmidt', 'Lee_Tae-sik', 'Robert_Stack', 'John_Snow', 'Harvey_Weinstein', 'Albrecht_Mentz', 'Jennifer_Connelly', 'Kwon_Yang-sook', 'Jennifer_Lopez', 'Kemal_Dervis', 'Stacy_Dragila', 'Alberto_Fujimori', 'Stellan_Skarsgard', 'Kent_Rominger', 'Dino_de_Laurentis', 'Nadia_Petrova', 'John_Rigas', 'Gerardo_Gambala', 'Kieran_Prendergast', 'Tom_Crean', 'Arlen_Specter', 'Jackie_Chan', 'David_Heyman', 'Kim_Jin-sun', 'Tim_Floyd', 'Alan_Ball', 'Emanuel_Ginobili', 'Ali_Abbas', 'Carmen_Electra', 'Cyndi_Thompson', 'Jane_Kaczmarek', 'Jesse_Jackson', 'Jorge_Rodolfo_Canicoba_Corral', 'Kifah_Ajouri', 'Carlo_Ancelotti', 'Arye_Mekel', 'Isabelle_Huppert', 'Bashar_Assad', 'James_Butts', 'Johnny_Unitas', 'Queen_Beatrix', 'Ian_Thorpe', 'Brigitte_Boisselier', 'Adrian_Nastase', 'Gabriel_Batistuta', 'Jonathan_Mostow', 'Sarah_Jessica_Parker', 'Anwar_Ibrahim', 'Gerard_Depardieu', 'Debra_Brown', 'Jeffrey_Scott_Postell', 'Roy_Williams', 'Doris_Schroeder', 'Christopher_Walken', 'Mitoji_Yabunaka', 'Peter_Harrison', 'David_Bell', 'Fred_Eckhard', 'William_Bratton', 'Jorge_Valdano', 'Amanda_Coetzer', 'Conchita_Martinez', 'Jennifer_Thompson', 'Carlos_Ghosn', 'Sally_Kirkland', 'Chris_Rock', 'Sam_Torrance', 'Valerie_Harper', 'Robert_Mugabe', 'Bill_Callahan', 'Patricia_Clarkson', 'Leon_LaPorte', 'Johnny_Carson', 'James_Schultz', 'Judy_Genshaft', 'OJ_Simpson', 'Peter_Struck', 'Mike_Weir', 'LeBron_James', 'Lino_Oviedo', 'Jim_Furyk', 'Evander_Holyfield', 'Eric_Clapton', 'Arnold_Palmer', 'Janet_Thorpe', 'John_Blaney', 'Meghann_Shaughnessy', 'Lloyd_Ward', 'Albert_Costa', 'Liu_Mingkang', 'Hassan_Nasrallah', 'Dale_Earnhardt_Jr', 'John_Wolf', 'Eddy_Merckx', 'Lee_Jun', 'Ilan_Ramon', 'Anders_Ebbeson', 'Eve_Pelletier', 'Jean_Carnahan', 'Julianne_Moore', 'Barrett_Jackman', 'Hannah_Stockbauer', 'Oscar_De_La_Hoya', 'Helen_Clark', 'Alex_Penelas', 'Michael_J_Sheehan', 'George_Tenet', 'Olesya_Bonabarenko', 'Patrick_Ewing', 'Chanda_Rubin', 'Larry_Johnson', 'Igor_Ivanov', 'Cameron_Diaz', 'Marc_Grossman', 'Joseph_Deiss', 'Mathias_Reichhold', 'Jennifer_Aniston', 'Alan_Mulally', 'Monica_Bellucci', 'Hanan_Ashrawi', 'Martina_McBride', 'Mark_Heller', 'Li_Peng', 'John_McCormack', 'John_Spencer', 'Michael_Phelps', 'Tim_Allen', 'Kurt_Russell', 'Luis_Horna', 'Robert_De_Niro', 'Mohammad_Khatami', 'Damon_van_Dam', 'Doris_Roberts', 'Scott_Rudin', 'Silvio_Berlusconi', 'John_Manley', 'Gary_Carter', 'Andrei_Mikhnevich', 'David_Caraway', 'Dorthy_Moxley', 'Guillermo_Coria', 'Vladimir_Putin', 'Adolfo_Aguilar_Zinser', 'Marat_Safin', 'Michael_Chiklis', 'Lindsay_Benko', 'Luciano_Pavarotti', 'Vicente_Fernandez', 'Lynne_Cheney', 'Jeffrey_Immelt', 'Brooke_Shields', 'GL_Peiris', 'Greg_Owen', 'Nelson_Mandela', 'Tom_Cruise', 'Boris_Yeltsin', 'Alexander_Losyukov', 'Chuck_Amato', 'Mark_Dacey', 'Ray_Nagin', 'Cindy_Margolis', 'Jose_Serra', 'Jason_Lezak', 'Howard_Dean', 'Brian_Griese', 'Yasar_Yakis', 'Lisa_Raymond', 'Joe_Nichols', 'Jay_Garner', 'Hector_Babenco', 'Martin_Verkerk', 'John_Howard', 'Nia_Vardalos', 'Marc-Andre_Fleury', 'Joseph_Blatter', 'Evan_Rachel_Wood', 'Barbara_Walters', 'Fayssal_Mekdad', 'Brad_Johnson', 'Byron_Scott', 'David_Coulthard', 'Omar_Sharif', 'Paul_McNulty', 'Martha_Beatriz_Roque', 'Francis_Ford_Coppola', 'Marie-Reine_Le_Gougne', 'Jeanne_Moreau', 'Robert_Bonner', 'Kevin_Stallings', 'Pascal_Lamy', 'Penelope_Ann_Miller', 'Jane_Pauley', 'Allison_Janney', 'Edward_James_Olmos', 'Coretta_Scott_King', 'Saddam_Hussein', 'Charlton_Heston', 'Taufik_Hidayat', 'Osama_bin_Laden', 'Saparmurat_Niyazov', 'Imad_Moustapha', 'Karin_Stoiber', 'Jose_Mourinho', 'Leonard_Hamilton', 'Heidi_Fleiss', 'Claire_Hentzen', 'Ronald_Reagan', 'Mario_Cipollini', 'Alec_Baldwin', 'Gisele_Bundchen', 'Sophia_Loren', 'James_Maguire', 'Nestor_Kirchner', 'John_Brady', 'Abel_Pacheco', 'Carla_Myers', 'Luke_Walton', 'Bill_Belichick', 'Jo_Dee_Messina', 'Luis_Figo', 'Blythe_Danner', 'Yevgeny_Kafelnikov', 'Anthony_Hopkins', 'Sachiko_Yamada', 'Hisao_Oguchi', 'Jim_Harrick', 'Bo_Ryan', 'Carson_Daly', 'Elin_Nordegren', 'Ernesto_Zedillo', 'Steve_Park', 'Gregg_Popovich', 'Jorge_Castaneda', 'Thomas_Rupprath', 'Lindsay_Davenport', 'Johnson_Panjaitan', 'Francis_Mer', 'Eric_Hinske', 'Michel_Temer', 'Celine_Dion', 'Shaukat_Aziz', 'LeAnn_Rimes', 'Jeffrey_Archer', 'Hayley_Tullett', 'Stockard_Channing', 'Gerry_Parsky', 'Patty_Schnyder', 'Hamzah_Haz', 'Ashanti', 'Tony_Bennett', 'David_Nalbandian', 'Dalai_Lama', 'Sharon_Frey', 'Diane_Green', 'Cristina_Saralegui', 'Masum_Turker', 'Bridget_Fonda', 'Lana_Clarkson', 'Alvaro_Uribe', 'William_Ford_Jr', 'Robert_DeFraites', 'Elizabeth_Taylor', 'Rich_Gannon', 'Mike_Babcock', 'Paul-Henri_Mathieu', 'John_Malkovich', 'Abdel_Nasser_Assidi', 'Bill_Gates', 'Anthony_LaPaglia', 'Heizo_Takenaka', 'James_McGreevey', 'Jack_Straw', 'Yasser_Arafat', 'Antonio_Banderas', 'Christian_Fittipaldi', 'Robbie_Fowler', 'Mark_Hamister', 'Ismail_Merchant', 'Frank_Griswold', 'Robert_Duvall', 'George_Roy_Hill', 'Alvaro_Noboa', 'Hillary_Clinton', 'Bertrand_Bonello', 'Richard_Krajicek', 'George_Lopez', 'Anneli_Jaatteenmaki', 'Justin_Gatlin', 'Ralph_Lauren', 'Jean_Brumley', 'Dick_Clark', 'Eduardo_Duhalde', 'Chita_Rivera', 'Jason_Jennings', 'Fidel_Castro', 'Eric_Rosser', 'Munir_Akram', 'Olivia_Newton-John', 'Antony_Leung', 'Zoran_Djindjic', 'Gary_Forsee', 'Stanley_McChrystal', 'Joe_Mantello', 'Harry_Kalas', 'Lili_Taylor', 'Vincent_Brooks', 'Gary_Williams', 'Gianna_Angelopoulos-Daskalaki', 'Dick_Latessa', 'Bernard_Lord', 'Gian_Marco', 'Emmit_Smith', 'Goh_Kun', 'Dominik_Garcia-Lorido', 'Leland_Chapman', 'John_Kerry', 'Nabil_Shaath', 'Harry_Belafonte', 'Lea_Fastow', 'JJ_Redick', 'Marina_Anissina', 'Claire_Leger', 'Oswaldo_Paya', 'Anna_Kournikova', 'Martin_Brodeur', 'Greg_Rusedski', 'Pamela_Anderson', 'Goldie_Hawn', 'Hans_Eichel', 'Richard_Shelby', 'Raghad_Saddam_Hussein', 'Anthony_Fauci', 'Mike_Price', 'Silvan_Shalom', 'Joe_Torre', 'Owen_Wilson', 'Kevin_Spacey', 'John_Allen_Muhammad', 'Larry_Lucchino', 'Jonathan_Edwards', 'Laurent_Jalabert', 'Kalpana_Chawla', 'Daniel_Day-Lewis', 'Larry_Coker', 'Noah_Wyle', 'Dexter_Jackson', 'Amelia_Vega', 'Kim_Jong-Il', 'Bill_Graham', 'Carolyn_Dawn_Johnson', 'John_Abizaid', 'Chakib_Khelil', 'Amber_Tamblyn', 'Jean-Claude_Trichet', 'Carol_Burnett', 'Chuck_Yeager', 'Paula_Zahn', 'Orlando_Bloom', 'Jeremy_Shockey', 'Robert_Zoellick', 'Hipolito_Mejia']
