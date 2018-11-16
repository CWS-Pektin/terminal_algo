# terminal_algo
Shit. Algo.

Grundinfos:

Verteidigungs (FireWall) Einheiten

    Filter          1Core       Wand
    Encryptor       4Cores      Buff
    Destructor      3Cores      AoE Damage

Angriffs (Information) Einheiten
    Ping            1Bit        Einfacher Hit
    EMP             3Bit        Wände Killer
    Scrambler       1Bit        Einheiten Killer / Tank


Eh Wir Teilen Hier unsere Aktuelle Strategie

im Moment:

Angriff:
[[ 9, 4],[ 10, 3],[ 17, 3],[ 11, 2],[ 16, 2]]

Verteitigung:
[[ 2, 13],[ 3, 13],[ 4, 13],[ 5, 13],[ 12, 13],[ 13, 13],[ 14, 13],[ 15, 13],[ 22, 13],[ 23, 13],[ 24, 13],[ 25, 13]]



Lass ein Verteidigungs Layer aus Wänden bauen und dann nurnoch runde für runde checken was kaputt geht und dass neu aufbauen

Dann senden wir projektiele aus


Verteidigung neu:

Filter:
[[ 4, 12],[ 23, 12],[ 4, 11],[ 5, 11],[ 6, 11],[ 21, 11],[ 22, 11],[ 23, 11],[ 7, 9],[ 20, 9],[ 7, 8],[ 8, 8],[ 9, 8],[ 18, 8],[ 19, 8],[ 20, 8],[ 10, 6],[ 17, 6],[ 10, 5],[ 11, 5],[ 12, 5],[ 15, 5],[ 16, 5],[ 17, 5],[ 13, 3],[ 14, 3]]

26 Filter Kosten: 
26-Cores

Encryptor:
[[ 4, 13],[ 23, 13],[ 7, 10],[ 20, 10],[ 10, 7],[ 17, 7],[ 13, 4],[ 14, 4],[ 13, 2],[ 14, 2]]

10 Encryptors Kosten:
40-Cores

Destructor:
[[ 3, 13],[ 24, 13],[ 6, 10],[ 21, 10],[ 9, 7],[ 18, 7],[ 12, 4],[ 15, 4],[ 16, 2],[ 13, 1],[ 14, 1]]

11 Destructors Kosten:
33-Cores