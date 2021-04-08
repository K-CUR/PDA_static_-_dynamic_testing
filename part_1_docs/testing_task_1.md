### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# Line 2: equals should be == not =
# Line 4: colon missing from end of else.
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# Line 1: spelling error dif instead of def
# Line 1: comma missing after card1
# Line 3: card is not a parameter. It needs to be card1 or card2.
# Lines 1 to 4: need to be indented one tab.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# Lines 1 to 4: need to be indented one tab.
# Line 2: total not defined. Should be total = x, x being a value
# Line 5: total is an integer so need to convert it to string to add it to 
#         concatenate it to a string.
# Line 5: space needed before closing quotation marks

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```