# CodeathonURV2016_Raspi
Gestió eficient de recursos a l'aula/laboratori

Raspi és un projecte pensat per coordinar l'ús dels recursos de l'aula, com projector o els ordinadors, i facilitar
l'estalvi energètic i la gestió de material.

# Requeriments del sistema
Raspi està dissenyat per a treballar amb una base de dades relacional PostgreSQL.

## Servidor web públic
El servidor web de Raspi treballa amb el framework Django. Tot el sistema està muntat en Django, el qual permet
connectar-lo amb bases de dades, cachés, frontends i distribuïdors de càrrega sense cap problema.

## Serveis d'aula
Els serveis d'aula s'han dissenyat per a funcionar sobre un sistema Raspbian (Raspberry Pi). Això permet al sistema
comunicar-se amb mòduls de hardware i enviar senyals elèctriques o electròniques a dispositius de l'aula.

Utilitzar un mòdul com la Raspberry Pi permet abaratir el projecte, oferir connexions electròniques directament, i
facilitar la comunicació entre servidor i clients. Es pot actualitzar la versió de Raspi fàcilment per a descarregar nous
mòduls de l'aplicació.

## Controladors hardware
Els controladors oferits per Raspi en aquest prototip es desenvolupen en Python i utilitzen llibreries GPIO de RPi per
connectar-se al hardware. Raspi està pensat per suportar qualsevol tipus de controladors, i, per tant, oferir un camí
d'actualitzacions i millores futures molt flexible.