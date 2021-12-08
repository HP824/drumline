# Drumline
----------

Create your own custom drumline objects!
Useful for planning out a drumline for the next marching season and creating
randomized drumlines for special occasions.

## Install
1. Clone the repository.
```sh
git clone https://github.com/HP824/drumline`
cd drumline
```
2. Make sure Python is installed, and pip as well.
Do NOT run `python3 setup.py install` directly.
```sh
# OPTIONAL: test app to ensure sanity
python3 -m unittest discover
python3 -m ensurepip --upgrade
pip3 install -e .
```
3. Restart your shell if needed and run `drumline`.

### Available commands:
* add (adds new member)
* list (lists all existing members)
* find (finds existing member)
* remove (removes existing member)
* promote (promotes years of drumline)
* scramble (assigns random roles to all members)
* quit (quits and exits program, changes are not saved)

### Usage:
###### Add a member to the drumline:
```
>>> add
Enter name of member: Harish
Enter year member is in (freshman, sophomore, junior, senior, alumnus): senior
Enter instrument for member (snare, tenors, bass, cymbals): snare
Added member successfully! :)
```

###### List members of drumline:
```
>>> list
Name: Varun, Year: junior, Instrument: tenors
Name: Adrian, Year: junior, Instrument: tenors
Name: Isaac, Year: senior, Instrument: snare
Name: Harish, Year: junior, Instrument: snare
Name: Siddharth, Year: junior, Instrument: snare
Name: Rebekah, Year: sophomore, Instrument: bass
Name: Brandon, Year: sophomore, Instrument: bass
Name: Avinash, Year: junior, Instrument: bass
Name: Aaditya, Year: sophomore, Instrument: bass
Name: John, Year: sophomore, Instrument: cymbals
Name: Ash, Year: sophomore, Instrument: cymbals
>>>
```

###### Find a single member in drumline
```
>>> find
Enter name of member (skip if unknown): 
Enter year they are in: (skip if unknown): 
Enter instrument they play (skip if unknown): snare
Multiple ambiguous results found, narrow your search
>>> find
Enter name of member (skip if unknown): Harish
Enter year they are in: (skip if unknown): 
Enter instrument they play (skip if unknown): snare
Name: Harish, Year: junior, Instrument: snare
>>> 
```

###### Remove a single member from drumline
```pycon
A sample drumline has already been created for you.
>>> remove
These are the current members:
1) Name: Varun, Year: junior, Instrument: tenors
2) Name: Adrian, Year: junior, Instrument: tenors
3) Name: Isaac, Year: senior, Instrument: snare
4) Name: Harish, Year: junior, Instrument: snare
5) Name: Siddharth, Year: junior, Instrument: snare
6) Name: Rebekah, Year: sophomore, Instrument: bass
7) Name: Brandon, Year: sophomore, Instrument: bass
8) Name: Avinash, Year: junior, Instrument: bass
9) Name: Aaditya, Year: sophomore, Instrument: bass
10) Name: John, Year: sophomore, Instrument: cymbals
11) Name: Ash, Year: sophomore, Instrument: cymbals
Which one do you want to remove? Enter the number: 11
Removed member successfully! :)
>>> list
Name: Varun, Year: junior, Instrument: tenors
Name: Adrian, Year: junior, Instrument: tenors
Name: Isaac, Year: senior, Instrument: snare
Name: Harish, Year: junior, Instrument: snare
Name: Siddharth, Year: junior, Instrument: snare
Name: Rebekah, Year: sophomore, Instrument: bass
Name: Brandon, Year: sophomore, Instrument: bass
Name: Avinash, Year: junior, Instrument: bass
Name: Aaditya, Year: sophomore, Instrument: bass
Name: John, Year: sophomore, Instrument: cymbals
>>> 
```

###### Promote all members of drumline to next grade (remove seniors/alumni)
```
A sample drumline has already been created for you.
>>> remove
These are the current members:
1) Name: Varun, Year: junior, Instrument: tenors
2) Name: Adrian, Year: junior, Instrument: tenors
3) Name: Isaac, Year: senior, Instrument: snare
4) Name: Harish, Year: junior, Instrument: snare
5) Name: Siddharth, Year: junior, Instrument: snare
6) Name: Rebekah, Year: sophomore, Instrument: bass
7) Name: Brandon, Year: sophomore, Instrument: bass
8) Name: Avinash, Year: junior, Instrument: bass
9) Name: Aaditya, Year: sophomore, Instrument: bass
10) Name: John, Year: sophomore, Instrument: cymbals
11) Name: Ash, Year: sophomore, Instrument: cymbals
Which one do you want to remove? Enter the number: 11
Removed member successfully! :)
>>> list
Name: Varun, Year: junior, Instrument: tenors
Name: Adrian, Year: junior, Instrument: tenors
Name: Isaac, Year: senior, Instrument: snare
Name: Harish, Year: junior, Instrument: snare
Name: Siddharth, Year: junior, Instrument: snare
Name: Rebekah, Year: sophomore, Instrument: bass
Name: Brandon, Year: sophomore, Instrument: bass
Name: Avinash, Year: junior, Instrument: bass
Name: Aaditya, Year: sophomore, Instrument: bass
Name: John, Year: sophomore, Instrument: cymbals
>>> 
```

###### Scramble all members of drumline
```
>>> list
Name: Varun, Year: junior, Instrument: tenors
Name: Adrian, Year: junior, Instrument: tenors
Name: Isaac, Year: senior, Instrument: snare
Name: Harish, Year: junior, Instrument: snare
Name: Siddharth, Year: junior, Instrument: snare
Name: Rebekah, Year: sophomore, Instrument: bass
Name: Brandon, Year: sophomore, Instrument: bass
Name: Avinash, Year: junior, Instrument: bass
Name: Aaditya, Year: sophomore, Instrument: bass
Name: John, Year: sophomore, Instrument: cymbals
Name: Ash, Year: sophomore, Instrument: cymbals
>>> scramble
Now scrambling the drumline. Here are your new roles:
Name: Varun, Year: junior, Instrument: snare
Name: Adrian, Year: junior, Instrument: bass
Name: Isaac, Year: senior, Instrument: cymbals
Name: Harish, Year: junior, Instrument: bass
Name: Siddharth, Year: junior, Instrument: snare
Name: Rebekah, Year: sophomore, Instrument: bass
Name: Brandon, Year: sophomore, Instrument: tenors
Name: Avinash, Year: junior, Instrument: tenors
Name: Aaditya, Year: sophomore, Instrument: snare
Name: John, Year: sophomore, Instrument: bass
Name: Ash, Year: sophomore, Instrument: cymbals
Would you like to replace the current drumline with the scrambled one?: y
>>> list
Name: Varun, Year: junior, Instrument: snare
Name: Adrian, Year: junior, Instrument: bass
Name: Isaac, Year: senior, Instrument: cymbals
Name: Harish, Year: junior, Instrument: bass
Name: Siddharth, Year: junior, Instrument: snare
Name: Rebekah, Year: sophomore, Instrument: bass
Name: Brandon, Year: sophomore, Instrument: tenors
Name: Avinash, Year: junior, Instrument: tenors
Name: Aaditya, Year: sophomore, Instrument: snare
Name: John, Year: sophomore, Instrument: bass
Name: Ash, Year: sophomore, Instrument: cymbals
>>> 
```

###### Quit the program
```
>>> quit
Goodbye!
```