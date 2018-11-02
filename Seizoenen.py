
# complexiteit : datetime next iterator
# titel : Seizoenen
# Bepaal het seizoen op een gegeven datum. Hierbij mag je ervan uitgaan dat het begin en het einde van de seizoenen vastligt op de datums weergegeven in onderstaande tabel.
#               seizoen 	begindatum 	    einddatum
#               lente 	    21 maart 	    20 juni
#               zomer 	    21 juni 	    22 september
#               herfst 	    23 september 	20 december
#               winter 	    21 december 	20 maart
#
# Invoer :
# De dag d∈N (1≤d≤31) en de naam van de maand van een gegeven datum.
# Uitvoer :
#  Een omschrijving die aangeeft welk seizoen het is op de gegeven datum. Gebruik
#
#     Het is seizoen op dag maand.
#
# als template voor de omschrijving, waarbij de cursieve fragmenten moeten ingevuld
# worden op basis van de gegeven en de berekende informatie.
#

dag = int(input(" Dag : "))
maand = input(" Maand : ")

jaar = 2016 # dummy schrikkeljaar om de invoer van jaar-02-29 toe te laten
from datetime import date, datetime
seizoenen = [('winter', (date(jaar,  1,  1),  date(jaar,  3, 20))),     # winter periode wordt opgesplitst in periode in het begin van het jaar en het einde
             ('lente',  (date(jaar,  3, 21),  date(jaar,  6, 20))),     # bij opvullen van de matrix wordt de juiste datum type opgenomen.
             ('zomer',  (date(jaar,  6, 21),  date(jaar,  9, 22))),
             ('herfst', (date(jaar,  9, 23),  date(jaar, 12, 20))),
             ('winter', (date(jaar, 12, 21),  date(jaar, 12, 31)))]

maanden = ['januari', 'februari', 'maart',
           'april', 'mei', 'juni',
           'juli', 'augustus', 'september',
           'oktober', 'november', 'december']
maand_int = maanden.index(maand) + 1

invoer_datum = date(jaar, maand_int, dag)

def bereken_seizoen(datum):
    if isinstance(datum, datetime):
        datum = datum.date()
    datum = datum.replace(year=jaar)
    return next(seizoen for seizoen, (begin, einde) in seizoenen
                if begin <= datum <= einde)

print('Het is {} op {} {}.'.format(bereken_seizoen(invoer_datum), maand, dag))
